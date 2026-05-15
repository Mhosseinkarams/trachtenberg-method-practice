import React from 'react';
import type { Rule } from '../logic/mathRules';

interface MethodCardProps {
  rule: Rule;
  onSelect: (rule: Rule) => void;
  isSelected: boolean;
}

const MethodCard: React.FC<MethodCardProps> = ({ rule, onSelect, isSelected }) => {
  return (
    <div
      className={`p-4 border rounded-lg cursor-pointer transition-all ${
        isSelected ? 'border-indigo-600 bg-indigo-50 shadow-md' : 'border-gray-200 hover:border-indigo-300'
      }`}
      onClick={() => onSelect(rule)}
    >
      <h3 className="font-bold text-lg">{rule.name}</h3>
      <p className="text-sm text-gray-600">{rule.method}</p>
      <p className="mt-2 text-sm">{rule.description}</p>
    </div>
  );
};

export default MethodCard;
