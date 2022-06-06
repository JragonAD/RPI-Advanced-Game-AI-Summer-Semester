# Numpy Neural Network

import gym
import pickle
import random
import numpy as np
from time import time


rng = np.random.default_rng(314)


def generate_random(size):
    rand_arr = rng.random(size)
    rand_signs = rng.choice([-1, 1], size)
    return rand_arr * rand_signs


def relu(a):
    return np.where(a > 0, a, 0)


def softmax(a):
    return np.exp(a) / np.sum(np.exp(a))


def sigmoid(a):
    return 1 / (1 + np.exp(-a))


sigmoid_v = np.vectorize(sigmoid)


def time_elapsed(prev, cur, round_digit=8):
    delta_time = cur - prev
    return f"\tTime elapsed: {round(delta_time, round_digit)} seconds"


# Mutation rate = 1/k where k is number of generations

params = {
    "env_name": "CartPole-v1",
    "model_path": "model.bin",
    "architecture": (4, 8, 2),
    "population": 64,
    "generations": 8,
    "keep_percentage": 0.5,
    "episodes": 8,
    "max_episode_length": 2000,
    "target_step": 300,
    "mutation_variance": 0.08,
    "mutation_percentage": 1.00,
    "verbose:": True,
    "render_env": False,
    "record_env": False,
}


class NN:
    def __init__(self, params, net_to_copy=None):
        self.params = params

        if net_to_copy is None:
            arch = self.params["architecture"]

            weights = [
                generate_random((arch[i + 1], arch[i])) for i in range(len(arch) - 1)
            ]

            biases = [generate_random((arch[i],)) for i in range(1, len(arch))]

        else:
            mut_var = self.params["mutation_variance"]

            weights = net_to_copy.weights
            biases = net_to_copy.biases

            weights = [
                weight + np.random.normal(0.0, mut_var, weight.shape)
                for weight in weights
            ]
            biases = [
                bias + np.random.normal(0.0, mut_var, bias.shape) for bias in biases
            ]

        self.weights = weights
        self.biases = biases

        self.fitness = None

    def _forward(self, observation):
        weights = self.weights
        biases = self.biases

        a = np.array(observation)

        for i in range(len(weights)):
            a = relu(weights[i] @ a + biases[i])

        probabilities = softmax(a)
        action = np.argmax(probabilities)

        return action

    def _evaluate(self):
        ep_rewards = []
        env = gym.make(self.env_name)

        if self.params["record_env"]:
            env = gym.wrappers.Monitor(env, "recording")

        env._max_episode_steps = self.params["max_episode_steps"]

        for _ in range(self.params["episodes"]):
            observation = env.reset()
            done = False
            score = 0

            while not done:
                if self.params["render_env"]:
                    env.render()

                action = self._forward(observation)

                observation, reward, done, _ = env.step(action)
                score += reward

            ep_rewards.append(score)

        env.close()

        return np.array(ep_rewards).mean()

    def get_fitness(self, evaluate_anyways):
        if evaluate_anyways or self.fitness is None:
            fitness = self._evaluate()
            self.fitness = fitness
            return fitness

        return self.fitness


class GA:
    def __init__(self, params):
        self.params = params
        self.generations_trained = 0

        self.nets = [NN(params) for _ in range(params["population"])]

    def evaluate(self):
        fitness_arr = []
        sorted_nets = []

        for i, net in enumerate(self.nets):
            if i < int(params["population"] * params["keep_percentage"]):
                print("Network:", i + 1, "\tEvaluated. Skipping.")
            prev_time = time()

            fitness = net.get_fitness()
            if self.verbose:
                print(
                    "Network:",
                    i + 1,
                    "\tFitness:",
                    round(fitness),
                    time_elapsed(prev_time, time()),
                )

            inserted = False
            for j in range(len(fitness_arr)):
                if fitness_arr[j] > fitness:
                    fitness_arr.insert(j, fitness)
                    sorted_nets.insert(j, net)
                    inserted = True
                    break

            if not inserted:
                fitness_arr.append(fitness)
                sorted_nets.append(net)

            if fitness == self.goal:
                break

        fitnesses = np.array(fitness_arr)

        return sorted_nets, fitnesses

    def mutate_nets(self, parents):
        params = self.params

        new_nets = [
            NN(params, random.choice(parents))
            for _ in range(params["population"] - len(parents))
        ]

        return new_nets

    def train(self):
        params = self.params

        for i in range(params["generations"]):
            prev_time = time()

            nets, fitnesses = self.evaluate()

            if self.verbose:
                print(
                    "=====",
                    "Generation:",
                    i + 1,
                    "\tMaximum Reward:",
                    round(fitnesses.max()),
                    "\tAverage Reward:",
                    round(fitnesses.mean()),
                    time_elapsed(prev_time, time(), 3),
                    "=====",
                    "\n",
                )

            parents = nets[
                int(params["population"] * (1 - params["keep_percentage"])) :
            ]

            children = self.mutate_nets(parents)

            self.nets = parents + children

            self.generations_trained += 1

            if fitnesses[-1] == self.goal:
                print("Callback reached: Max score obtained.")
                self.solved_net = nets[-1]
                break

        """Note:
        Not done yet, needs model path generation and testing
        """

    def load(self):
        with open(path, "rb") as f:
            self.nets = pickle.load(f)

    def save(self):
        data = {""}
        with open(path, "wb") as f:
            pickle.dump(self.nets, f)
