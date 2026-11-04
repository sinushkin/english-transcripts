#!/usr/bin/env python3
"""
Скачивает субтитры всех видео с плейлиста YouTube и записывает инфо в CSV.
- Первый запуск: загружает плейлист, сохраняет URL+названия в CSV, затем скачивает субтитры
- Следующие запуски: пропускает уже скаченные, продолжает с того же места
"""

import sys
import csv
import os
import json
import subprocess
from pathlib import Path
from typing import Set, Tuple, List
import pandas as pd

def load_playlist_from_youtube(playlist_url: str) -> List[dict]:
    """Загружает список видео с YouTube плейлиста."""
    print(f"📺 Загружаю плейлист: {playlist_url}")

    cmd = [
        'yt-dlp',
        '-j',
        '--flat-playlist',
        playlist_url
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        videos = []

        if result.returncode == 0 and result.stdout.strip():
            for line in result.stdout.strip().split('\n'):
                if line.strip():
                    try:
                        data = json.loads(line)
                        if 'id' in data:
                            videos.append(data)
                    except json.JSONDecodeError:
                        pass

        if not videos:
            print(f"⚠️  Не удалось загрузить плейлист. stderr: {result.stderr[:200]}")

        return videos
    except subprocess.TimeoutExpired:
        print(f"❌ Таймаут при загрузке плейлиста (>60с)")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        sys.exit(1)

def init_csv_from_playlist(csv_path: str, videos: List[dict]) -> pd.DataFrame:
    """Инициализирует CSV из плейлиста."""
    data = []
    for video in videos:
        data.append({
            'url': f"https://www.youtube.com/watch?v={video['id']}",
            'title': video.get('title', 'Unknown'),
            'subtitle_file': None  # Будет заполнено при скачивании
        })

    df = pd.DataFrame(data)
    df.to_csv(csv_path, index=False)
    print(f"✅ Создан CSV с {len(df)} видео: {csv_path}")
    return df

def load_csv(csv_path: str) -> pd.DataFrame:
    """Загружает существующий CSV."""
    if not os.path.exists(csv_path):
        return None

    try:
        df = pd.read_csv(csv_path)
        return df
    except Exception as e:
        print(f"⚠️  Ошибка при чтении CSV: {e}")
        return None

def download_subtitle(video_url: str, output_dir: str) -> Tuple[bool, str]:
    """Скачивает субтитры для одного видео. Возвращает (успех, путь_файла)."""
    cmd = [
        'yt-dlp',
        '--skip-download',
        '--write-subs',
        '--write-auto-subs',
        '--sub-langs', 'ru',
        '--convert-subs', 'srt',
        '-o', os.path.join(output_dir, '%(id)s'),
        '--extractor-args', 'youtube:player_client=web,mweb,android',
        video_url
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        # Извлекаем ID видео из URL
        video_id = video_url.split('v=')[-1].split('&')[0]
        srt_file = os.path.join(output_dir, f'{video_id}.ru.srt')

        if os.path.exists(srt_file):
            return True, srt_file
        else:
            return False, ""
    except subprocess.TimeoutExpired:
        print(f"  ⚠️  Таймаут при скачивании субтитров")
        return False, ""
    except Exception as e:
        print(f"  ⚠️  Ошибка: {e}")
        return False, ""

def main():
    if len(sys.argv) < 2:
        print("❌ Использование: python3 download_playlist_subs.py <playlist_url> [output_csv]")
        print("Пример: python3 download_playlist_subs.py 'https://www.youtube.com/playlist?list=PLxxx' playlist.csv")
        sys.exit(1)

    playlist_url = sys.argv[1]
    csv_path = sys.argv[2] if len(sys.argv) > 2 else 'playlist.csv'
    output_dir = 'subtitles'

    # Создаем директорию для субтитров
    os.makedirs(output_dir, exist_ok=True)

    # Проверяем, есть ли уже CSV
    df = load_csv(csv_path)

    if df is None:
        # Первый запуск: загружаем плейлист и создаем CSV
        videos = load_playlist_from_youtube(playlist_url)
        if not videos:
            print("❌ Не удалось загрузить плейлист")
            sys.exit(1)

        df = init_csv_from_playlist(csv_path, videos)
    else:
        print(f"✅ Загружен существующий CSV с {len(df)} видео")

    # Подсчитываем уже скаченные
    downloaded = df['subtitle_file'].notna().sum()
    pending = df['subtitle_file'].isna().sum()

    print(f"📊 Статус: {downloaded} скачано, {pending} осталось")

    if pending == 0:
        print("✅ Все видео уже скачаны!")
        return

    # Скачиваем субтитры для видео без файлов
    processed = 0
    skipped_errors = 0
    for idx, row in df.iterrows():
        if pd.notna(row['subtitle_file']):
            # Уже скачано
            continue

        video_url = row['url']
        title = row['title']

        print(f"[{idx+1}/{len(df)}] ⬇️  {title[:60]}")

        try:
            # Скачиваем субтитры
            success, srt_path = download_subtitle(video_url, output_dir)

            if success:
                # Обновляем DataFrame
                df.at[idx, 'subtitle_file'] = srt_path

                # Сохраняем CSV после каждого видео
                df.to_csv(csv_path, index=False)

                print(f"  ✅ Сохранено: {srt_path}")
                processed += 1
            else:
                print(f"  ⏭️  Пропущено (нет субтитров)")
                skipped_errors += 1
        except Exception as e:
            print(f"  ⚠️  Ошибка: {str(e)[:50]}")
            skipped_errors += 1
            continue

    print(f"\n📈 В этом сеансе скачано: {processed}")
    total_downloaded = df['subtitle_file'].notna().sum()
    print(f"📊 Всего скачано: {total_downloaded}/{len(df)}")
    print(f"📁 CSV файл: {csv_path}")

if __name__ == '__main__':
    main()
