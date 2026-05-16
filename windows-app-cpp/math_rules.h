#ifndef MATH_RULES_H
#define MATH_RULES_H

#include <string>
#include <vector>
#include <functional>

struct Problem {
    std::string question;
    int answer;
};

struct Rule {
    std::string id;
    std::string name;
    std::string method;
    std::string description;
    std::string explanation;
    std::string example;
    std::function<Problem()> generateProblem;
};

extern std::vector<Rule> rules;

#endif
