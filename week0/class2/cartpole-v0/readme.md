# Cartpole-v0 05-29-22
- Time spend coding: 2 hours

## Utilizes genetic algorithm:
- (4, 16, 2) Architecture
- Default constants of:
    - 32 Population
    - 5 Generations
    - 8 Episodes
    - 0.1 Mutation Variance

## Features:
- Training callback to stop training when max score reached
    - Prevents over-training and decreases training duration
- Model save and load feature to restore NNs

## Solutions:
- Default constants produced average results
- Faster version with following changes solved in **10.692** seconds:
    - (4, 8, 2) Architecture
    - 10K Episode Length
    - 64 Population
- Extremely fast version solved in **0.814** seconds with slightly more "bouncy" solution
    - (4, 4, 2) Architecture
    - 5K Episode Length
    - 64 Population
    - 2 Episodes Per Evaluation
- Way too fast version solved in **0.018** seconds with perfect PID (what???)
    - (4, 1, 2) Architecture
    - 200 Episode Length
    - 64 Population
    - 1 Episode Per Evaluation

![Solve Video](solve.mp4)