import { useState } from 'react'
import Header from './components/Header'
import Footer from './components/Footer'
import RuleSelector from './components/RuleSelector'
import PracticeArea from './components/PracticeArea'
import TheorySection from './components/TheorySection'
import type { Rule } from './logic/mathRules'

function App() {
  const [selectedRule, setSelectedRule] = useState<Rule | null>(null)

  return (
    <div className="min-h-screen flex flex-col bg-gray-50">
      <Header />

      <main className="flex-grow container mx-auto px-4 py-8">
        {!selectedRule ? (
          <div className="max-w-4xl mx-auto">
            <div className="text-center mb-12">
              <h2 className="text-4xl font-extrabold text-gray-900 mb-4">Master Rapid Calculation</h2>
              <p className="text-xl text-gray-600">Choose a method to start practicing mental math shortcuts.</p>
            </div>
            <RuleSelector selectedRule={selectedRule} onRuleSelect={setSelectedRule} />
          </div>
        ) : (
          <div className="max-w-6xl mx-auto">
            <button
              onClick={() => setSelectedRule(null)}
              className="mb-6 flex items-center text-indigo-600 hover:text-indigo-800 transition-colors"
            >
              <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 mr-1" viewBox="0 0 20 20" fill="currentColor">
                <path d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z" />
              </svg>
              Back to methods
            </button>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 items-start">
              <PracticeArea rule={selectedRule} />
              <TheorySection rule={selectedRule} />
            </div>
          </div>
        )}
      </main>

      <Footer />
    </div>
  )
}

export default App
