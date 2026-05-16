#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include "math_rules.h"

void clearScreen() {
#ifdef _WIN32
    system("cls");
#else
    system("clear");
#endif
}

int main() {
    srand(time(NULL));

    while (true) {
        clearScreen();
        std::cout << "===============================" << std::endl;
        std::cout << "      FAST MATH TRAINER        " << std::endl;
        std::cout << "===============================" << std::endl;
        std::cout << "Select a method to practice:" << std::endl;

        for (size_t i = 0; i < rules.size(); ++i) {
            std::cout << i + 1 << ". " << rules[i].name << " (" << rules[i].method << ")" << std::endl;
        }
        std::cout << "0. Exit" << std::endl;
        std::cout << "\nChoice: ";

        int choice;
        std::cin >> choice;

        if (choice == 0) break;
        if (choice < 1 || choice > (int)rules.size()) continue;

        const Rule& rule = rules[choice - 1];
        int score = 0;
        int total = 0;

        while (true) {
            clearScreen();
            std::cout << "Method: " << rule.name << std::endl;
            std::cout << "Theory: " << rule.explanation << std::endl;
            std::cout << "Score: " << score << "/" << total << std::endl;
            std::cout << "-------------------------------" << std::endl;

            Problem p = rule.generateProblem();
            std::cout << "\n  " << p.question << " = ? " << std::endl;
            std::cout << "\nYour answer (or -1 to go back): ";

            int userAnswer;
            std::cin >> userAnswer;

            if (userAnswer == -1) break;

            total++;
            if (userAnswer == p.answer) {
                std::cout << "\nCorrect!" << std::endl;
                score++;
            } else {
                std::cout << "\nWrong. The answer was " << p.answer << std::endl;
            }

            std::cout << "\nPress Enter to continue...";
            std::cin.ignore();
            std::cin.get();
        }
    }

    return 0;
}
