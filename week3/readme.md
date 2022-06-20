# Exploring OpenAI Baseline Library

## Running Code

- Open StableBaselineAlgorithms.ipynb
- Run all code up to the calls to learning the environments (`{model name}.learn()`)
- Load the model to evaluate using `{model name}.load()`
- Evaluate the model using `{model name}.evaluate()`
  - The sequence of evaluation is PPO, DQN, A2C

## Viewing Tensorboard Logs

- Navigate to the current directory in cmd
- Launch TensorBoard using `tensorboard --logdir="./"`
  - Alternatively, change logdir to the desired environment to see only the training data for that environment
