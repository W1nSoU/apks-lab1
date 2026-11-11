@echo off
setlocal enabledelayedexpansion
chcp 65001 >nul 2>&1

echo ==========================================================
echo  [CI Build Script - Windows]
echo  Project: Hello World Java (Variant 5)
echo  Student: Душинський Даніїл (КІ-406)
echo ==========================================================

echo [CI Windows] Starting build and test process...

rem 1. Check for Maven
where mvn.cmd >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set "MVN_CMD=mvn.cmd"
) else (
    where mvn >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        set "MVN_CMD=mvn"
    ) else (
        if exist "mvnw.cmd" (
            set "MVN_CMD=mvnw.cmd"
        ) else (
            echo ERROR: Maven not found in PATH.
            exit /b 1
        )
    )
)

echo [CI Windows] Using Maven command: %MVN_CMD%

rem 2. Cleaning and compiling
echo [CI Windows] Step 1/4: Cleaning and compiling...
call %MVN_CMD% clean compile
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Compile failed!
    exit /b %ERRORLEVEL%
)

rem 3. Running unit tests
echo [CI Windows] Step 2/4: Running JUnit 5 tests...
call %MVN_CMD% test
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Tests failed!
    exit /b %ERRORLEVEL%
)

rem 4. Packaging JAR
echo [CI Windows] Step 3/4: Packaging hello.jar...
call %MVN_CMD% package -DskipTests=true
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Package failed!
    exit /b %ERRORLEVEL%
)

rem 5. Verifying executable
echo [CI Windows] Step 4/4: Verifying execution of target\hello.jar...
if not exist "target\hello.jar" (
    echo ERROR: target\hello.jar not found!
    exit /b 1
)

java -jar target\hello.jar
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Execution failed!
    exit /b %ERRORLEVEL%
)

echo ==========================================================
echo  [SUCCESS] All Windows CI build steps completed successfully!
echo ==========================================================
exit /b 0
