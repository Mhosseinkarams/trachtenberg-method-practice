import React from 'react';
import type { Rule } from '../logic/mathRules';

interface TheorySectionProps {
  rule: Rule;
}

const TheorySection: React.FC<TheorySectionProps> = ({ rule }) => {
  return (
    <div className="bg-indigo-50 p-6 rounded-xl border border-indigo-100 h-full">
      <h2 className="text-2xl font-bold text-indigo-900 mb-4">How it works</h2>

      <div className="prose prose-indigo max-w-none">
        <h3 className="text-xl font-semibold text-indigo-800">{rule.name}</h3>
        <p className="text-indigo-900 mt-2">{rule.explanation}</p>

        <div className="mt-6 bg-white p-4 rounded-lg border border-indigo-200">
          <h4 className="font-bold text-indigo-800 mb-2">Example:</h4>
          <code className="text-lg text-indigo-600 block">{rule.example}</code>
        </div>

        <div className="mt-8">
          <h4 className="font-bold text-indigo-800 mb-2">Key points:</h4>
          <ul className="list-disc list-inside text-indigo-900 space-y-1">
            {rule.method === 'Trachtenberg' && (
              <>
                <li>Focus on the "neighbor" of each digit.</li>
                <li>Work from right to left.</li>
                <li>Mental addition is key.</li>
              </>
            )}
            {rule.method === 'Vedic' && (
              <>
                <li>Look for patterns near base numbers (10, 100).</li>
                <li>Use "vertical and crosswise" thinking.</li>
                <li>Simpler formulas for specific cases.</li>
              </>
            )}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default TheorySection;
