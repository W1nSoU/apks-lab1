# ЗВІТ З ЛАБОРАТОРНОЇ РОБОТИ № 1

**Тема:** Проєктування AI-агента для автоматизації розробки та CI/CD  
**Дисципліна:** Архітектура паралельних комп'ютерних систем (АПКС)  
**Виконав:** студент групи КІ-406 Душинський Даніїл  
**Варіант:** 5 (Java 17 LTS / Apache Maven / JUnit 5)  
**Національний університет «Львівська політехніка»**  
**2026 рік**

---

## 1. Мета роботи
Набути практичних навичок проєктування та використання AI-автоматизації у розробці програмного забезпечення. Опанувати перетворення вимог на структуру AI-агента, розробку маніфесту агента (manifest), навичок (skills), команд (commands), оркестратора (orchestrator), а також створення кросплатформного проєкту з автоматизованим складанням, тестуванням і CI/CD на базі GitHub Actions (Ubuntu, Windows, macOS).

---

## 2. Опис задачі, яку вирішує AI-агент
AI-агент **`build-engineer`** автоматизує процес розгортання, збірки, тестування та інтеграції кросплатформного Java-проєкту. Агент усуває необхідність ручного створення файлової структури, конфігурації `pom.xml`, написання тестів та скриптів CI/CD.

Основні задачі:
1. Автономне створення ієрархії каталогів та `.gitignore`.
2. Генерація робочого коду застосунку та юніт-тестів на базі JUnit 5.
3. Створення кросплатформних скриптів складання (`ci.sh` для Unix-подібних ОС та `ci.bat` для Windows).
4. Налаштування матричного CI/CD workflow у GitHub Actions для трьох цільових ОС (`ubuntu-latest`, `windows-latest`, `macos-latest`).
5. Валідація цілісності та безпеки (контроль відсутності тимчасових каталогів `target/` та секретів у Git).

---

## 3. Таблиця та схема взаємодії компонентів

| Компонент | Тип | Роль / Призначення |
| :--- | :--- | :--- |
| `build-engineer.agent.md` | Manifest | Опис ролі агента, правил безпеки, обмежень та критеріїв DoD |
| `project-scaffold` | Skill | Створення файлової структури, каталогів пакетів та `.gitignore` |
| `build-and-test` | Skill | Генерація `pom.xml`, `App.java`, тестів JUnit 5 та скриптів збірки |
| `github-actions` | Skill | Генерація `.github/workflows/ci.yml` із кросплатформною матрицею |
| `git-init` | Command | Перевірка статусу Git, ініціалізація та оновлення `.gitignore` |
| `create-project` | Command | Виклик скіла `project-scaffold` |
| `create-build` | Command | Виклик скіла `build-and-test` |
| `create-actions` | Command | Виклик скіла `github-actions` |
| `check` | Command | Комплексна перевірка коду, тестів, структури та конфігурацій |
| `init` | Orchestrator | Послідовний виклик команд: `git-init` -> `create-project` -> `create-build` -> `create-actions` -> `check` |

### Схема передачі управління:
```text
[Користувач / /init]
       │
       ▼
[init (Orchestrator)]
       ├─► [1. git-init] ─────────► Створює .gitignore
       ├─► [2. create-project] ───► Створює src/, docs/, README.md (через project-scaffold)
       ├─► [3. create-build] ─────► Створює pom.xml, Java код, JUnit, ci.sh/bat (через build-and-test)
       ├─► [4. create-actions] ───► Створює .github/workflows/ci.yml (через github-actions)
       └─► [5. check] ────────────► Запускає локальні тести, перевіряє DoD та статус Git
```

---

