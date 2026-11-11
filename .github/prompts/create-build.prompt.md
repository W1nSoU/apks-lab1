---
name: create-build
description: "Команда налаштування системи складання Maven, юніт-тестів та скриптів ci.sh/ci.bat."
---

# Command: create-build

## Передумови
- Виконано команду `create-project`.

## Дії агента
1. Викликати skill `build-and-test`.
2. Створити `pom.xml`:
   - Java 17 LTS.
   - Залежність `org.junit.jupiter:junit-jupiter:5.10.2`.
   - `maven-surefire-plugin` (версія 3.2.5).
   - `maven-shade-plugin` для збірки `target/hello.jar` з головним класом `com.example.App`.
3. Створити вихідний код `src/main/java/com/example/App.java`:
   - Вивід "Hello, World! From Variant 5 (Java/Maven)".
   - Метод `public static int add(int a, int b) { return a + b; }`.
4. Створити юніт-тест `src/test/java/com/example/BasicAdditionTest.java`:
   - Тести методу `add`: додатні числа, від'ємні числа, додавання нуля.
5. Створити скрипти збірки:
   - `ci.sh`: збірка та запуск тестів на Linux/macOS. Встановити `chmod +x`.
   - `ci.bat`: збірка та запуск тестів на Windows.

## Очікувані файли
- `pom.xml`
- `src/main/java/com/example/App.java`
- `src/test/java/com/example/BasicAdditionTest.java`
- `ci.sh`
- `ci.bat`

## Команди перевірки
```bash
test -f pom.xml && test -f ci.sh && test -f ci.bat && echo "OK: Build files created"
```

## Повідомлення про помилку
- *Помилка:* "Синтаксична помилка у pom.xml або відсутні скрипти збірки".
- *Рішення:* Перевірити XML валідатором та переконатися у наявності дозволу на виконання для `ci.sh`.
