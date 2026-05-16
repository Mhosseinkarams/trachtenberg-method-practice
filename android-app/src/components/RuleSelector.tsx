import React from 'react';
import { rules } from '../logic/mathRules';
import type { Rule } from '../logic/mathRules';
import MethodCard from './MethodCard';

interface RuleSelectorProps {
  selectedRule: Rule | null;
  onRuleSelect: (rule: Rule) => void;
}

const RuleSelector: React.FC<RuleSelectorProps> = ({ selectedRule, onRuleSelect }) => {
  const trachtenbergRules = rules.filter(r => r.method === 'Trachtenberg');
  const vedicRules = rules.filter(r => r.method === 'Vedic');

  return (
    <div className="space-y-6">
      <section>
        <h2 className="text-xl font-semibold mb-4 text-gray-800 border-b pb-2">Trachtenberg System</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {trachtenbergRules.map(rule => (
            <MethodCard
              key={rule.id}
              rule={rule}
              onSelect={onRuleSelect}
              isSelected={selectedRule?.id === rule.id}
            />
          ))}
        </div>
      </section>

      <section>
        <h2 className="text-xl font-semibold mb-4 text-gray-800 border-b pb-2">Vedic Mathematics</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {vedicRules.map(rule => (
            <MethodCard
              key={rule.id}
              rule={rule}
              onSelect={onRuleSelect}
              isSelected={selectedRule?.id === rule.id}
            />
          ))}
        </div>
      </section>
    </div>
  );
};

export default RuleSelector;
