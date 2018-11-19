import numpy as np
import queue

class Variable:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cluster = None
        
    def __str__(self):
        return str((self.x, self.y))
        
    def set_cluster(self, cluster):
        self.cluster = cluster
        
class Cluster:
    
    def __init__(self):
        self.center = None
        self.points = []
        
    def calc_center(self):
        x = np.mean([i.x for i in self.points])
        y = np.mean([i.y for i in self.points])
        self.center = (x, y)
        
    def add_point(self, point):
        self.points.append(point)
        
    def reset_points(self):
        self.points = []
        
def next_variable(variables, method="naive"):
    if len(variables) == 0:
        return None
    if method == 'naive':
        return variables[0]
    else:
        return None
    
def cost():
    cost = 0
    return cost
        
def cluster_branch(points, k=5, depth_limit=-1):
    
    #Initialize variable objects
    variables = []
    for i in range(points.shape[0]):
        point = points[i]
        next_var = Variable(point[0], point[1])
        variables.append(next_var)
        
   #Initialize clutser objects
    clusters = []
    for i in range(k):
        clusters.append(Cluster())
    
    #Initialize helper variables
    n_recurs = 0
    q = queue.Queue()
    q.put(next_variable(variables))
    possible_cluster = dict()
    for var in variables:
        cluster_list 
    
    
    #Clustering Loop
    while (n_recurs != depth_limit and not q.empty()):
        print(q.get())
        
        n_recurs = n_recurs + 1
        
    return clusters