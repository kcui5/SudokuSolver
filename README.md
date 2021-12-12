# SudokuSolver
Sudoku Solver

An algorithm I wrote to solve sudoku boards while also practicing my Python skills.
Some aspects are purposely less efficient so that I can practice my Python. For example, there are classes created for each set of functionality to practice creating classes, empty lists as board entry placeholders to practice error handling, and others.

This project was split in two parts.
In the first part, I attempted to solve only easy Sudokus which do not require the guessing of certain entries. This was implemented with the solveBoardOnce() function of the Solver class.
In the second part, I proceeded to difficult Sudokus which require guessing of entries and backtracing of those guesses. This was implemented with the guessSolveBoard() function of the Solver class.