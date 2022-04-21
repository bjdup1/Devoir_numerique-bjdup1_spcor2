from dataclasses import field
import env_examples  # Modifies path, DO NOT REMOVE
import numpy as np
from src import Circuit, Current, Wire, World, fields



if __name__ == "__main__":
    
    # Boucle a)
    world = World(shape=(80, 80))
    wires = [
        Wire(start=(15, 15), stop=(40, 15), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(40, 15), stop=(65, 15), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(65, 15), stop=(65, 65), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(65, 65), stop=(40, 65), current=Current(x=1, y=0), voltage=-4.5),
        Wire(start=(40, 65), stop=(15, 65), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(15, 65), stop=(15, 15), current=Current(x=0, y=1), voltage=4.5),
    ]

    # Boucle b)
    """world = World(shape=(80, 80))
    wires = [
        Wire(start=(15, 15), stop=(65, 15), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(65, 15), stop=(65, 65), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(65, 65), stop=(15, 65), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(15, 65), stop=(15, 15), current=Current(x=0, y=1), voltage=4.5),
    ]"""

    # Boucle c)
    """world = World(shape=(130, 80))
    wires = [
        Wire(start=(15, 15), stop=(115, 15), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(115, 15), stop=(115, 65), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(115, 65), stop=(15, 65), current=Current(x=1, y=0), voltage=4.5),
        Wire(start=(15, 65), stop=(15, 15), current=Current(x=0, y=1), voltage=4.5),
    ]"""

    # Boucle d) coeur
    """world = World(shape=(110, 100))
    wires = [
        Wire(start=(55, 15), stop=(50, 15), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(50, 15), stop=(50, 20), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(50, 20), stop=(45, 20), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(45, 20), stop=(45, 25), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(45, 25), stop=(40, 25), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(40, 25), stop=(40, 30), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(40, 30), stop=(35, 30), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(35, 30), stop=(35, 35), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(35, 35), stop=(30, 35), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(30, 35), stop=(30, 40), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(30, 40), stop=(25, 40), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(25, 40), stop=(25, 45), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(25, 45), stop=(20, 45), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(20, 45), stop=(20, 50), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(20, 50), stop=(20, 55), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(20, 55), stop=(15, 55), current=Current(x=-1, y=0), voltage=4.5),
        Wire(start=(15, 55), stop=(15, 60), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(15, 60), stop=(15, 65), current=Current(x=0, y=1), voltage=4.5),
        Wire(start=(15, 65), stop=(15, 70), current=Current(x=0, y=1), voltage=4.5),

        Wire(start=(15, 70), stop=(20, 70), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(20, 70), stop=(20, 75), current=Current(x=0, y=1), voltage=1.5),
        Wire(start=(20, 75), stop=(25, 75), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(25, 75), stop=(25, 80), current=Current(x=0, y=1), voltage=1.5),
        Wire(start=(25, 80), stop=(30, 80), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(30, 80), stop=(30, 85), current=Current(x=0, y=1), voltage=1.5),
        Wire(start=(30, 85), stop=(35, 85), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(35, 85), stop=(40, 85), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(40, 85), stop=(45, 85), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(45, 85), stop=(45, 80), current=Current(x=0, y=-1), voltage=1.5),
        Wire(start=(45, 80), stop=(50, 80), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(50, 80), stop=(50, 75), current=Current(x=0, y=-1), voltage=1.5),
        Wire(start=(50, 75), stop=(55, 75), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(55, 75), stop=(60, 75), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(60, 75), stop=(60, 80), current=Current(x=0, y=1), voltage=1.5),
        Wire(start=(60, 80), stop=(65, 80), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(65, 80), stop=(65, 85), current=Current(x=0, y=1), voltage=1.5),
        Wire(start=(65, 85), stop=(70, 85), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(70, 85), stop=(75, 85), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(75, 85), stop=(80, 85), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(80, 85), stop=(80, 80), current=Current(x=0, y=-1), voltage=1.5),
        Wire(start=(80, 80), stop=(85, 80), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(85, 80), stop=(85, 75), current=Current(x=0, y=-1), voltage=1.5),
        Wire(start=(85, 75), stop=(90, 75), current=Current(x=1, y=0), voltage=1.5),
        Wire(start=(90, 75), stop=(90, 70), current=Current(x=0, y=-1), voltage=1.5),
        Wire(start=(90, 70), stop=(95, 70), current=Current(x=1, y=0), voltage=1.5),

        Wire(start=(95, 70), stop=(95, 65), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(95, 65), stop=(95, 60), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(95, 60), stop=(95, 55), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(95, 55), stop=(90, 55), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(90, 55), stop=(90, 50), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(90, 50), stop=(90, 45), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(90, 45), stop=(85, 45), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(85, 45), stop=(85, 40), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(85, 40), stop=(80, 40), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(80, 40), stop=(80, 35), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(80, 35), stop=(75, 35), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(75, 35), stop=(75, 30), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(75, 30), stop=(70, 30), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(70, 30), stop=(70, 25), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(70, 25), stop=(65, 25), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(65, 25), stop=(65, 20), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(65, 20), stop=(60, 20), current=Current(x=-1, y=0), voltage=-4.5),
        Wire(start=(60, 20), stop=(60, 15), current=Current(x=0, y=-1), voltage=-4.5),
        Wire(start=(60, 15), stop=(55, 15), current=Current(x=-1, y=0), voltage=-4.5),
    ]"""

    circuit = Circuit(wires=wires)
    world.place(circuit)
    world.compute(10000)
    world.show_all()
