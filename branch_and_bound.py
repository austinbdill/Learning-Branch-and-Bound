import numpy as np
from collections import defaultdict

class Variable:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None
        
    def set_cluster(cluster):
        self.cluster = cluster
        
class Cluster:
    
    def __init__(self):
        self.center = None
        
    def set_center(center):
        self.center = center

def cluster_branch(points, k=5, depth_limit=None):
    variables = []
    clusters = defaultdict()
    for i in range(points.shape[0]):
        point = points[0]
        next_var = Variable(point[0], point[1])
    return clusters