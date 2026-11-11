# Лабораторна робота № 1: Проєктування AI-агента для автоматизації розробки та CI/CD

- **Студент:** Душинський Даніїл  
- **Група:** КІ-406  
- **Варіант:** 5  
- **Дисципліна:** Архітектура паралельних комп'ютерних систем (АПКС)  
- **Стек технологій:** Java 17 LTS, Apache Maven, JUnit 5, GitHub Actions CI/CD  

---

## 1. Короткий опис проєкту
Проєкт демонструє використання спеціалізованого AI-агента **`build-engineer`** з навичками (skills), командами (commands) та оркестрацією для генерації, складання, тестування і перевірки кросплатформного застосунку **Hello World** на мові Java.

Система забезпечує:
- Автономне розгортання структури коду та конфігурацій.
- Автоматизоване складання у виконуваний артефакт `target/hello.jar`.
- Запуск юніт-тестів `BasicAdditionTest` за допомогою JUnit 5.
- Кросплатформний запуск через уніфіковані скрипти `ci.sh` (Linux/macOS) та `ci.bat` (Windows).
- Повний CI матричний пайплайн у GitHub Actions для трьох ОС (`ubuntu-latest`, `windows-latest`, `macos-latest`).

---

## 2. Структура проєкту
```text
.
├── .github/
│   ├── agents/
│   │   └── build-engineer.agent.md       # Маніфест AI-агента
│   ├── skills/
│   │   ├── project-scaffold/SKILL.md     # Створення структури проєкту
│   │   ├── build-and-test/SKILL.md       # Конфігурація Maven, Java та тести
│   │   └── github-actions/SKILL.md       # Налаштування CI пайплайну
│   ├── prompts/
│   │   ├── git-init.prompt.md            # Команда ініціалізації Git
│   │   ├── create-project.prompt.md      # Команда генерації структури
│   │   ├── create-build.prompt.md        # Команда створення збірки
│   │   ├── create-actions.prompt.md      # Команда створення CI
│   │   ├── check.prompt.md               # Команда перевірки проєкту
│   │   └── init.prompt.md                # Оркестратор усіх дій
│   └── workflows/
│       └── ci.yml                        # GitHub Actions Matrix CI (Ubuntu, Windows, macOS)
├── src/
│   ├── main/java/com/example/App.java    # Застосунок Hello World
│   └── test/java/com/example/BasicAdditionTest.java # JUnit 5 тести
├── docs/
│   ├── architecture.md                   # Архітектура AI-агента
│   ├── usage.md                          # Повна інструкція із запуску
│   └── ai-log.md                         # Журнал взаємодії з AI та опис помилки
├── ci.sh                                 # Скрипт збірки для Linux/macOS
├── ci.bat                                # Скрипт збірки для Windows
├── pom.xml                               # Дескриптор складання Maven
├── README.md                             # Цей файл
└── .gitignore                            # Виключення артефактів збірки
```

---

## 3. Спосіб запуску AI-агента
В AI-середовищі викликається оркестратор-команда:
```text
/init
```
яка послідовно запускає ланцюжок дій:
`git-init` -> `create-project` -> `create-build` -> `create-actions` -> `check`.

Детальний опис команд та навичок доступний у файлі [docs/usage.md](docs/usage.md).

---

## 4. Локальний запуск та тестування вручну
- **Linux / macOS:**
  ```bash
  chmod +x ci.sh
  ./ci.sh
  ```
- **Windows:**
  ```cmd
  ci.bat
  ```
- **Запуск зібраного JAR-файлу:**
  ```bash
  java -jar target/hello.jar
  ```
