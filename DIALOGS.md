# DIALOGS.md - Interactive Dialog Learning System

## 📚 Назначение

Диалоги разработаны для использования в интерактивной системе обучения (аналог `~/langteacher`), где:
1. **Claude спрашивает** - задает вопрос на английском
2. **Claude подсказывает** - дает подсказку на русском как ответить
3. **Ты отвечаешь** - отвечаешь по-английски (может быть ошибки)
4. **Claude исправляет** - показывает правильный ответ с идиомой и дает ссылку на видео для доп. изучения

---

## 📖 Структура диалога

```markdown
# Dialog N: Theme Name

**Level:** A2/B1/B2/C1
**Duration:** 3-4 minutes
**Key idioms:** 3-5 выражений
**Target:** Описание цели обучения

## Characters
- **Person A:** Description
- **Person B:** Description

## Full Dialogue
[Полный текст диалога с примерами использования идиом]

## Learning Points

### Expression 1: "idiom here"

**English question (Claude asks):**
What would you say if...?

**Russian hint (Claude provides):**
[Подсказка на русском - как перефразировать ответ без идиомы]

**Correct answer with idiom:**
Full sentence using the idiom correctly.

**Reference (Video Link + Timestamp):**
- **Video ID:** ABC123xyz
- **Timestamp:** 00:15-00:25
- **Source:** [Expression description from video analysis]
- **Full phrase context:** [How it was used in the video]

**Alternative expressions:**
- Similar idioms or phrasal verbs
- Formal vs informal variations
- Common mistakes to avoid

---

### Expression 2: [repeat above structure]
```

---

## 🎯 Правила для использования диалогов

### Для Claude (интерактивная работа):

1. **Выбор expresion** - из диалога случайно выбрать 2-3 ключевых выражения
2. **Вопрос** - спросить на английском (контекст из диалога)
3. **Подсказка** - если нужна, дать на русском
4. **Ответ пользователя** - дождаться его ответа на английском
5. **Корректировка** - исправить ошибки, показать правильный вариант
6. **Ссылка** - дать видео-ссылку (ID + timestamp) для самостоятельного изучения

### Для пользователя (тебя):

- Отвечай так естественно как сможешь (ошибки OK!)
- Старайся использовать идиомы из подсказки
- Если застрял - попроси еще подсказку
- После исправления - смотри видео для закрепления

---

## 📊 Метаданные диалогов

| Параметр | Значение | Примеры |
|----------|----------|---------|
| **Level** | A2, B1, B2, C1 | Beginner → Advanced |
| **Duration** | 3-4 минут | На основе текста |
| **Idioms per dialog** | 3-5 | Ключевые выражения |
| **Video references** | ID + Timestamp | FOzoCpD27Cs 00:15-00:25 |
| **Topic categories** | 8 групп | Job, Travel, Social, etc. |

---

## 🗂️ Категории диалогов (20 всего)

### Professional (5 диалогов)
- Job Interview
- Workplace Conflict Resolution
- Team Meeting
- Project Deadline Discussion
- Salary Negotiation

### Social/Casual (5 диалогов)
- First Date
- Making Plans with Friends
- Complaining About Work
- Gossip/Small Talk
- Party Conversation

### Travel (3 диалога)
- At the Airport
- Hotel Check-in
- Restaurant Ordering

### Personal Growth (3 диалога)
- Motivation/Encouragement
- Problem Solving
- Health/Fitness Goals

### Education (2 диалога)
- Student-Teacher Discussion
- Peer Tutoring

### Lifestyle (2 диалога)
- Moving House
- Shopping/Negotiations

---

## 🔗 Видео-ссылки (из 227 анализированных видео)

Каждое выражение ссылается на:
- **Video ID** - идентификатор YouTube видео
- **Timestamp** - где разбирается выражение (примерно)
- **Context** - как оно было использовано в видео

Примеры часто используемых видео:
- `V3LxVLQe5QA` - 30 крутых выражений (around the clock...)
- `OPdiTXzllOM` - Идиомы (break a leg, etc.)
- `QGib5gpTTKI` - 20 фразовых глаголов (take on, etc.)
- `Phm5iIZbks4` - 50 фраз (all set, etc.)

---

## ⚙️ Интеграция с LangTeacher

Планируемый workflow:
```
1. User runs: langteacher --dialogs
2. Claude selects random dialog & expression
3. Claude asks in English + Russian hint
4. User answers (any form)
5. Claude corrects & shows proper idiom
6. Claude provides video link for self-study
7. Repeat with next expression
```

---

## 📝 Версия: 1.0
**Created:** 2026-11-04  
**Total Dialogs:** 20  
**Total Expressions:** 80-100  
**Video References:** 40+ из 227 анализированных  

---

## 🎓 Цель

Интерактивное изучение английских идиом через **практические диалоги** + **видео-примеры** из реальных уроков Dragon Club YouTube.
