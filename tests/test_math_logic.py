import sys
import os

# Add the project root to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.math_logic import rules

def test_all_rules():
    print(f"Testing {len(rules)} math rules...")
    for rule in rules:
        print(f"  Testing: {rule.name} ({rule.id})... ", end="")
        try:
            # Generate 10 problems per rule
            for _ in range(10):
                problem = rule.generate_problem()
                assert 'question' in problem
                assert 'answer' in problem

                # Basic sanity check: answer should be an integer
                assert isinstance(problem['answer'], int)

                # Rule specific validation (optional, but good for regression)
                if rule.id == 'tracht-11':
                    num = int(problem['question'].split('x ')[1])
                    assert problem['answer'] == 11 * num
                elif rule.id == 'tracht-12':
                    num = int(problem['question'].split('x ')[1])
                    assert problem['answer'] == 12 * num
                elif rule.id == 'tracht-5':
                    num = int(problem['question'].split('x ')[1])
                    assert problem['answer'] == 5 * num
                elif rule.id == 'tracht-6':
                    num = int(problem['question'].split('x ')[1])
                    assert problem['answer'] == 6 * num
                elif rule.id == 'tracht-7':
                    num = int(problem['question'].split('x ')[1])
                    assert problem['answer'] == 7 * num
                elif rule.id == 'tracht-8':
                    num = int(problem['question'].split('x ')[1])
                    assert problem['answer'] == 8 * num
                elif rule.id == 'tracht-9':
                    num = int(problem['question'].split('x ')[1])
                    assert problem['answer'] == 9 * num
                elif rule.id == 'vedic-square-5':
                    num = int(problem['question'].replace('²', ''))
                    assert problem['answer'] == num * num
                elif rule.id == 'vedic-base-10':
                    parts = problem['question'].split(' x ')
                    assert problem['answer'] == int(parts[0]) * int(parts[1])
                elif rule.id == 'vedic-base-100':
                    parts = problem['question'].split(' x ')
                    assert problem['answer'] == int(parts[0]) * int(parts[1])
                elif rule.id == 'vedic-base-1000':
                    parts = problem['question'].split(' x ')
                    assert problem['answer'] == int(parts[0]) * int(parts[1])
                elif rule.id == 'vedic-squaring-general':
                    num = int(problem['question'].replace('²', ''))
                    assert problem['answer'] == num * num
                elif rule.id == 'vedic-sqrt-perfect':
                    num = int(problem['question'].replace('√', ''))
                    assert problem['answer'] * problem['answer'] == num
                elif rule.id == 'tracht-addition':
                    parts = problem['question'].split(' + ')
                    assert problem['answer'] == int(parts[0]) + int(parts[1])
                elif rule.id == 'vedic-complementary-addition':
                    parts = problem['question'].split(' + ')
                    assert problem['answer'] == int(parts[0]) + int(parts[1])
                elif rule.id == 'tracht-4':
                    num = int(problem['question'].split('x ')[1])
                    assert problem['answer'] == 4 * num
                elif rule.id == 'tracht-3':
                    num = int(problem['question'].split('x ')[1])
                    assert problem['answer'] == 3 * num
                elif rule.id == 'vedic-subtraction-base':
                    parts = problem['question'].split(' - ')
                    assert problem['answer'] == int(parts[0]) - int(parts[1])
                elif rule.id == 'vedic-vertically-crosswise':
                    parts = problem['question'].split(' x ')
                    assert problem['answer'] == int(parts[0]) * int(parts[1])
                elif rule.id == 'vedic-square-near-base':
                    num = int(problem['question'].replace('²', ''))
                    assert problem['answer'] == num * num
                elif rule.id == 'tracht-13':
                    num = int(problem['question'].split('x ')[1])
                    assert problem['answer'] == 13 * num
                elif rule.id == 'tracht-general':
                    parts = problem['question'].split(' x ')
                    assert problem['answer'] == int(parts[0]) * int(parts[1])
                elif rule.id == 'tracht-division':
                    parts = problem['question'].split(' ÷ ')
                    assert problem['answer'] == int(parts[0]) // int(parts[1])
                elif rule.id == 'tracht-sqrt':
                    num = int(problem['question'].replace('√', ''))
                    assert problem['answer'] * problem['answer'] == num
                elif rule.id == 'vedic-div-9':
                    parts = problem['question'].split(' ÷ ')
                    assert problem['answer'] == int(parts[0]) // int(parts[1])
                elif rule.id == 'vedic-series-9':
                    parts = problem['question'].split(' x ')
                    assert problem['answer'] == int(parts[0]) * int(parts[1])
                elif rule.id == 'vedic-ekadhikena':
                    parts = problem['question'].split(' x ')
                    assert problem['answer'] == int(parts[0]) * int(parts[1])
                elif rule.id == 'vedic-cubing':
                    num = int(problem['question'].replace('³', ''))
                    assert problem['answer'] == num ** 3

            print("PASSED")
        except Exception as e:
            print(f"FAILED: {e}")
            sys.exit(1)

if __name__ == "__main__":
    test_all_rules()
