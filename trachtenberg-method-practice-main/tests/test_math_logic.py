import sys
import os

# Add the project root to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.math_logic import rules

def test_all_rules():
    print(f"Testing {len(rules)} math rules...")
    for rule in rules:
        print(f"  Testing: {rule.id}... ", end="")
        try:
            # Generate 5 problems per rule
            for _ in range(5):
                problem = rule.generate_problem()
                assert 'question' in problem
                assert 'answer' in problem
                assert isinstance(problem['answer'], int)

                # Check steps
                steps_en = rule.get_steps(problem, 'en')
                steps_fa = rule.get_steps(problem, 'fa')
                assert isinstance(steps_en, list)
                assert isinstance(steps_fa, list)
            print("PASSED")
        except Exception as e:
            print(f"FAILED: {e}")
            sys.exit(1)

if __name__ == "__main__":
    test_all_rules()
