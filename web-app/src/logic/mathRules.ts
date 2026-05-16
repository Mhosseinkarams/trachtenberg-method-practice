export type Rule = {
  id: string;
  name: string;
  description: string;
  method: 'Trachtenberg' | 'Vedic';
  explanation: string;
  example: string;
  generateProblem: () => { question: string; answer: number };
};

export const rules: Rule[] = [
  {
    id: 'tracht-11',
    name: 'Multiplication by 11',
    method: 'Trachtenberg',
    description: 'Add the neighbor rule.',
    explanation: 'To multiply a number by 11: 1. The last digit of the number is the last digit of the answer. 2. Each successive digit of the number is added to its right-hand neighbor. 3. The first digit of the number becomes the first digit of the answer (plus any carry).',
    example: '11 x 432 = 4 (4+3) (3+2) 2 = 4752',
    generateProblem: () => {
      const num = Math.floor(Math.random() * 9000) + 100;
      return { question: `11 x ${num}`, answer: 11 * num };
    }
  },
  {
    id: 'tracht-12',
    name: 'Multiplication by 12',
    method: 'Trachtenberg',
    description: 'Double the digit and add the neighbor.',
    explanation: 'To multiply by 12: Double each digit in turn and add its neighbor.',
    example: '12 x 413 = (2*4+1) (2*1+3) (2*3) = 4956',
    generateProblem: () => {
      const num = Math.floor(Math.random() * 900) + 10;
      return { question: `12 x ${num}`, answer: 12 * num };
    }
  },
  {
    id: 'tracht-5',
    name: 'Multiplication by 5',
    method: 'Trachtenberg',
    description: 'Half the neighbor rule.',
    explanation: 'Use half the neighbor: if the digit is odd, add 5 to half the neighbor.',
    example: '5 x 426 = (half of 4) (half of 2) (half of 6) 0 = 2130',
    generateProblem: () => {
      const num = Math.floor(Math.random() * 9000) + 100;
      return { question: `5 x ${num}`, answer: 5 * num };
    }
  },
  {
    id: 'vedic-square-5',
    name: 'Squaring ending in 5',
    method: 'Vedic',
    description: 'By one more than the previous one.',
    explanation: 'To square a number ending in 5: Multiply the part before 5 by (itself + 1), then append 25.',
    example: '35^2 = (3 * 4) | 25 = 1225',
    generateProblem: () => {
      const base = Math.floor(Math.random() * 12) + 1;
      const num = base * 10 + 5;
      return { question: `${num}^2`, answer: num * num };
    }
  },
  {
    id: 'vedic-base-10',
    name: 'Multiplication near base 10',
    method: 'Vedic',
    description: 'All from 9 and the last from 10.',
    explanation: 'Multiply numbers close to 10. Find the deficiencies, multiply them for the right part, add crosswise for the left part.',
    example: '9 x 8: Deficiencies are 1 and 2. 1*2=2. 9-2=7 or 8-1=7. Answer 72.',
    generateProblem: () => {
      const a = Math.floor(Math.random() * 5) + 6; // 6-10
      const b = Math.floor(Math.random() * 5) + 6; // 6-10
      return { question: `${a} x ${b}`, answer: a * b };
    }
  },
  {
    id: 'vedic-squaring-general',
    name: 'General Squaring',
    method: 'Vedic',
    description: 'Duplex method.',
    explanation: 'To square any number: use the duplex (D). For a single digit a, D=a^2. For two digits ab, D=2ab.',
    example: '23^2 = D(2) | D(23) | D(3) = 4 | 12 | 9 = 529',
    generateProblem: () => {
      const num = Math.floor(Math.random() * 89) + 11; // 11-99
      return { question: `${num}^2`, answer: num * num };
    }
  },
  {
    id: 'vedic-sqrt-perfect',
    name: 'Square Root (Perfect)',
    method: 'Vedic',
    description: 'Observation method.',
    explanation: 'Look at the last digit to find the possible last digit of the root. Ignore last two digits and find the nearest square below the remaining number.',
    example: 'sqrt(1225): ends in 5, so root ends in 5. 12 is between 3^2 and 4^2. So tens digit is 3. Answer 35.',
    generateProblem: () => {
      const root = Math.floor(Math.random() * 90) + 10; // 10-99
      const num = root * root;
      return { question: `√${num}`, answer: root };
    }
  },
  {
    id: 'tracht-addition',
    name: 'Rapid Addition',
    method: 'Trachtenberg',
    description: 'The L-R column method.',
    explanation: 'Add columns from left to right, then adjust for carries.',
    example: '456 + 123 = (4+1) (5+2) (6+3) = 579',
    generateProblem: () => {
      const a = Math.floor(Math.random() * 900) + 100;
      const b = Math.floor(Math.random() * 900) + 100;
      return { question: `${a} + ${b}`, answer: a + b };
    }
  },
  {
    id: 'vedic-complementary-addition',
    name: 'Complementary Addition',
    method: 'Vedic',
    description: 'Completing the whole.',
    explanation: 'Look for numbers that add up to 10, 100, etc. to simplify addition.',
    example: '48 + 32 = 40 + 30 + (8 + 2) = 70 + 10 = 80',
    generateProblem: () => {
      const base = (Math.floor(Math.random() * 8) + 1) * 10;
      const diff = Math.floor(Math.random() * 9) + 1;
      const a = base + diff;
      const b = (10 - diff) + Math.floor(Math.random() * 5) * 10;
      return { question: `${a} + ${b}`, answer: a + b };
    }
  }
];
