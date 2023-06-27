import numpy as np
import tensorflow as tf
from skimage.morphology import binary_erosion
from skimage.morphology import disk
from skimage import img_as_ubyte
from skimage.filters.rank import entropy
import sklearn.mixture
from warnings import warn
import cv2
import maxflow
import matplotlib.pyplot as plt
import matplotlib as mpl



import numpy as np

from skimage.feature import blob_doh
from skimage.measure import regionprops
from sklearn.preprocessing import StandardScaler
from skimage.filters import gaussian


from numpy.lib.stride_tricks import as_strided


def graph_cut(data_img, prior = 0.8, max_weight = 2, sigma = 0.3):
  ''' A generic graph cut algorithm to separate foreground from background.
  data_img: either 2D or 3D numpy array
  prior: Prior probability of foreground pixels, float (0,1)
  max_weight: Max cut penalty. A smaller value resulted in more fragmented cutting
  sigma: Affects how much the intensity gradient lowers the cut penalty. A large value means low effect and thus a more constant cut penalty.

  returns: Graph cut image
  '''
  if prior <=0 or prior >= 1.0:
    raise ValueError("prior must be between (0,1)")

  dim = len(data_img.shape)
  if dim != 2 and dim !=3:
    raise ValueError("Input image should be 2D or 3D")

  img = (data_img - data_img.min()) / data_img.ptp()

  f_weights = -np.log(np.maximum(img, np.finfo(float).eps)) - np.log(prior)
  b_weights = -np.log(1.0-prior) - np.log(np.maximum(1.0 - img, np.finfo(float).eps))

  g = maxflow.GraphFloat()
  nodes = g.add_grid_nodes(img.shape)

  g.add_grid_tedges(nodes, f_weights, b_weights)

  if dim == 2:
    connectivities = ((-1,1), (0,1), (1,1), (1,0)) # 2D
    for c in connectivities:
      struct = np.zeros((3,3))
      struct[1+c[0], 1+c[1]] = 1
      weights = img - np.roll(img, -np.array(c), axis=(0,1))
      weights = np.exp(-weights*weights/2/sigma/sigma) * max_weight
      g.add_grid_edges(nodes, weights, struct)
  else:
    connectivities = ((0,-1,1), (0,0,1), (0,1,0), (0,1,1), (1,-1,-1), (1,-1,0), (1,-1,1), (1,0,-1), (1,0,0), (1,0,1), (1,1,-1), (1,1,0), (1,1,1)) # 3D
    for c in connectivities:
      struct = np.zeros((3,3,3))
      struct[1+c[0], 1+c[1], 1+c[2]] = 1
      weights = img - np.roll(img, -np.array(c), axis=(0,1,2))
      weights = np.exp(-weights*weights/2/sigma/sigma) * max_weight
      g.add_grid_edges(nodes, weights, struct)

  g.maxflow()
  sgm_img = g.get_grid_segments(nodes)
  sgm_img = (sgm_img * 255).astype(np.uint8)

  return sgm_img 

cv2.imwrite('test.png', graph_cut(cv2.imread('sp.png', 0)))




