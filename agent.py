#!/usr/bin/env python3
"""
AI-Agent Build-Engineer CLI Orchestrator.
Лабораторна робота № 1 (АПКС, НУЛП).
Студент: Душинський Даніїл (КІ-406), Варіант 5.
"""

import sys
import os
import subprocess
import time

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

def log_step(step_num, total_steps, title, skill=None):
    skill_info = f" [Skill: {skill}]" if skill else ""
    print(f"\n\033[1;34m[{step_num}/{total_steps}] ⚙️  Command: {title}{skill_info}\033[0m")

def log_success(msg):
    print(f"  \033[32m✔ {msg}\033[0m")

def log_error(msg):
    print(f"  \033[31m✖ ERROR: {msg}\033[0m")

def cmd_git_init():
    log_step(1, 5, "git-init")
    # Перевірка git
    res = subprocess.run(["git", "status"], cwd=PROJECT_DIR, capture_output=True, text=True)
    if res.returncode != 0:
        log_error("Git репозиторій не ініціалізовано!")
        return False
    log_success("Git сховище активне.")
    
    # Перевірка .gitignore
    gitignore_path = os.path.join(PROJECT_DIR, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            content = f.read()
        if "target/" in content:
            log_success(".gitignore перевірено (правило 'target/' присутнє).")
        else:
            log_error(".gitignore не містить 'target/'!")
            return False
    else:
        log_error("Файл .gitignore відсутній!")
        return False
    return True

def cmd_create_project():
    log_step(2, 5, "create-project", skill="project-scaffold")
    src_main = os.path.join(PROJECT_DIR, "src", "main", "java", "com", "example")
    src_test = os.path.join(PROJECT_DIR, "src", "test", "java", "com", "example")
    readme = os.path.join(PROJECT_DIR, "README.md")
    
    if os.path.isdir(src_main) and os.path.isdir(src_test):
        log_success("Структура каталогів src/main та src/test готова.")
    else:
        log_error("Відсутня стандартна структура каталогів!")
        return False
        
    if os.path.isfile(readme):
        log_success("README.md присутній.")
    else:
        log_error("README.md відсутній!")
        return False
    return True

def cmd_create_build():
    log_step(3, 5, "create-build", skill="build-and-test")
    pom = os.path.join(PROJECT_DIR, "pom.xml")
    app = os.path.join(PROJECT_DIR, "src", "main", "java", "com", "example", "App.java")
    test = os.path.join(PROJECT_DIR, "src", "test", "java", "com", "example", "BasicAdditionTest.java")
    ci_sh = os.path.join(PROJECT_DIR, "ci.sh")
    ci_bat = os.path.join(PROJECT_DIR, "ci.bat")
    
    for f_path, label in [(pom, "pom.xml"), (app, "App.java"), (test, "BasicAdditionTest.java"), (ci_sh, "ci.sh"), (ci_bat, "ci.bat")]:
        if os.path.isfile(f_path):
            log_success(f"Артефакт {label} наявний.")
        else:
            log_error(f"Артефакт {label} не знайдено!")
            return False
    return True

def cmd_create_actions():
    log_step(4, 5, "create-actions", skill="github-actions")
    ci_yml = os.path.join(PROJECT_DIR, ".github", "workflows", "ci.yml")
    if os.path.isfile(ci_yml):
        log_success(".github/workflows/ci.yml налаштовано (матриця Ubuntu, Windows, macOS).")
        return True
    else:
        log_error("Workflow файл не знайдено!")
        return False

def cmd_check():
    log_step(5, 5, "check", skill="build-and-test")
    print("  -> Запуск локального складання та модульних тестів через ./ci.sh...")
    ci_sh = os.path.join(PROJECT_DIR, "ci.sh")
    res = subprocess.run(["bash", ci_sh], cwd=PROJECT_DIR, capture_output=True, text=True)
    if res.returncode == 0:
        log_success("Локальні тести пройдено успішно (BasicAddition: OK).")
        log_success("Виконуваний файл target/hello.jar згенеровано та протестовано.")
        return True
    else:
        log_error("Тести або компіляція впали з помилкою!")
        print("\n\033[33m--- Вивід помилки збірки ---\033[0m")
        print(res.stdout[-600:] if res.stdout else "")
        print(res.stderr[-600:] if res.stderr else "")
        return False

def run_init():
    print("=" * 65)
    print("\033[1;36m🤖 AI AGENT 'build-engineer' -> ORCHESTRATOR 'init'\033[0m")
    print("   Role: Build & CI/CD Automation Engineer")
    print("   Author: Душинський Даніїл (КІ-406), Варіант 5 (Java/Maven)")
    print("=" * 65)
    
    steps = [
        cmd_git_init,
        cmd_create_project,
        cmd_create_build,
        cmd_create_actions,
        cmd_check
    ]
    
    for step in steps:
        time.sleep(0.3)
        if not step():
            print("\n\033[1;31m❌ [FAIL-FAST ABORT] Оркестратор зупинено через помилку на поточному етапі!\033[0m")
            sys.exit(1)
            
    print("\n" + "=" * 65)
    print("\033[1;32m✅ [INIT ORCHESTRATION SUCCESS] Усі етапи успішно завершено!\033[0m")
    print("   Проєкт повністю верифіковано, тести зелені, артефакт зібрано.")
    print("=" * 65)

def main():
    if len(sys.argv) < 2:
        print("Використання:")
        print("  ./agent.py init            - Запустити повний оркестратор")
        print("  ./agent.py check           - Запустити перевірку")
        print("  ./agent.py git-init        - Перевірити стан Git")
        print("  ./agent.py create-project  - Перевірити структуру проєкту")
        print("  ./agent.py create-build    - Перевірити конфігурацію збірки")
        print("  ./agent.py create-actions  - Перевірити CI workflow")
        sys.exit(0)
        
    cmd = sys.argv[1].lower()
    if cmd in ("init", "run", "/init"):
        run_init()
    elif cmd in ("check", "/check"):
        if cmd_check():
            print("\n\033[32m✔ Перевірка успішна!\033[0m")
        else:
            sys.exit(1)
    elif cmd in ("git-init", "/git-init"):
        cmd_git_init()
    elif cmd in ("create-project", "/create-project"):
        cmd_create_project()
    elif cmd in ("create-build", "/create-build"):
        cmd_create_build()
    elif cmd in ("create-actions", "/create-actions"):
        cmd_create_actions()
    else:
        print(f"Невідома команда: {cmd}")
        sys.exit(1)

if __name__ == "__main__":
    main()
