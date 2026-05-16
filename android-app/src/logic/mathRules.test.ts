import { expect, test, describe } from 'vitest';
import { rules } from './mathRules';

describe('Math Rules Problem Generation', () => {
  rules.forEach(rule => {
    test(`Rule ${rule.name} generates valid problems`, () => {
      for (let i = 0; i < 50; i++) {
        const { question, answer } = rule.generateProblem();
        expect(question).toBeDefined();
        expect(typeof answer).toBe('number');

        // Basic validation that the answer matches the question format
        if (rule.id === 'tracht-11') {
           const num = parseInt(question.split('x ')[1]);
           expect(answer).toBe(11 * num);
        }
        else if (rule.id === 'tracht-12') {
           const num = parseInt(question.split('x ')[1]);
           expect(answer).toBe(12 * num);
        }
        else if (rule.id === 'tracht-5') {
           const num = parseInt(question.split('x ')[1]);
           expect(answer).toBe(5 * num);
        }
        else if (rule.id === 'vedic-square-5') {
           const num = parseInt(question.split('^')[0]);
           expect(answer).toBe(num * num);
           expect(num % 10).toBe(5);
        }
        else if (rule.id === 'vedic-base-10') {
           const parts = question.split(' x ');
           const a = parseInt(parts[0]);
           const b = parseInt(parts[1]);
           expect(answer).toBe(a * b);
        }
        else if (rule.id === 'vedic-squaring-general') {
           const num = parseInt(question.split('^')[0]);
           expect(answer).toBe(num * num);
        }
        else if (rule.id === 'vedic-sqrt-perfect') {
           const num = parseInt(question.substring(1));
           expect(answer * answer).toBe(num);
        }
        else if (rule.id === 'tracht-addition') {
           const parts = question.split(' + ');
           const a = parseInt(parts[0]);
           const b = parseInt(parts[1]);
           expect(answer).toBe(a + b);
        }
        else if (rule.id === 'vedic-complementary-addition') {
           const parts = question.split(' + ');
           const a = parseInt(parts[0]);
           const b = parseInt(parts[1]);
           expect(answer).toBe(a + b);
        }
      }
    });
  });
});
