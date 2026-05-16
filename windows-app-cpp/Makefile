CXX = x86_64-w64-mingw32-g++
CXXFLAGS = -Wall -O2

FastMathTrainer.exe: main.o math_rules.o
	$(CXX) $(CXXFLAGS) -o FastMathTrainer.exe main.o math_rules.o -static

main.o: main.cpp math_rules.h
	$(CXX) $(CXXFLAGS) -c main.cpp

math_rules.o: math_rules.cpp math_rules.h
	$(CXX) $(CXXFLAGS) -c math_rules.cpp

clean:
	rm -f *.o FastMathTrainer.exe
