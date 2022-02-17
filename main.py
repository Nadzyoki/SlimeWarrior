from ursina import *
from Hero.Skeleton.Skelet import Player


class Main(Ursina):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.castel = load_blender_scene('castel', reload=True)
        for e in self.castel.children:
            e.collider = 'mesh'



if __name__ == '__main__':
    app = Main()
    app.run()
