# Markov Decision Process (MDP)

## Finite State Machine vs

- State
  - Initial state
  - Final state
- Transition

## Markov Decision Process

- Markov - things that deal with probabilities / uncertainties
- Assumes that all actions will only succeed n% of the time
- P_a(s, s'), P(s, a, s')
- Transition function affects the probabilities of the system in each state

### Notation

- Tuple (S, A, P(.,.), R(.)))
  - S -> state space
  - A -> action space
  - P_a(s, s') = Pr(s_(t+1) = s' | s_t = s, a_t = a)
  - R(s) = immediate reward if the current state is S

### Define the goal of a MDP

- For example, if we want a light to be off at the end of the game, we can define
  - R(light on) = 0
  - R(light  off) = 1

### Automated action selection: maximize expected rewards

```txt
- Current state s
- For each action a:
  - Reward = sum(p(s, a, s') * r(s'))
- Select the action with the highest reward
```

- So if the light is on, what is the best action to do?
  - Action 1: turn the light on
    - Reward = (0.9 \* 0 + 0.1 \* 1) = 0.1
  - Action 2: turn the light off
    - **Reward = (0.1 \* 0 + 0.9 \* 1) = 0.9**
- Typically uses recursive work to determine expected reward looking ahead
- Accumulate the reward
- Then determine best path

### Discount of future rewards

- Total reward after n steps = reward0 + {gamma}1 \* reward1 + {gamma}2 \* reward2 + ... + {gamma}(n - 1) \* reward(n - 1)
- Ex. To calculate rewards over two steps starting from S1
  - A1
    - 0.9 \* R(S1) + 0.1 \* R(S2) --> step1 reward, reward0
    - 0.9 \* R1step(S1) + 0.1 \* R1step(S2) --> step2 reward, reward1
      - Where R*n*step(S*k*) is the computed expected reward from the step
  - A2
    - ??

## Markov Chains
