# Інструкція користувача та запуск AI-агента

**Автор:** Душинський Даніїл (КІ-406)  
**Проєкт:** Hello World Java Application & Cross-Platform CI/CD  
**Варіант:** 5 (Java / Maven / JUnit 5)

---

## 1. Системні вимоги
- **Java SE Development Kit (JDK):** версія 17 або новіша (`java -version`).
- **Apache Maven:** версія 3.8+ (`mvn -version`) або наявний bash/cmd інтерпретатор.
- **Git:** встановлений та налаштований клієнт Git (`git --version`).
- **Операційна система:** macOS, Linux або Windows.

---

## 2. Запуск AI-агента

У середовищі, що підтримує агентські промпти (Antigravity, GitHub Copilot Workspace, Cursor тощо):

### 2.1. Повний автоматичний запуск (Оркестратор `init`)
Для запуску повного циклу розгортання проєкту від ініціалізації до перевірки виконайте:
```text
/init
```
або завантажте промпт `.github/prompts/init.prompt.md`.

### 2.2. Покроковий виклик окремих команд
Користувач може запускати окремі команди незалежно:
1. Ініціалізація Git та `.gitignore`:
   ```text
   /git-init
   ```
2. Створення структури папок та опису:
   ```text
   /create-project
   ```
3. Генерація `pom.xml`, коду, тестів та скриптів:
   ```text
   /create-build
   ```
4. Генерація GitHub Actions CI:
   ```text
   /create-actions
   ```
5. Запуск перевірки:
   ```text
   /check
   ```

---

## 3. Локальна перевірка та запуск проєкту вручну

### 3.1. Запуск через скрипти автоматизації (рекомендовано)
- **На macOS / Linux:**
  ```bash
  chmod +x ci.sh
  ./ci.sh
  ```
- **На Windows:**
  ```cmd
  ci.bat
  ```

Скрипт автоматично:
1. Запускає очищення та компіляцію (`mvn clean compile`).
2. Запускає юніт-тести JUnit 5 (`mvn test`).
3. Збирає автономний JAR-архів (`mvn package`).
4. Запускає зібраний застосунок для перевірки працездатності:
   ```bash
   java -jar target/hello.jar
   ```

### 3.2. Прямий запуск через Maven
- Запуск тестів:
  ```bash
  mvn test
  ```
- Збірка виконуваного файлу:
  ```bash
  mvn clean package
  ```
- Запуск згенерованого застосунку:
  ```bash
  java -jar target/hello.jar
  ```
  **Очікуваний вивід:**
  ```text
  Hello, World! From Variant 5 (Java/Maven)
  2 + 3 = 5
  Application executed successfully!
  ```
