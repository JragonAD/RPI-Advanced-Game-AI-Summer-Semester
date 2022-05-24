import random

from constants import *

class Gene:
    def __init__(self, gene):
        self.gene = gene
        self.length = len(gene)

        # self.target = ""
        # self.target_compare = []

    def get_fitness(self, target):
        target = target.get_gene()
        fit = 0

        self.is_letter_locked = [False] * self.length # If current letter is correct, don't mutate
        self.is_letter_contained = [False] * self.length # If current letter is contained, move when mutating

        if self.gene == target:
            return len(self.gene * MATCH_REWARD)

        target_compare = [char for char in target]
        for i in range(len(target_compare)):
            if self.gene[i] == target_compare[i]:
                fit += MATCH_REWARD
                target_compare[i] = "*"
                self.is_letter_locked[i] = True

        for i in range(len(target_compare)):
            if self.is_letter_locked[i]: # Ensures following checks exclusively for contained letters
                continue

            if self.gene[i] in target_compare:
                fit += CONTAIN_REWARD
                target_compare[target_compare.index(self.gene[i])] = "*"
                self.is_letter_contained[i] = True

        # self.target = target
        # self.target_compare = target_compare

        return fit

    def get_mutation(self) -> str:
        if True in self.is_letter_contained:
            choice = random.choice([True, False])
        else:
            choice = True

        i = 0
        # j= 0
        while i < MUTATION_N:
            # j += 1
            # if j > 100:
                # print("A", self.gene, self.is_letter_contained, self.is_letter_locked)

            index = random.randint(0, len(self.gene)-1)

            if choice: # Replace letter
                if sum(self.is_letter_locked) + sum(self.is_letter_contained) == self.length:
                    gene = self.gene
                    break

                if self.is_letter_locked[index]: # Only let unlocked letters mutate
                    continue

                if self.is_letter_contained[index]:
                    continue

                gene = self.gene[:index] + random.choice(LETTERS) + self.gene[index+1:]

            else: # Move letter
                if not self.is_letter_contained[index]:
                    continue

                # k = 0
                while True:
                    # k += 1
                    # if k > 100:
                        # print(self.target, self.target_compare, self.gene, self.is_letter_contained, self.is_letter_locked)

                    to_index = random.randint(0, len(self.gene)-1)

                    if self.is_letter_locked[to_index]:
                        continue

                    if index == to_index:
                        continue

                    gene_chars = [char for char in self.gene]

                    temp = gene_chars[to_index]
                    gene_chars[to_index] = gene_chars[index]
                    gene_chars[index] = temp

                    temp_bool = self.is_letter_contained[to_index]
                    self.is_letter_contained[to_index] = self.is_letter_contained[index]
                    self.is_letter_contained[index] = temp_bool

                    gene = "".join(gene_chars)
                    break

            i += 1

        return gene # Returns mutated to create new gene with; keeps this one same

    # Both mutate and swap letters to increase efficiency; doesn't seem to actually work
    def get_mutation_both(self): #! NOTE: This function is not used. It serves as a reference for possible improvements
        choices = [True, False]
        for choice in choices:

            i = 0
            # j= 0
            while i < MUTATION_N:
                # j += 1
                # if j > 100:
                    # print("A", self.gene, self.is_letter_contained, self.is_letter_locked)


                index = random.randint(0, len(self.gene)-1)

                if choice: # Replace letter
                    if sum(self.is_letter_locked) + sum(self.is_letter_contained) == self.length:
                        gene = self.gene
                        break

                    if self.is_letter_locked[index]: # Only let unlocked letters mutate
                        continue

                    if self.is_letter_contained[index]:
                        continue

                    gene = self.gene[:index] + random.choice(LETTERS) + self.gene[index+1:]

                else: # Move letter
                    if True not in self.is_letter_contained:
                        break

                    if not self.is_letter_contained[index]:
                        continue

                    # k = 0
                    while True:
                        # k += 1
                        # if k > 100:
                            # print(self.target, self.target_compare, self.gene, self.is_letter_contained, self.is_letter_locked)

                        to_index = random.randint(0, len(self.gene)-1)

                        if self.is_letter_locked[to_index]:
                            continue

                        if index == to_index:
                            continue

                        gene_chars = [char for char in self.gene]

                        temp = gene_chars[to_index]
                        gene_chars[to_index] = gene_chars[index]
                        gene_chars[index] = temp

                        temp_bool = self.is_letter_contained[to_index]
                        self.is_letter_contained[to_index] = self.is_letter_contained[index]
                        self.is_letter_contained[index] = temp_bool

                        gene = "".join(gene_chars)
                        break

                i += 1

        return gene # Returns mutated to create new gene with; keeps this one same

    def get_gene(self):
        return self.gene

    def get_length(self):
        return self.length