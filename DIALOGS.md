# DIALOGS.md — диалоги для интерактивной тренировки

Папка `dialogs/` — диалоги по 280–350 слов (примерно 2,5 минуты речи) для тренировки в формате LangTeacher. В каждом диалоге идиомы стоят примерно в каждой второй реплике и выделены **жирным**. Идиомы взяты только из реально разобранных видео плейлиста.

## Сценарий тренировки (для Claude)

1. Выбрать диалог и карточку (`### N. фраза`).
2. Задать вопрос из поля **Ask (EN)** по-английски.
3. По просьбе показать **Hint (RU)** — как это сказать по-русски, без идиомы на английском.
4. Пользователь отвечает по-английски (возможно, с ошибками).
5. Разобрать ответ и показать **Model answer** с идиомой, объяснить разницу.
6. Дать ссылку из поля **In the video** — ссылка открывает видео на нужной секунде.

## Формат файла

```
# Dialog NN: Название
Level · Setting · Length · Idioms
## Dialogue      — реплики, идиомы выделены **жирным**
## Cards         — по одной карточке на идиому:
   Ask (EN) / Hint (RU) / Model answer / In the video «значение из видео» — ссылка ?t=секунды
```

## Откуда таймкоды

- Источник — `.ru.srt` из `~/data/dragon-club/subtitles/`, время — **начало момента, где учитель вводит фразу**. Ссылка ведёт на несколько секунд раньше разбора.
- Субтитры — русское автораспознавание английской речи, английские слова в них искажены. Момент определяется по русским репликам учителя («не торопись», «взять под контроль» и т. д.).
- Единая таблица «фраза → видео → секунда» хранилась в скрипте-сборщике. Здесь ссылки лишь сгенерированы из неё, поэтому секунды везде совпадают с `mm:ss`.
- Допущение: фраза «take your time» взята как перевод учителя «не торопись» (2oScAyV9p0A @ 1:10); автораспознавание не позволяет подтвердить точное английское слово.

## Источники (6 видео, ~45 фраз)

| Видео | Тема |
|---|---|
| `2oScAyV9p0A` | фразы с TAKE |
| `BohT_bO9OWY` | фразы с GET |
| `jQeqtYCYF90` | фразы с PUT |
| `FOzoCpD27Cs` | pass by, get over, fall short, slip one's mind, hold back |
| `PD2uFZIF36U` | get on one's nerves, get by, shoot a message, get back to, see off, take a year off, set off, kick off, lose track of time |
| `BrI2MsgT7dU` | beat around the bush, keep to oneself, workaholic, outside of work, apparently, overcome one's fears, socialize, crack of dawn, dizzy spells, rolling stone |

## Список диалогов

1. First week at a new job · 2. Noisy neighbours · 3. A missed deadline · 4. Planning a trip abroad · 5. Getting promoted · 6. After a breakup · 7. A new hobby · 8. At the doctor's · 9. Launching a new product · 10. Parent-teacher meeting · 11. Family budget · 12. Running at dawn · 13. Moving abroad · 14. University group project · 15. Old friends reunion

## Что дальше

Чтобы добавлять новые диалоги, сначала нужно по-настоящему разобрать больше видео (сейчас полноценно разобрано 34 из 228 транскриптов, остальные — заглушки), затем строить диалоги на их фразах с таймкодами из `.srt`.
