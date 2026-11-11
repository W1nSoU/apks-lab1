package com.example;

/**
 * Головний клас застосунку Hello World.
 * Варіант 5 (Java / Maven / JUnit 5).
 * Автор: Душинський Даніїл (КІ-406).
 */
public class App {

    /**
     * Статичний метод для додавання двох цілих чисел.
     * Використовується для демонстрації модульного тестування (BasicAddition).
     */
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        System.out.println("==================================================");
        System.out.println("Hello, World! From Variant 5 (Java / Maven)");
        System.out.println("Student: Душинський Даніїл, Group: КІ-406");
        System.out.println("==================================================");

        int a = 2;
        int b = 3;
        int result = add(a, b);
        System.out.println("Verification calculation: " + a + " + " + b + " = " + result);

        if (result == 5) {
            System.out.println("Status: BasicAddition logic verified successfully!");
        } else {
            System.err.println("Status: Calculation error!");
            System.exit(1);
        }
    }
}
