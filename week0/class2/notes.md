# Search Capabilities

## Search

### Quality

### (See slides for complete notes)

# Problems with Fitness Range

## Premature convergence

- Population converges on local maximum
- Doesn't find true solution before completing

## Slow finishing

- Too "careful" in finding solution
- Doesn't complete with given computational cycles

# Terms

## Generation gap

- Proportion of population replaced

## Selecting pressure

- Difference of fitness among individuals
- Helps determine which parent (individual) gets selected for the next generation

# Chromosome Selection Techniques

## Elitism (Generational GA)

- Replace most members of population

## Steady State Selection

- More conservative approach than replacing most of population
- Used when closer to solution for fine tuning

## Fitness Proportionate Selection

- Roulette Wheel Selection (original technique)
- Better individuals get higher chance (greater percentage of the pie chart)
  - Chances proportionate to fitness
- Implementation
  - Assign each individual to part of the roulette wheel
  - Spin the wheel n times to select n individuals
- Why give poorer individuals a chance?
  - Just in case they lead to a global maximum solution
  - Low chance corresponds with the low chance that they lead to a solution, but still is non zero
- Should you allow chosen individuals to be chosen again?
  - If overall population is large, we can afford it.
  - If overall population is small, it's probably not the best for efficiency.

## Tournament

- All other methods rely on global population statistics
  - Could be a bottleneck especially on parallel machines
  - Relies on presence of external fitness function which might not exist
    - Ex. evolving game players
- Procedure for Tournament selection:
  - Pick k members at random then select the "best" of these
  - Repeat to select more individuals

### Tournament Types

- Binary tournament
  - Choose one of two
- Probabilistic binary tournament
  - Two individuals are randomly chosen; with a chance p, 0.5 < p < 1, the fitter of the two parents are selected
- Larger tournaments
  - n individuals randomly chosen with fittest selected
- Chancing n and/or p affects the GA dynamically

# Scaling Techniques

- Instead of using the raw fitness score, run it through a function first.

## Ranked Scaling (Linear Scaling)

- Instead of absolute fitness score, rank them first, then use a distribution based on ranks
- New score = (p-ri)(max-min)/(P-1) + min
  - Where ri is the rank of individual i
  - P is the population size
  - Max --> best fitness
  - Min --> worse fitness
- Yields better selecting pressure while population converges
  - Tends to avoid premature conversion by tempering selection pressure
  - Amplifying small fitness differentials in later generations increases selection pressure
- Cons:
  - Worse distinguishability for individuals with higher differences in fitness
    - Slow convergence
  - Population must be sorted each cycle --> computationally expensive

## Sigma Scaling

- Keeps selection pressure relatively constant
  - Not too strong in early generations and not too weak once population stabilizes and fitness differences are smaller
- An individual's expected value is a function of its fitness, the population mean, and the population standard deviation
