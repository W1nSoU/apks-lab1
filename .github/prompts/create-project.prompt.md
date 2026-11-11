---
name: create-project
description: "Команда створення базової структури каталогів та початкового README."
---

# Command: create-project

## Передумови
- Виконано команду `git-init`.

## Дії агента
1. Викликати skill `project-scaffold`.
2. Створити каталоги:
   - `src/main/java/com/example`
   - `src/test/java/com/example`
   - `docs/`
3. Створити початковий `README.md` із зазначенням:
   - ПІП: Душинський Даніїл
   - Група: КІ-406
   - Варіант 5: Java (Maven + JUnit 5)
   - Призначення проєкту та спосіб запуску агента.

## Очікувані файли
- `README.md`
- Каталог `src/main/java/com/example`
- Каталог `src/test/java/com/example`

## Команди перевірки
```bash
test -d src/main/java/com/example && test -f README.md && echo "OK: Structure created"
```

## Повідомлення про помилку
- *Помилка:* "Неможливо створити каталоги проєкту".
- *Рішення:* Перевірити права запису у поточну папку.
