---
name: init
description: "Головна оркестратор-команда повного циклу розгортання та перевірки проєкту."
---

# Command: init (Orchestrator)

When the user runs `/init`, act as the **Build Engineer** AI agent defined in `.github/agents/build-engineer.agent.md` and execute the full orchestration workflow:

1. **Step 1 (git-init):** Verify that the project repository is initialized, on `develop` or `feature/` branch, and that `.gitignore` correctly ignores `target/`, `.idea/`, and temporary build artifacts.
2. **Step 2 (create-project):** Check and scaffold `src/main/java/com/example/App.java` and `README.md`.
3. **Step 3 (create-build):** Verify `pom.xml` configured for Java 17 LTS, JUnit 5 test in `src/test/java/com/example/BasicAdditionTest.java`, and executable scripts `ci.sh` / `ci.bat`.
4. **Step 4 (create-actions):** Verify `.github/workflows/ci.yml` matrix workflow for Ubuntu, Windows, and macOS.
5. **Step 5 (check & validate):** Run the build and test validation via `./ci.sh` (or `mvn clean compile test package` / `python3 agent.py check`).
6. **Report outcome:** Output a summary table of all verified components and declare:
   `✅ [INIT ORCHESTRATION SUCCESS] Всі компоненти проєкту згенеровано, протестовано та верифіковано!`
