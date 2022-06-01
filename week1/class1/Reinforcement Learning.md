# Reinforcement Learning

- GA learning encodes solutions directly and doe snot consider the state of the world
- RL is learning from interaction and observations from the world

## MDP Model

- `<S,T,A,R>`
- S - set of states
- A - set of actions
- T - The probability of transition from *s* to *s'* given action *a*
- R(s,a) - the expected reward for taking action *a* in state *s*

## Categories of RL

- Model-based RL
  - Constructs domain transition model, MDP
    - E^3 - Kearns and Singh
  - Model-free RL
    - Only concerns policy
      - Q-Learning, Sarsa
  - Active Learning (Off-Policy Learning)
    - Q-Learning
    - Actively engage in exploration
  - Passive Learning (On-Policy Learning)
    - Sarsa
    - Observe surrounding agents to learn

## Challenges of Reinforcement Learning

- No knowledge of environment
  - Can only act in the world and observe states and reward
- Many factors make RL difficult:
  - Actions have non-deterministic effects
    - Which are initially unknown
  - Rewards / punishments are infrequent --> **Delayed Reward**
    - Often at the end of long sequences of actions
    - How do we determine what action(s) were really responsible for reward or punishment? (credit assignment)
  - World is large and complex
- Nevertheless, the learner must decide what actions to take
  - We will assume the world behaves as an MDP

## Delayed Reward Problem

- Delayed reward makes learning challenging
- For example, the choice in state *S* may lead to a big reward, but the action in *S'* seems to lead to the reward in *S''* because it's closer to the reward

## Model-Based vs Model-Free RL

- MDP and POMDP assume that the agent accurately knows the transition function and the reward for all states in the environment
- RL *can be* model-free learning, meaning that

## Passive vs Active Learning

- Passive
  - The agent watches the world going by and tries to learn the utilities of being in various states
  - **Update the utility value using the given training sequences**
- Active
  - The agent will explore the world
  - Needs to balance **exploration and exploitation**
  - Whether the AI should make predictions on what its learned or take random moves to look for other, better paths

    - Similar to GA

## Q-Learning

- Give each cell (Q, A) values, and update the Q values
  - Ex. A = right (rational decision)
    - (Q, up) = 0.1
    - (Q, down) = 0.1
    - (Q, left) = 0
    - (Q, right) = 0.5
- Q-learning finds a mapping from state/action pairs to values (called Q-values)
  - Create graph of all states horizontally by all actions vertically
  - Update each cell as per below
  - The max value of each column--after the table is fully trained--represents the most optimal path
  - With more transactions (iterations of path), reward is propagated backwards until the origin decision necessary to reach reward is found
    - **Solves Delayed Reward Problem**
      - As path to reward is discovered
  - Takes many iterations to make solution apparent
    - As compared to genetic algorithm, where you can get lucky
    - If plot reaches a value that doesn't change too much, an approximate solution may be assumed

```txt
    - Initialize Q(s,a) arbitrarily (typically 0)
    - Repeat (for each episode):
        - Initialize s --> equivalent to resetting the environment
        - Choose a from s using policy derived from Q
            # In the process of training the table, the policy can be random (doesn't have to be the action with maximum reward)
            # Once the policy is trained, then choose maximum reward for optimal solution
        - Take action a, observe r, s'
        - Q(s, a) <-- Q(s, a) + {alpha}[r + {gamma}max_a'Q(s', a') - Q(s, a)]
            #! Bellman Equation
            # Where {alpha} and {gamma} are constants between 0 and 1
            # Part of previous computation + learning rate * [reward + maximum future reward]
        - s <-- s'
    - Until s is terminal
```

### Alpha

- Learning rate
- How much of the original Q-value is kept
- Comparable to mutation rate in GA
- Tune it down near the end of training
- Fixed vs Variable
  - Fixed alpha generates faster learning --> rewards are not decayed
  - However, Q-learning with fixed alpha is not guaranteed to converge

### Gamma

- Discount of future reward
- Typically not changed over training

### Def

- didactic

### Monte Carlo Policy Evaluation

- Works with episodic environments, where a series of steps can be taken, with a final reward provided
- No bias
- Steps evaluated based on final reward

### Temporal Difference

- Some bias
- Previous step evaluated based on current step

### Think of above as two ends of an axis: one step or all steps
