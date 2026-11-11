---
name: github-actions
description: "Генерація кросплатформного CI workflow (.github/workflows/ci.yml) для Windows, Linux та macOS."
version: 1.0.0
---

# Skill: github-actions

## 1. Призначення
Генерація автоматизованого CI/CD пайплайну для GitHub Actions, що перевіряє працездатність Java/Maven проєкту на трьох основних операційних системах: Ubuntu Linux, Microsoft Windows та Apple macOS.
Згідно з вимогами лабораторної роботи, кроки компіляції, тестування та пакування делегуються виключно скриптам `ci.sh` та `ci.bat`.

## 2. Вхідні параметри
- `trigger_branches`: `master`, `develop`.
- `matrix_os`: `[ubuntu-latest, windows-latest, macos-latest]`.
- `jdk_version`: `17`.
- `jdk_distribution`: `temurin`.

## 3. Створювані артефакти
- `.github/workflows/ci.yml`: опис робочого процесу GitHub Actions.

## 4. Структура workflow
- **Тригери:** події `push` та `pull_request` у гілки `develop` та `master`.
- **Матриця збірки:**
  - `ubuntu-latest`
  - `windows-latest`
  - `macos-latest`
- **Кроки (Steps):**
  1. `actions/checkout@v4`: отримання коду репозиторію.
  2. `actions/setup-java@v4`: налаштування JDK 17 (Temurin).
  3. Запуск скрипта збірки:
     - Для Linux/macOS: `run: bash ./ci.sh`
     - Для Windows: `run: .\ci.bat`
  4. `actions/upload-artifact@v4`: збереження згенерованого `hello.jar` як артефакту складання.

## 5. Критерії перевірки (Verification)
1. Файл `.github/workflows/ci.yml` містить коректний синтаксис YAML.
2. Вказано матрицю з трьох операційних систем.
3. Відсутні жорстко прописані виклики `mvn` безпосередньо у workflow - запуск виконується через `ci.sh` та `ci.bat`.
4. Відсутні збережені секрети чи приватні токени.

## 6. Типові сценарії помилок та їх вирішення
- **Помилка: На Linux/macOS скрипт `ci.sh` падає з `Permission denied`.**
  - *Дія агента:* Встановити права виконання через Git (`git update-index --chmod=+x ci.sh`) або запускати через `bash ./ci.sh`.
- **Помилка: Несумісність закінчень рядків (CRLF vs LF) на Windows.**
  - *Дія агента:* Налаштувати `.gitattributes` або запускати bash-інтерпретатор коректно.
