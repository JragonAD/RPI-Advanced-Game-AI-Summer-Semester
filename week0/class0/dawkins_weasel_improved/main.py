import random

from constants import *
from gene import Gene


def generate_word(length):
    return "".join([random.choice(LETTERS) for i in range(length)])


class Runner:
    def __init__(self, target_str):

        self.target = Gene(target_str)

        # print(f"Target: ", self.target.get_gene())

        self.length = self.target.get_length()
        # print(f"Length: ", self.length)

        self.parents = self.generate_population()

    def generate_population(self):
        parents = []

        for i in range(POPULATION):
            parents.append(Gene(generate_word(self.length)))

        return parents

    def select_parents(self):
        isFound = False
        selected = []

        selected = sorted(self.parents, key=lambda f: f.get_fitness(self.target))

        selected = selected[int(POPULATION * (1 - KEEP_PERCENTAGE)) :]

        max_fitness = selected[-1].get_fitness(self.target)

        isFound = max_fitness == self.target.get_fitness(self.target)

        return selected, isFound, selected[-1].get_gene(), max_fitness

    def run(self):
        isFound = False
        iteration_num = 0

        while not isFound:
            iteration_num += 1

            selected, isFound, bestGene, bestFitness = self.select_parents()

            mutated = []
            for i in range(int(POPULATION * (1 - KEEP_PERCENTAGE))):
                mutated.append(Gene(selected[i % len(selected)].get_mutation()))

            self.parents = selected + mutated

            # print(f"Iteration: {iteration_num} Best gene: {bestGene} Best fitness: {bestFitness}")

        return iteration_num


if __name__ == "__main__":
    total_iterations = 0
    for i in range(1, TEST_CASES + 1):
        word = generate_word(WORD_LENGTH)
        r = Runner(word)
        iterations = r.run()

        print(f"Test case: {i} Word: {word} Iterations: {iterations}")

        total_iterations += iterations

    print()
    print(f"Total iterations: {total_iterations} for {TEST_CASES} test cases.")
    print(
        f"With an average of {total_iterations / TEST_CASES} iterations per test case."
    )


"""
Total iterations: 5093 for 250 test cases.
With an average of 20.372 iterations per test case.
"""
