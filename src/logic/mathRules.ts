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
  }
];
