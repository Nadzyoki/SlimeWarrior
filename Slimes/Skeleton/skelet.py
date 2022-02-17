from ursina import *
import random

class Slime(Entity):
    def __init__(self):
        super().__init__()
        self.hp = 100
        self.dist = 20
        self.speed = 5
        self.knowledge = {
            "home" : 0,


        }

    def Spray(self):
        for i in range(360):
            self.rotation_directions = i
            v = raycast(origin=self, direction=self.forward, ignore=(self,), distance=self.dist)
            if v.hit:
                match v.entity.tag :
                    case "friend":
                        v.entity.Know(self.MyKnow())
                    case "warrior":
                        print("No")
                    case "res":
                        print("oh my")
                    case _:
                        print("ERROR WTF THIS IS???????")


    def MyKnow(self):
        pass

    def Know(self):
        pass
