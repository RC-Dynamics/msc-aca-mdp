import numpy as np

width = 4
height = 3
r_s = [-0.4, -0.04, -0.004]

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
    spec_pos = create_spec_pos()
    world = create_world(height, width, spec_pos)
    print(world)