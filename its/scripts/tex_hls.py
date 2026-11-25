"""Small textures shared by the parts: lamp masks and the plain steel."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, tl, hls_layout as HL
from texcommon import line, cells, hash2
W = int(os.environ.get('ITS_HULL', 4096))


def noise(seed, base, o=4):
    return np.kron(tl._fbm(W // 2, W // 2, seed, base=base, octaves=o), np.ones((2, 2), np.float32))


import its_lamp

g = np.zeros((512, 512, 4), np.uint8); g[..., :3] = 203; g[..., 3] = np.clip(190 + 10 * tl._fbm(512, 512, 5, base=6, octaves=4), 0, 255); tl.write_dds(g, 'stms_steel_diff')      # the ship's steel: SEP's average colour and smoothness
g[...] = (255, 255, 0, 255); tl.write_dds(g[:64, :64].copy(), 'stms_steelmask_diff'); g[...] = (255, 128, 128, 128); tl.write_dds(g[:64, :64].copy(), 'stms_steel_nrm')
