#!/usr/bin/env bash
# Печатает список ссылок «видео на нужном месте» из файлов разбора.
# Использование:
#   ./get-links.sh transcript/2oScAyV9p0A.md        # один файл
#   ./get-links.sh transcript/*.md                  # несколько файлов
#   ./get-links.sh transcript                       # вся папка
#   ./get-links.sh -g "take over" transcript        # только строки, где есть текст
# Вывод: «m:ss<TAB>фраза<TAB>ссылка», перед каждым файлом — строка «# ID — заголовок».

set -u

pattern=""
if [ "${1:-}" = "-g" ]; then
  [ $# -ge 2 ] || { echo "нужен текст после -g" >&2; exit 2; }
  pattern=$2
  shift 2
fi

if [ $# -eq 0 ]; then
  echo "Использование: $0 [-g текст] файл.md|папка ..." >&2
  exit 2
fi

files=()
for arg in "$@"; do
  if [ -d "$arg" ]; then
    for f in "$arg"/*.md; do [ -e "$f" ] && files+=("$f"); done
  elif [ -f "$arg" ]; then
    files+=("$arg")
  else
    echo "нет такого файла: $arg" >&2
  fi
done

for f in "${files[@]}"; do
  out=$(awk -v pat="$pattern" '
    function strip(s) { gsub(/\*\*/, "", s); gsub(/^[ \t]+|[ \t]+$/, "", s); return s }
    /\[▶ [0-9]+:[0-9][0-9]\]\(https:\/\/youtu\.be\// {
      line = $0
      if (!match(line, /\[▶ [0-9:]+\]\(https[^)]*\)/)) next
      link = substr(line, RSTART, RLENGTH)
      rest = substr(line, 1, RSTART - 1) substr(line, RSTART + RLENGTH)
      t = link; sub(/^\[▶ /, "", t); sub(/\].*/, "", t)
      u = link; sub(/^[^(]*\(/, "", u); sub(/\)$/, "", u)
      sub(/^## [0-9]+\. /, "", rest)
      sub(/^- /, "", rest)
      label = strip(rest)
      if (pat != "" && index(tolower(label), tolower(pat)) == 0) next
      print t "\t" label "\t" u
    }' "$f")
  [ -n "$out" ] || continue
  title=$(head -1 "$f" | sed 's/^# *//')
  echo "# $(basename "$f" .md) — $title"
  echo "$out"
done
