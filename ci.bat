@echo off
rem ==========================================================
rem  [CI Build Script - Windows]
rem  Project: Hello World Java (Variant 5)
rem  Student: Душинський Даніїл (КІ-406)
rem ==========================================================

echo [CI Windows] Starting build and test process...

rem 1. Перевірка наявності Maven
where mvn >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    if exist "mvnw.cmd" (
        set "MVN_CMD=mvnw.cmd"
    ) else (
        echo ERROR: Maven (mvn) не знайдено в PATH.
        exit /b 1
    )
) else (
    set "MVN_CMD=mvn"
)

echo [CI Windows] Using Maven command: %MVN_CMD%

rem 2. Очищення та компіляція
echo [CI Windows] Step 1/4: Cleaning and compiling...
call %MVN_CMD% clean compile
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Помилка компіляції проєкту!
    exit /b %ERRORLEVEL%
)

rem 3. Запуск модульних тестів (JUnit 5)
echo [CI Windows] Step 2/4: Running JUnit 5 tests...
call %MVN_CMD% test
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Юніт-тести завершилися з помилкою!
    exit /b %ERRORLEVEL%
)

rem 4. Пакування виконуваного JAR
echo [CI Windows] Step 3/4: Packaging hello.jar...
call %MVN_CMD% package -DskipTests=true
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Помилка пакування JAR-архіву!
    exit /b %ERRORLEVEL%
)

rem 5. Верифікація виконуваного файлу
echo [CI Windows] Step 4/4: Verifying execution of target/hello.jar...
if not exist "target\hello.jar" (
    echo ERROR: target\hello.jar не знайдено!
    exit /b 1
)

java -jar target\hello.jar
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Помилка запуску hello.jar!
    exit /b %ERRORLEVEL%
)

echo ==========================================================
echo  [SUCCESS] All Windows CI build steps completed successfully!
echo ==========================================================
exit /b 0
