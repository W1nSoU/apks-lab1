package com.example;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Юніт-тести для перевірки базової логіки додавання (BasicAddition).
 * Реалізовано за допомогою JUnit 5 (Jupiter).
 */
public class BasicAdditionTest {

    @Test
    @DisplayName("BasicAddition: Тест додавання двох додатних чисел (2 + 3 == 5)")
    public void testPositiveAddition() {
        int result = App.add(2, 3);
        assertEquals(5, result, "2 + 3 повинно дорівнювати 5");
    }

    @Test
    @DisplayName("BasicAddition: Тест додавання з нулем (10 + 0 == 10)")
    public void testAdditionWithZero() {
        int result = App.add(10, 0);
        assertEquals(10, result, "10 + 0 повинно дорівнювати 10");
    }

    @Test
    @DisplayName("BasicAddition: Тест додавання від'ємних чисел (-4 + -6 == -10)")
    public void testNegativeAddition() {
        int result = App.add(-4, -6);
        assertEquals(-10, result, "-4 + -6 повинно дорівнювати -10");
    }

    @Test
    @DisplayName("BasicAddition: Тест додавання додатного та від'ємного числа (7 + -3 == 4)")
    public void testMixedAddition() {
        int result = App.add(7, -3);
        assertEquals(4, result, "7 + -3 повинно дорівнювати 4");
    }
}
