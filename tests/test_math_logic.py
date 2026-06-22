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

                # Assert that it's not the placeholder
                placeholder_en = "Apply the rule mentioned in the explanation above"
                placeholder_fa = "قوانین ذکر شده در بخش تئوری بالا را برای حل مرحله‌به‌مرحله این مسئله به کار ببرید"

                for s in steps_en:
                    assert placeholder_en not in s, f"Placeholder found in English steps for {rule.id}"
                for s in steps_fa:
                    assert placeholder_fa not in s, f"Placeholder found in Persian steps for {rule.id}"
            print("PASSED")
        except Exception as e:
            print(f"FAILED: {e}")
            sys.exit(1)

def test_steps_accuracy():
    print("Testing steps accuracy...")
    import re
    for rule in rules:
        for _ in range(5):
            problem = rule.generate_problem()
            steps = rule.get_steps(problem, 'en')
            if not steps: continue

            # Look for "Result: [num]" or "Result: [num] R [num]"
            last_step = steps[-1]
            if "Result:" in last_step:
                # Handle cases like "Result: 5 R 2" vs "Result: 123"
                match = re.search(r"Result: (\d+)(?: R (\d+))?", last_step)
                if match:
                    q = int(match.group(1))
                    if match.group(2) is not None:
                        # Special case for division with remainder
                        expected_q = problem['num'] // 9 if rule.id == 'vedic-div-9' else problem['answer']
                        expected_r = problem['num'] % 9
                        assert q == expected_q, f"Quotient mismatch in {rule.id}: Got {q}, expected {expected_q}. Step: {last_step}"
                        r = int(match.group(2))
                        assert r == expected_r, f"Remainder mismatch in {rule.id}: Got {r}, expected {expected_r}. Step: {last_step}"
                    else:
                        assert q == problem['answer'], f"Answer mismatch in {rule.id}: Got {q}, expected {problem['answer']}. Step: {last_step}"

if __name__ == "__main__":
    test_all_rules()
