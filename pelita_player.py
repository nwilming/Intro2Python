from pelita.player import AbstractPlayer, SimpleTeam
import numpy as np
import networkx as nx

from tsp_solver.greedy import solve_tsp

# Call like this: pelita /path/pelita_player.py:team1 /path/pelita_player.py:team2

class Collector(AbstractPlayer):
    """
    A Player that aims to collect as much as possible. It
    coordinates with other Collector players.
    """

    def set_initial(self):
        '''
        Precompute a graph of the maze, an adjacency list that contains
        distances between food items and an optimal tour through food.

        '''
        universe = self.current_uni
        self.graph = nx.Graph()  # Represent board as a graph
        # now iterate over all free positions
        for pos, neighbors in universe.free_positions():
            for n in neighbors:
                self.graph.add_edge(pos, n)

        self.shortest_tour = self.enemy_food
        self.opt_tours()

    def get_move(self):
        '''
        Compute a new move for this bot.
        '''
        enemy_pos = [e.current_pos for e in self.enemy_bots]
        try:
            index = 0 if self.me.index == 0 else -1
            target = self.shortest_tour[index]
            if target == self.current_pos:
                self.opt_tours()
                target = self.shortest_tour[index]

            # Compute shortest path to next target
            path = nx.shortest_path(self.graph, self.current_pos, target)
            # Translate next position in path to target to a move
            pos = path[1]
            pos2move = dict((v, k) for k, v in self.legal_moves.items())
            move = pos2move[pos]

            if pos in enemy_pos:
                # Next move moves onto enemy bot, return random
                # TODO: Check if in own half (will wrongly avoid in this case)
                print('Too close to enemy bot')
                del pos2move[pos]
                return self.rnd.choice(list(pos2move.values()))
            if pos in self.enemy_food:
                # If next move is onto food pellet remove it from targets
                self.shortest_tour = [
                    x for x in self.shortest_tour if not (x == pos)]

            return move

        except (KeyError, IndexError):
            import traceback
            print(traceback.format_exc())
            return self.rnd.choice(list(self.legal_moves.keys()))

    def tour_length(self, tour):
        '''
        Compute the length of a tour. 

        This can be ommitted when using a proper TSP library.
        '''
        cost = 0
        for start, end in zip(tour[0:-1], tour[1:]):
            cost += self.adjacency[start, end]
        return cost

    def opt_tours(self):
        '''
        Generate shortest tour through enemy food.
        '''
        n_food = len(self.enemy_food)
        # Create adjacency list of distance of enemy food
        self.adjacency = np.zeros((n_food, n_food))
        for i, f1 in enumerate(self.enemy_food):
            for j, f2 in enumerate(self.enemy_food):
                self.adjacency[i, j] = len(
                    nx.shortest_path(self.graph, f1, f2))  # Compute shortest path
        tour = solve_tsp(self.adjacency)
        self.shortest_tour = [self.enemy_food[t] for t in tour]


def team1():
    return SimpleTeam("CollectorZ", Collector(), Collector())


def team2():
    return SimpleTeam("KolleKtorZ", Collector(), Collector())
