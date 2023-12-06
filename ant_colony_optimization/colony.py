from ant import Ant


class Colony:
    def __init__(self, nr_ants, alpha, beta, attractions):
        self.nr_ants = nr_ants
        self.alpha = alpha
        self.beta = beta
        self.attractions = attractions
        self.ants = [Ant(self.attractions) for i in range(self.nr_ants)]
        self.pheromones = [[1 for i in range(len(self.attractions))] for j in range(len(self.attractions))]
        #TODO pamietac, ze to to indeksowane od 0, a atrakcje od id 1

