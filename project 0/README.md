# Project 0. Guess the number

## Table of contents:
[1. Project description](https://github.com/lamewarden/sf_data_science-2022-/tree/main/project%200/README_project_0.md#Project-description)

[2. Task](https://github.com/lamewarden/sf_data_science-2022-/tree/main/project%200/README_project_0.md#Task)

[3. Data description](https://github.com/lamewarden/sf_data_science-2022-/tree/main/project%200/README_project_0.md#Data-description)

[4. Project steps](https://github.com/lamewarden/sf_data_science-2022-/tree/main/project%200/README_project_0.md#Project-steps)

[5. Results](https://github.com/lamewarden/sf_data_science-2022-/tree/main/project%200/README_project_0.md#Results)

[6. Conclusions](https://github.com/lamewarden/sf_data_science-2022-/tree/main/project%200/README_project_0.md#Conclusions)


## Project description
Guess the number with the least possible attempts 

## Task
Write a program for the efficient guessing

### Rules:
- A random number from 0 to 100 is taken, and we should compose a program that guesses what it is as efficient as possible;
- The program should take into account hints for every previous try (if it's smaller or bigger than the guessed number);

### Evaluation
Results are evaluated according to the mean guess numbers for 1000 repetitions

**What do we practice?**
Learn how to write readable and reproducible code in python

## Data description

The list of randomly generated numbers ranged from 0 to 100

## Project steps

1. Check out the [baseline solution](https://github.com/lamewarden/sf_data_science-2022-/blob/main/project%200/game(baseline_solution).py) provided by the teacher.
2. Modify the function `random_predict` in the [baseline solution](https://github.com/lamewarden/sf_data_science-2022-/blob/main/project%200/game(baseline_solution).py) in order to optimize it. The description of the new `fractions_of_100_predict` function logic can be found in the [new function docstring](https://github.com/lamewarden/sf_data_science-2022-/blob/main/project%200/game_solution.py).

## Results

`fractions_of_100_predict` function guess the secret number in 5 attempts

## Conclusions

Random guess sucks.