## 4. Лістинг маніфесту агента (`.github/agents/build-engineer.agent.md`)
```markdown
---
name: build-engineer
role: Build & CI/CD Automation Engineer
description: "Спеціалізований AI-агент для автоматизації ініціалізації, складання, тестування та налаштування кросплатформного CI/CD пайплайну для Java/Maven проєкту."
version: 1.0.0
---

# Агентський маніфест: Build Engineer

## 1. Роль та призначення
Build Engineer - це автономний інженерний AI-агент, призначений для автоматизації повного циклу розробки програмного забезпечення на базі Java та Apache Maven:
- Генерація структури проєкту та конфігураційних файлів.
- Налаштування системи автоматичного складання (Maven) та тестування (JUnit 5).
- Реалізація кросплатформних скриптів складання (ci.sh та ci.bat).
- Створення та валідація матричного CI/CD workflow для GitHub Actions.
- Верифікація якості коду, проходження тестів та цілісності репозиторію.

## 2. Область відповідальності
1. Створення мінімального, валідного та автономного Java-проєкту з вихідним кодом у src/main/java/ та тестами у src/test/java/.
2. Забезпечення детермінованого складання у виконуваний артефакт target/hello.jar.
3. Контроль відсутності тимчасових каталогів (target/, .idea/, кешів) у системі контролю версій Git.
4. Забезпечення проходження юніт-тестів на всіх підтримуваних операційних системах.
5. Надання повної документації та журналів взаємодії.

## 3. Доступні навички (Skills)
- project-scaffold: створює структуру каталогів проєкту, базовe середовище та .gitignore.
- build-and-test: генерує pom.xml, вихідний код, тести JUnit 5 та скрипти складання ci.sh, ci.bat.
- github-actions: створює матричний файл .github/workflows/ci.yml для трьох ОС (Ubuntu, Windows, macOS).

## 4. Доступні команди (Commands)
- git-init, create-project, create-build, create-actions, check, init.

## 5. Правила роботи та безпека
- Заборонено видаляти файли за межами робочої директорії.
- Заборонено виконувати git push --force або переписувати історію Git.
- Заборонено генерувати або передавати токени, приватні ключі чи паролі.
- Ідемпотентність: повторний запуск не повинен ламати створений проєкт.

## 6. Критерії завершення (DoD)
- Усі файли проєкту згенеровані.
- pom.xml валідний і успішно збирає проєкт під Java 17.
- Тест BasicAdditionTest успішно проходить за допомогою mvn test.
- Створюється виконуваний файл target/hello.jar.
- Скрипти ci.sh та ci.bat повертають код 0.
- Відсутні сміттєві файли та секрети в Git.
```

---

## 5. Посилання та лістинги Skills
1. **`project-scaffold`** — [.github/skills/project-scaffold/SKILL.md](../.github/skills/project-scaffold/SKILL.md)
2. **`build-and-test`** — [.github/skills/build-and-test/SKILL.md](../.github/skills/build-and-test/SKILL.md)
3. **`github-actions`** — [.github/skills/github-actions/SKILL.md](../.github/skills/github-actions/SKILL.md)

---

## 6. Посилання та лістинги Commands
1. **`git-init`** — [.github/prompts/git-init.prompt.md](../.github/prompts/git-init.prompt.md)
2. **`create-project`** — [.github/prompts/create-project.prompt.md](../.github/prompts/create-project.prompt.md)
3. **`create-build`** — [.github/prompts/create-build.prompt.md](../.github/prompts/create-build.prompt.md)
4. **`create-actions`** — [.github/prompts/create-actions.prompt.md](../.github/prompts/create-actions.prompt.md)
5. **`check`** — [.github/prompts/check.prompt.md](../.github/prompts/check.prompt.md)
6. **`init` (Orchestrator)** — [.github/prompts/init.prompt.md](../.github/prompts/init.prompt.md)

---

## 7. Ключові файли вихідного проєкту

### 7.1. Дескриптор складання (`pom.xml`)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>hello-world-java</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <name>Hello World Java Application</name>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <junit.jupiter.version>5.10.2</junit.jupiter.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${junit.jupiter.version}</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.13.0</version>
                <configuration>
                    <source>17</source>
                    <target>17</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.2.5</version>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.5.2</version>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                        <configuration>
                            <outputFile>${project.build.directory}/hello.jar</outputFile>
                            <transformers>
                                <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                                    <mainClass>com.example.App</mainClass>
                                </transformer>
                            </transformers>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>
```

### 7.2. Вихідний код застосунку (`src/main/java/com/example/App.java`)
```java
package com.example;

public class App {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("Hello, World! From Variant 5 (Java / Maven)");
        System.out.println("Student: Душинський Даніїл, Group: КІ-406");
        System.out.println("==================================================");

        int a = 2;
        int b = 3;
        int result = add(a, b);
        System.out.println("Verification calculation: " + a + " + " + b + " = " + result);

        if (result == 5) {
            System.out.println("Status: BasicAddition logic verified successfully!");
        } else {
            System.err.println("Status: Calculation error!");
            System.exit(1);
        }
    }
}
```

### 7.3. Юніт-тести (`src/test/java/com/example/BasicAdditionTest.java`)
```java
package com.example;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class BasicAdditionTest {
    @Test
    @DisplayName("BasicAddition: Тест додавання двох додатних чисел (2 + 3 == 5)")
    public void testPositiveAddition() {
        int result = App.add(2, 3);
        assertEquals(5, result, "2 + 3 повинно дорівнювати 5");
    }

    @Test
    @DisplayName("BasicAddition: Тест додавання з нулем (10 + 0 == 10)")
    public void testAdditionWithZero() {
        int result = App.add(10, 0);
        assertEquals(10, result, "10 + 0 повинно дорівнювати 10");
    }

    @Test
    @DisplayName("BasicAddition: Тест додавання від'ємних чисел (-4 + -6 == -10)")
    public void testNegativeAddition() {
        int result = App.add(-4, -6);
        assertEquals(-10, result, "-4 + -6 повинно дорівнювати -10");
    }

    @Test
    @DisplayName("BasicAddition: Тест додавання додатного та від'ємного числа (7 + -3 == 4)")
    public void testMixedAddition() {
        int result = App.add(7, -3);
        assertEquals(4, result, "7 + -3 повинно дорівнювати 4");
    }
}
```

### 7.4. GitHub Actions CI Workflow (`.github/workflows/ci.yml`)
```yaml
name: Cross-Platform CI (Ubuntu, Windows, macOS)

