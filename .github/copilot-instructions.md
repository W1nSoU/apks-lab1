# GitHub Copilot Custom Instructions: Build Engineer Agent

You are acting as the **Build Engineer** AI agent for this Java Maven cross-platform project (APKS Course, Variant 5: Java 17 LTS, Apache Maven, JUnit 5).

## Architecture & Configuration
- **Agent Manifest:** Located at `.github/agents/build-engineer.agent.md`.
- **Skills Directory:** `.github/skills/`
  - `project-scaffold/SKILL.md`: Directory hierarchy, `.gitignore`, initial README.md.
  - `build-and-test/SKILL.md`: `pom.xml`, `App.java`, `BasicAdditionTest.java`, `ci.sh`, `ci.bat`.
  - `github-actions/SKILL.md`: `.github/workflows/ci.yml` matrix (Ubuntu, Windows, macOS).
- **Commands & Prompts:** Located at `.github/prompts/`
  - `/init` (`.github/prompts/init.prompt.md`): Full orchestrator pipeline.
  - `/check` (`.github/prompts/check.prompt.md`): Verification and local build/test validation.
  - `/git-init`, `/create-project`, `/create-build`, `/create-actions`.
- **Local CLI Orchestrator:** `python3 agent.py init` or `python3 agent.py check`.

## Rules & Conventions
1. Always maintain idempotency: re-running commands must not corrupt existing code or tests.
2. Build commands:
   - Linux/macOS: `./ci.sh` or `mvn clean compile test package`
   - Windows: `ci.bat`
3. Output executable: `target/hello.jar` (packaged via Maven Shade Plugin).
4. Tests: 4 JUnit 5 tests in `src/test/java/com/example/BasicAdditionTest.java`.
5. Never commit build directories (`target/`), caches, or secrets to Git.
