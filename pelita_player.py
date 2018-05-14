from pelita.player import AbstractPlayer, SimpleTeam
import numpy as np
import networkx as nx

from tsp_solver.greedy import solve_tsp

goals = None


class Goals(object):
    '''
    Represent and coordinate goals for two bots.
    '''

    def __init__(self, bot, maze, universe):
        self.graph = nx.Graph()
        # now iterate over all free positions
        for pos, neighbors in universe.free_positions():
            for n in neighbors:
                self.graph.add_edge(pos, n)

        n_food = len(bot.enemy_food)
        self.adjacency = np.zeros((n_food, n_food))
        for i, f1 in enumerate(bot.enemy_food):
            for j, f2 in enumerate(bot.enemy_food):
                self.adjacency[i, j] = len(
                    nx.shortest_path(self.graph, f1, f2))
        self.targets = bot.enemy_food
        self.target_idx = np.arange(len(self.targets))
        self.shortest_tour = self.targets
        self.lowest_cost = 10000000
        self.opt_tours(2)

    def update(self, bot):
        '''
        Compute a new move for this bot.
        '''
        enemy_pos = [e.current_pos for e in bot.enemy_bots]
        try:
            if bot.me.index == 0:
                target = self.shortest_tour[0]
            else:
                target = self.shortest_tour[-1]
            path = nx.shortest_path(self.graph, bot.current_pos, target)
            legal_moves = bot.legal_moves
            pos = path[1]
            pos2move = dict((v, k) for k, v in legal_moves.items())
            move = pos2move[pos]
            if pos in enemy_pos:
                print('DANGER')
                del pos2move[pos]
                bot.rnd.choice(list(pos2move.values()))
            if pos in bot.enemy_food:
                self.targets = [x for x in self.targets if not (x == pos)]
                self.shortest_tour = [
                    x for x in self.shortest_tour if not (x == pos)]

            return move
        except (KeyError, IndexError):
            print('RANDOM')
            return bot.rnd.choice(list(legal_moves.keys()))

    def tour_length(self, tour):
        '''
        Compute the length of a tour
        '''
        cost = 0
        for start, end in zip(tour[0:-1], tour[1:]):
            cost += self.adjacency[start, end]
        return cost

    def opt_tours(self, dt):
        '''
        Generate optimal tour.
        '''
        tour = solve_tsp(self.adjacency)
        cost = self.tour_length(tour)
        if cost < self.lowest_cost:
            print(cost)
            self.lowest_cost = cost
            self.shortest_tour = [self.targets[t] for t in tour]


class Collector(AbstractPlayer):
    """
    A Player aims to collect as much as possible. It
    coordinates with other Collector players.
    """

    def set_initial(self):
        global goals
        if goals is None:
            goals = Goals(self, self.current_uni.maze, self.current_uni)

    def get_move(self):        
        return goals.update(self)


def team():
    return SimpleTeam("CollectorZ", Collector(), Collector())
