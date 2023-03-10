_ = False
mini_map = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,2,2,2,2,2,_,_,_,_,3,_,3,_,3,_,_,_,1],
    [1,_,_,_,_,_,2,_,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,2,_,_,_,2,_,_,_,_,3,_,5,_,3,_,_,_,1],
    [1,_,_,_,_,_,2,_,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,2,2,_,2,2,_,_,_,_,3,_,3,_,3,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,4,2,3,1,4,1,3,2,1,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,3,1,2,3,2,4,_,3,_,1],
    [1,_,_,_,_,_,_,_,_,_,_,_,_,_,1,_,_,_,_,_,_,2,_,1],
    [1,4,4,4,4,4,4,4,4,_,_,_,_,_,2,_,2,3,2,1,1,4,_,1],
    [1,4,_,4,_,_,_,_,4,_,_,_,_,_,2,_,2,_,_,_,_,_,_,1],
    [1,4,_,_,_,_,5,_,4,_,_,_,_,_,1,_,1,_,_,_,_,_,_,1],
    [1,4,_,4,_,_,_,_,4,_,_,_,_,_,2,_,4,_,_,_,_,_,_,1],
    [1,4,_,4,4,4,4,4,4,4,4,4,4,4,4,_,4,3,3,3,3,3,3,1],
    [1,4,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,3,1],
    [1,4,4,4,4,4,4,4,4,_,_,_,_,_,_,_,3,3,3,3,3,_,3,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()
    
    def get_map(self):
        """
        Armazena toda posição da matriz que contenha um obstáculo
        """
        for i in range(len(self.mini_map)):
            for j in range(len(self.mini_map[i])):
                if self.mini_map[i][j]:
                    self.world_map[(j,i)] = self.mini_map[i][j]
