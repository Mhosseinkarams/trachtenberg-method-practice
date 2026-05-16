#include "math_rules.h"
#include <random>

std::vector<Rule> rules = {
    {
        "tracht-11", "Multiplication by 11", "Trachtenberg",
        "Add the neighbor rule.",
        "To multiply a number by 11: 1. Last digit is same. 2. Add each digit to its neighbor. 3. First digit stays (with carry).",
        "11 x 432 = 4752",
        []() {
            int num = rand() % 9000 + 100;
            return Problem{"11 x " + std::to_string(num), 11 * num};
        }
    },
    {
        "vedic-square-5", "Squaring ending in 5", "Vedic",
        "By one more than the previous one.",
        "Multiply the part before 5 by (itself + 1), then append 25.",
        "35^2 = 1225",
        []() {
            int base = rand() % 12 + 1;
            int num = base * 10 + 5;
            return Problem{std::to_string(num) + "^2", num * num};
        }
    },
    {
        "vedic-sqrt-perfect", "Square Root (Perfect)", "Vedic",
        "Observation method.",
        "Look at the last digit and nearest square below.",
        "sqrt(1225) = 35",
        []() {
            int root = rand() % 90 + 10;
            return Problem{"sqrt(" + std::to_string(root * root) + ")", root};
        }
    },
    {
        "tracht-addition", "Rapid Addition", "Trachtenberg",
        "The L-R column method.",
        "Add columns from left to right.",
        "456 + 123 = 579",
        []() {
            int a = rand() % 900 + 100;
            int b = rand() % 900 + 100;
            return Problem{std::to_string(a) + " + " + std::to_string(b), a + b};
        }
    }
};
