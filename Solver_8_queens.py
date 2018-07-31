import numpy as np
import random


class Solver_8_queens:

    def __init__(self, pop_size=30, cross_prob=1.0, mut_prob=1.0):
        self.__pop_size = pop_size
        self.__cross_prob = cross_prob
        self.__mut_prob = mut_prob

    def solve(self, min_fitness=None, max_epochs=None):
