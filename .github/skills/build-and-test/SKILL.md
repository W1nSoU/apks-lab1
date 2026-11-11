---
name: build-and-test
description: "Налаштування конфігурації Maven (pom.xml), коду застосунку, юніт-тестів JUnit 5 та скриптів збірки ci.sh / ci.bat."
version: 1.0.0
---

# Skill: build-and-test

## 1. Призначення
Створення повної конфігурації складання для Java-проєкту з використанням Apache Maven, реалізація точки входу застосунку з тестовою логікою додавання, юніт-тестів на базі JUnit 5, а також генерація автономних скриптів `ci.sh` та `ci.bat` для виконання збірки в один клік на будь-якій ОС.

## 2. Вхідні параметри
- `java_version`: цільова версія Java SE (17 LTS).
- `main_class`: повне ім'я головного класу (`com.example.App`).
- `test_framework`: тестовий фреймворк (`JUnit 5 Jupiter` версії 5.10.2).
- `artifact_name`: ім'я вихідного jar-файлу (`hello.jar`).

## 3. Створювані артефакти
- `pom.xml`: конфігурація Maven із залежностями `junit-jupiter`, плагінами `maven-compiler-plugin`, `maven-surefire-plugin` та `maven-shade-plugin` для збірки виконуваного fat/uber JAR.
- `src/main/java/com/example/App.java`: вихідний код із методом `main` (виводить "Hello, World! From Variant 5 (Java/Maven)") та статичним методом `add(int a, int b)`.
- `src/test/java/com/example/BasicAdditionTest.java`: набір юніт-тестів, що верифікують роботу методу `App.add(a, b)` (додатні числа, від'ємні числа, нуль).
- `ci.sh`: shell-скрипт для Linux та macOS (з правами `chmod +x`), що компілює проєкт, проганяє тести, збирає JAR і перевіряє його запуск.
- `ci.bat`: командний файл для Windows, що виконує аналогічні дії на платформі Windows.

## 4. Критерії перевірки (Verification)
1. Команда `mvn test` завершується з результатом `BUILD SUCCESS` (0 failed, 0 errors).
2. Команда `mvn package` створює файл `target/hello.jar`.
3. Команда `java -jar target/hello.jar` повертає код виходу `0` та виводить очікуване привітання.
4. Скрипт `./ci.sh` успішно відпрацьовує на macOS/Linux без помилок.

## 5. Типові сценарії помилок та їх вирішення
- **Помилка: Maven не знаходить інсталяцію JDK або версія нижча за 17.**
  - *Дія агента:* Перевірити `JAVA_HOME`, вказати явно сумісність `<source>17</source>` та `<target>17</target>` у `pom.xml`.
- **Помилка: JUnit тести не запускаються під час `mvn test`.**
  - *Дія агента:* Переконатися, що `maven-surefire-plugin` додано з версією `>= 3.2.5` для коректної підтримки JUnit Platform Provider.
