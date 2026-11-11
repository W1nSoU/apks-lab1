#!/usr/bin/env bash
set -euo pipefail

echo "=========================================================="
echo " [CI Build Script - Linux / macOS]"
echo " Project: Hello World Java (Variant 5)"
echo " Student: Душинський Даніїл (КІ-406)"
echo " Date: $(date)"
echo "=========================================================="

# 1. Визначення команди Maven (mvn, maven wrapper або системний шлях)
MVN_CMD="mvn"
if ! command -v mvn &> /dev/null; then
    if [ -f "$HOME/.maven/apache-maven-3.9.6/bin/mvn" ]; then
        MVN_CMD="$HOME/.maven/apache-maven-3.9.6/bin/mvn"
    elif [ -f "./mvnw" ]; then
        MVN_CMD="./mvnw"
    else
        echo "Error: Maven (mvn) не знайдено в PATH."
        exit 1
    fi
fi

echo "--> Using Maven command: $MVN_CMD"

# 2. Очищення та компіляція
echo "--> Step 1/4: Cleaning & Compiling..."
$MVN_CMD clean compile

# 3. Запуск модульних тестів (JUnit 5)
echo "--> Step 2/4: Running Unit Tests (BasicAddition)..."
$MVN_CMD test

# 4. Пакування виконуваного JAR
echo "--> Step 3/4: Packaging hello.jar..."
$MVN_CMD package -DskipTests=true

# 5. Верифікація виконуваного файлу
echo "--> Step 4/4: Verifying executable target/hello.jar..."
if [ ! -f "target/hello.jar" ]; then
    echo "ERROR: target/hello.jar не знайдено після збірки!"
    exit 1
fi

echo "--> Testing execution: java -jar target/hello.jar"
java -jar target/hello.jar

echo "=========================================================="
echo " [SUCCESS] All build steps and tests completed successfully!"
echo "=========================================================="
exit 0
