---
name: create-actions
description: "Команда генерації матричного GitHub Actions CI workflow."
---

# Command: create-actions

## Передумови
- Створено скрипти `ci.sh` та `ci.bat`.

## Дії агента
1. Викликати skill `github-actions`.
2. Створити `.github/workflows/ci.yml`:
   - Назва: `Cross-Platform CI (Ubuntu, Windows, macOS)`.
   - Тригери: `push` та `pull_request` для гілок `develop` та `master`.
   - Матриця операційних систем: `[ubuntu-latest, windows-latest, macos-latest]`.
   - Крок налаштування Java 17 Temurin.
   - Виклик виключно `bash ./ci.sh` на Linux/macOS та `ci.bat` на Windows.
   - Збереження артефакту `target/hello.jar`.

## Очікувані файли
- `.github/workflows/ci.yml`

## Команди перевірки
```bash
test -f .github/workflows/ci.yml && echo "OK: Workflow file exists"
```

## Повідомлення про помилку
- *Помилка:* "Workflow викликає mvn безпосередньо замість скриптів".
- *Рішення:* Переписати кроки у `ci.yml` на запуск `ci.sh` / `ci.bat`.
