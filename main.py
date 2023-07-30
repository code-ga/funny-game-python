from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from perlin_noise import PerlinNoise
import random

app = Ursina()

grass = "grass.png"
player = FirstPersonController()
Sky()

deepest = -10


class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass):
        super().__init__(
            model="cube",
            texture=texture,
            color=color.color(0, 0, random.uniform(0.823, 0.984)),
            parent=scene,
            position=position,
        )

    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                Voxel(position=self.position + mouse.normal)

            if key == "left mouse down":
                # deepest is -10
                if self.position.y <= deepest:
                    return
                else:
                    Voxel(position=self.position - (0, 1, 0))
                    destroy(self)


noise = PerlinNoise(octaves=20, seed=random.randint(1, 1000000))
print(noise)

for z in range(-20, 20):
    for x in range(-20, 20):
        y = noise([x *0.02, z * 0.02])
        y = math.floor(y * 7.5)
        voxel = Voxel(position=(x, y, z))

app.run()
