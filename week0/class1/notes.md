# Genetic Learning

## Population

Chromosomes could be:

- Bit strings (0101... 11000)
- Real numbers (43.2, -33.1 ... 0.0 89.2)
- Permutations of element (E11E3 E7 ... E1 E15)
- Any data structure

## Mutation

### Crossover: Recombination
- Greatly accelerates search early in evolution
- Leads to effective combination fo schemata

### N-point crossover
- Choose n random points to cross over

### Uniform crossover
- Random (heads/tails) for each cell of gene
- Pretty much only works for binary
- Rare

### Local Modification
- Ex. one bit mutation --> changes one element of genome
- Causes movement in the search space
- Restores lost info to the population
- Don't change too dramatically (~10%)

### Displacement
- Grab random from Parent A --> insert randomly into parent B

### Insertion
- Like displacement, but for single gene

### Inversion
- Reverse chosen string

### Displaced Inversion

## Evaluation
- Evaluator decodes a chromosome and assigns fitness
- Evaluator is the only link between GA and its problem

## Selection

Start with generational to allow for more randomness/changes

### Generational
- Entire (most of) population replaced

### Steady-state
- Few members replaced each  generation

## Things We Can Tweak

- Mutation rate - 0.01 is reasonable
- Chromosome length - varies based on problem
- Population size - 150-250

## Video notes

- Bit_error_rate = 1 / MAX_FITNESS --> Worse a child performs, the more it's mutated for variety

# Neural Network with Multiple Layers

## Inputs, Intermediate (Hidden), Output Layers

Values can be experimental parameters set based on prior experience

### Brief mention: Auto-encoder AI

- Type of AI where the hidden nodes are drastically less than input/output nodes
- Used to match the input and output by decimating quality
- Ex. hand drawn digit to digital digit through reducing image quality

## Nodes Connected by Links

- Links each contain a weight that affects the data being passed between nodes
- Sigmoid function of sum of activity --> See Sigmoid Perceptron Unit
    - Sigma(wn * xn) --> where w is weight and x is input value
    - Sigmoid = 1/(1 + n^-x)
    - Activation function:
        - If the sum reaches a certain threshold, it returns 1, else -1
- Some nodes may contained constants called biases
    - Connected to the hidden layer like any other input node, but biases the decision making

### Sigmoid Perceptron Unit

- Contained in each hidden layer node
- Other LTUs can be used, such as:
    - Perceptron
    - Softmax
    - ReLu

# Evolving Neural Networks

## Case 1: Weights of the links can be represented as a list of real numbers:
- -1.0, 0.3, 0.7, ...
- Using GA for evolving the weights
- Look into breadth-first search

## Case 2: The topology of the neural network itself can evolve (NEAT)
- Adding, combining, deleting nodes in addition to varying the link weights

# Implementing Neural Networks

## Overview of the Algorithm

1. Design a neural network for the problem
    - Decide number of input or output nodes
    - Decide number of middle layers and number of nodes per based on experience or heuristics

2. Put the weight of each link into a list in order
3. Randomly generate a population of weights (100-200)
4. Select the parents based on fitness function
    - Decide what portion to select (half, bad ones, etc)
5. Perform recombination and mutation
6. Repeat 4 and 5 until result is good enough

## Generating a node

- for each layer: for each node: sum += weight * value
- return sigmoid(sum)

