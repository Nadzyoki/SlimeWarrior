from ursina import *
import random

class Slime(Entity):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.dist = 20
        self.speed = 5
        self.knowledge_dis = {
            "home" : 0,
            "fire" : 0,
            "water": 0,
            "rock" : 0,
            "tree" : 0,
            "metall":0
        }

    def update(self):
        pass

#get data other around
    def Spray(self):
        for i in range(360):
            self.rotation_directions = i
            v = raycast(origin=self, direction=self.forward, ignore=(self,), distance=self.dist)
            if v.hit:
                match v.entity.tag:
                    case "friend":
                        v.entity.Know(self.MyKnow())
                    case "warrior":
                        print("No")
                    case "res":
                        print("oh my")
                    case _:
                        print("ERROR WTF THIS IS???????")

    def MyKnow(self):
        ret = []
        ret[0] = random.choice(self.knowledge_dis.keys())
        ret[1] = self.knowledge_dis[ret[0]]
        return ret

    def Know(self,kn):
        if kn[1] < self.knowledge_dis[kn[0]]:
            self.knowledge_dis[kn[0]] = kn[1]
