from random import randint
from numpy import zeros, add, subtract, multiply, negative, array
from itertools import product

class board():    
    def __init__(self, dim=randint(2,9)):
        self.dim = dim
        self.state = zeros((3,)*dim, dtype = int)
        self.score = dict()

    def place(self, pt, symbol):
        if len(pt) != self.dim or not all(3>=index>=0 for index in pt):
            raise Exception("Point specified is not a point on the board (dimention mismatch?)")
        elif self.state[pt] == 0:
            points = 0
            p = list(product([0,1,-1], repeat=self.dim))
            p.remove((0,)*self.dim)
            for n in p:
                try:
                    print "thingy"
                    if self.state[tuple(add(n, pt))] == symbol:
                        print "dude"
                        try:
                            if self.state[tuple(add(multiply(n,2), pt))] == symbol:
                                points += 1
                                print n
                        except IndexError:
                            pass
                        try:
                            behind = tuple(subtract(pt, n))
                            print "first", behind
                            if not any((x < 0 for x in behind)):
                                try:
                                    p.remove(behind)
                                except ValueError:
                                    pass
                                print "second", behind
                                if self.state[tuple(subtract(pt, n))] == symbol:
                                    points += 1
                                    print n, self.state[tuple(subtract(pt, n))], tuple(subtract(pt, n))
                        except IndexError:
                            pass
                except IndexError:
                    pass
            if symbol in self.score.keys():
                self.score[symbol] += points
            else:
                self.score[symbol] = points
            self.state[pt] = symbol
            print points
        else:
            raise Exception("Point already occupied.")
