# Imports

import random
import string

# Constants

POPULATION = 100
MUTATION_N = 1
LETTERS = [char for char in string.ascii_letters + "!?,. "]

# Funcs

def generate_population(length):
    parents = []

    for i in range(POPULATION):
        parents.append("".join([random.choice(LETTERS) for i in range(length)]))

    return parents

def fit_func(target, generated):
    fit = 0

    for i in range(len(target)):
        if target[i] == generated[i]:
            fit += 1

    return fit

def select_parents(target, parents):
    isFound = False
    selected = []
    fits = []

    for i, parent in enumerate(parents):
        fit = fit_func(target, parent)
        if fit == len(target):
            isFound = True

        # Insertion sort
        isInserted = False
        for j in range(i):
            if fits[j] >= fit:
                fits.insert(j, fit)
                selected.insert(j, parent)
                isInserted = True
                break
        if not isInserted:
            fits.append(fit)
            selected.append(parent)

    selected = selected[int(POPULATION / 2):]

    return selected, isFound, selected[-1], fits[-1]

def mutation(gene):

    for i in range(MUTATION_N):
        index = random.randint(0, len(gene)-1)
        gene = gene[:index] + random.choice(LETTERS) + gene[index+1:]

    return gene

target = input("Input: ")
print(f"Target: ", target)
length = len(target)
print(f"Length: ", length)

parents = generate_population(length)

isFound = False
iteration_num = 0

while not isFound:
    iteration_num += 1

    selected, isFound, bestGene, bestFitness = select_parents(target, parents)

    mutated = []
    for gene in selected:
        mutated.append(mutation(gene))

    parents = selected + mutated

    print(f"Iteration: {iteration_num} Best gene: {bestGene} Best fitness: {bestFitness}")