on:
  push:
    branches:
      - develop
      - master
      - 'feature/**'
  pull_request:
    branches:
      - develop
      - master

jobs:
  build-and-test:
    name: Build & Test on ${{ matrix.os }}
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]

    steps:
      - name: 1. Checkout repository code
        uses: actions/checkout@v4

      - name: 2. Set up JDK 17 (Temurin)
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'
          cache: 'maven'

      - name: 3. Make CI script executable (Linux/macOS)
        if: runner.os != 'Windows'
        run: chmod +x ci.sh

      - name: 4. Execute build & test via ci.sh (Linux/macOS)
        if: runner.os != 'Windows'
        run: bash ./ci.sh

      - name: 5. Execute build & test via ci.bat (Windows)
        if: runner.os == 'Windows'
        run: .\ci.bat

      - name: 6. Upload built artifact (hello.jar)
        uses: actions/upload-artifact@v4
        with:
          name: hello-app-${{ matrix.os }}
          path: target/hello.jar
          if-no-files-found: error
          retention-days: 7
```

---

## 8. Журнал запитів до AI та виправлення помилки

- **Опис проблеми:**  
  Під час початкового формування файлу `.github/workflows/ci.yml` AI-генератор згенерував прямі команди `mvn -B package` всередині YAML кроків. Це порушувало вимогу методичних вказівок (розділ 2), де зазначено, що `ci.yml` повинен містити лише виклик скриптів `ci.sh` або `ci.bat`, а вся логіка збірки має перебувати в цих скриптах.
- **Виправлення:**  
  AI переписав структуру робочого процесу GitHub Actions, створив файли `ci.sh` і `ci.bat` з повною інкапсуляцією збірки, тестування і перевірки `hello.jar`, а у `ci.yml` залишив тільки виклики:
  - `bash ./ci.sh` (для Linux та macOS);
  - `.\ci.bat` (для Windows).
- **Результат:** Пайплайн відповідає стандарту безпеки та повністю ізольований від налаштувань середовища CI.

---

## 9. Результати локального складання і тестування
Локальний запуск скрипта `./ci.sh` на робочій станції розробника:
```text
==========================================================
 [CI Build Script - Linux / macOS]
 Project: Hello World Java (Variant 5)
 Student: Душинський Даніїл (КІ-406)
 Date: Wed Nov 11 12:39:04 EET 2026
==========================================================
--> Step 1/4: Cleaning & Compiling...
[INFO] BUILD SUCCESS
--> Step 2/4: Running Unit Tests (BasicAddition)...
[INFO] Running com.example.BasicAdditionTest
[INFO] Tests run: 4, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 0.017 s -- in com.example.BasicAdditionTest
[INFO] BUILD SUCCESS
--> Step 3/4: Packaging hello.jar...
[INFO] BUILD SUCCESS
--> Step 4/4: Verifying executable target/hello.jar...
--> Testing execution: java -jar target/hello.jar
==================================================
Hello, World! From Variant 5 (Java / Maven)
Student: Душинський Даніїл, Group: КІ-406
==================================================
Verification calculation: 2 + 3 = 5
Status: BasicAddition logic verified successfully!
==========================================================
 [SUCCESS] All build steps and tests completed successfully!
==========================================================
```

---

## 10. Висновок
Під час виконання лабораторної роботи № 1:
1. Було повністю спроєктовано та реалізовано спеціалізованого AI-агента `build-engineer`, структурованого за принципом маніфесту, навичок (skills) та команд (commands).
2. Реалізовано оркестратор `init`, що забезпечує автоматизоване детерміноване розгортання проєкту від ініціалізації Git до фінальної верифікації якості.
3. Створено кросплатформний проєкт на мові Java 17 з використанням Apache Maven та модульних тестів JUnit 5 (варіант 5).
4. Розроблено кросплатформний CI/CD пайплайн для GitHub Actions із матрицею для трьох операційних систем (Ubuntu, Windows, macOS), що делегує виконання скриптам `ci.sh` та `ci.bat`.
5. Забезпечено надійний захист репозиторію від потрапляння артефактів збірки, логів та конфіденційних даних за допомогою `.gitignore`.
