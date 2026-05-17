import os
import sys

# Add parent directory to path to import math_logic
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.math_logic import rules

# ANSI colors
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
BOLD = '\033[1m'
END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    while True:
        clear_screen()
        print(f"{BOLD}{BLUE}==============================={END}")
        print(f"{BOLD}{BLUE}      FAST MATH TRAINER        {END}")
        print(f"{BOLD}{BLUE}==============================={END}")
        print("Select a method to practice:\n")

        tracht_rules = [r for r in rules if r.method == "Trachtenberg"]
        vedic_rules = [r for r in rules if r.method == "Vedic"]

        all_display_rules = tracht_rules + vedic_rules

        print(f"{BOLD}--- Trachtenberg System ---{END}")
        for i, rule in enumerate(tracht_rules):
            print(f"{i + 1:2}. {rule.name}")

        print(f"\n{BOLD}--- Vedic Mathematics ---{END}")
        for i, rule in enumerate(vedic_rules):
            print(f"{len(tracht_rules) + i + 1:2}. {rule.name}")

        print(f"\n{BOLD} 0. Exit{END}")

        try:
            choice_str = input(f"\n{BOLD}Choice: {END}")
            if not choice_str: continue
            choice = int(choice_str)
        except ValueError:
            continue

        if choice == 0:
            break
        if choice < 1 or choice > len(all_display_rules):
            continue

        rule = all_display_rules[choice - 1]
        score = 0
        total = 0

        while True:
            p = rule.generate_problem()
            while True:
                clear_screen()
                print(f"{BOLD}Method: {BLUE}{rule.name}{END}")
                print(f"{BOLD}Theory: {END}{rule.description}")
                print(f"{BOLD}Score:  {GREEN}{score}{END}/{total}")
                print("-" * 31)

                print(f"\n  {BOLD}{p['question']} = ?{END} ")

                user_input = input(f"\nYour answer (or {BOLD}'h'{END} for hint, {BOLD}'q'{END} to quit): ").strip().lower()

                if user_input == 'q':
                    break

                if user_input == 'h':
                    print(f"\n{BOLD}Explanation:{END} {rule.explanation}")
                    print(f"{BOLD}Example:{END} {rule.example}")
                    input("\nPress Enter to return to problem...")
                    continue

                try:
                    user_answer = int(user_input)
                    break
                except ValueError:
                    continue

            if user_input == 'q':
                break

            total += 1
            if user_answer == p['answer']:
                print(f"\n{BOLD}{GREEN}Correct!{END}")
                score += 1
            else:
                print(f"\n{BOLD}{RED}Wrong.{END} The answer was {BOLD}{p['answer']}{END}")

            input("\nPress Enter to continue...")

if __name__ == "__main__":
    if os.name == 'nt':
        os.system('')
    main()
