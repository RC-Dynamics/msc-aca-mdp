import numpy as np

width = 4
height = 3

def create_spec_pos():
    spec_pos = []
    spec_pos.append(((0,3), 1))
    spec_pos.append(((1,1), -0.5))
    spec_pos.append(((1,3), -1))
    spec_pos.append(((2,3), 0.2))
    return spec_pos

def create_world(h, w, spc_pos):
    w = np.zeros((h, w))
    for p in spc_pos:
        w[p[0][0]][p[0][1]] = p[1]
    return w

if __name__ == "__main__":
    world = create_world(3, 4, create_spec_pos())
    print(world)