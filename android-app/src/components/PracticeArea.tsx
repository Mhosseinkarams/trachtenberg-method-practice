import React, { useState, useEffect, useRef } from 'react';
import type { Rule } from '../logic/mathRules';

interface PracticeAreaProps {
  rule: Rule;
}

const PracticeArea: React.FC<PracticeAreaProps> = ({ rule }) => {
  const [problem, setProblem] = useState(rule.generateProblem());
  const [userInput, setUserInput] = useState('');
  const [feedback, setFeedback] = useState<{ message: string; isCorrect: boolean } | null>(null);
  const [stats, setStats] = useState({ correct: 0, total: 0 });
  const inputRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    newProblem();
  }, [rule]);

  const newProblem = () => {
    setProblem(rule.generateProblem());
    setUserInput('');
    setFeedback(null);
    inputRef.current?.focus();
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const isCorrect = parseInt(userInput) === problem.answer;

    setFeedback({
      message: isCorrect ? 'Correct!' : `Wrong. The answer was ${problem.answer}`,
      isCorrect
    });

    setStats(prev => ({
      correct: prev.correct + (isCorrect ? 1 : 0),
      total: prev.total + 1
    }));

    if (isCorrect) {
      setTimeout(newProblem, 1000);
    }
  };

  return (
    <div className="bg-white p-8 rounded-xl shadow-lg border border-gray-100 max-w-md mx-auto">
      <div className="flex justify-between mb-6 text-sm font-medium text-gray-500">
        <span>{rule.name}</span>
        <span>Score: {stats.correct}/{stats.total}</span>
      </div>

      <div className="text-center mb-8">
        <div className="text-4xl font-bold text-gray-800 mb-2">
          {problem.question}
        </div>
        <div className="text-gray-400 text-lg">= ?</div>
      </div>

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          ref={inputRef}
          type="number"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          className="w-full text-2xl p-3 border-2 border-indigo-200 rounded-lg focus:border-indigo-500 focus:outline-none text-center"
          placeholder="Enter answer"
          autoFocus
        />
        <button
          type="submit"
          className="w-full bg-indigo-600 text-white py-3 rounded-lg font-bold hover:bg-indigo-700 transition-colors"
        >
          Check Answer
        </button>
      </form>

      {feedback && (
        <div className={`mt-6 p-3 rounded-lg text-center font-medium ${
          feedback.isCorrect ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700'
        }`}>
          {feedback.message}
          {!feedback.isCorrect && (
            <button
              onClick={newProblem}
              className="block w-full mt-2 text-sm underline"
            >
              Try another one
            </button>
          )}
        </div>
      )}
    </div>
  );
};

export default PracticeArea;
