from ant import Ant


class Colony:
    def __init__(self, nr_ants, alpha, beta, attractions):
        self.nr_ants = nr_ants
        self.alpha = alpha
        self.beta = beta
        self.attractions = attractions
        self.ants = self.spawn_ants()


    def spawn_ants(self): #TODO mrówka powinna miec losowa atrakcje jako pierwsza (od niej zaczyna)
        ants = []
        for i in range(self.nr_ants):
            ants.append(Ant(self.attractions))