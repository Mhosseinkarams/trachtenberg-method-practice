import os
import sys

# Add parent directory to path to import math_logic
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.math_logic import rules

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print("===============================")
        print("      FAST MATH TRAINER        ")
        print("===============================")
        print("Select a method to practice:")

        for i, rule in enumerate(rules):
            print(f"{i + 1}. {rule.name} ({rule.method})")
        print("0. Exit")

        try:
            choice = int(input("\nChoice: "))
        except ValueError:
            continue

        if choice == 0:
            break
        if choice < 1 or choice > len(rules):
            continue

        rule = rules[choice - 1]
        score = 0
        total = 0

        while True:
            clear_screen()
            print(f"Method: {rule.name}")
            print(f"Theory: {rule.explanation}")
            print(f"Score: {score}/{total}")
            print("-------------------------------")

            p = rule.generate_problem()
            print(f"\n  {p['question']} = ? ")

            user_input = input("\nYour answer (or 'q' to go back): ")

            if user_input.lower() == 'q':
                break

            try:
                user_answer = int(user_input)
            except ValueError:
                continue

            total += 1
            if user_answer == p['answer']:
                print("\nCorrect!")
                score += 1
            else:
                print(f"\nWrong. The answer was {p['answer']}")

            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
