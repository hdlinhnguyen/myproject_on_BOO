from math import inf

class bi_objective_priority_queue:
   def __init__(self):
       self.queue = []
       self.size = 0

   def insert(self, item):
       self.queue.append(item)
       self.size += 1
       self.sort_lex()

   def extract(self):
       if self.size == 0:
           return None
       else:
           self.size -= 1
           return self.queue.pop(0)

   def sort_lex(self):
       self.queue.sort(key=lambda x: (x[0], x[1]))

   def __len__(self):
       return self.size

   def __str__(self):
       return str(self.queue)

M = 50
C1 = [
  [inf, 4, 5, inf, inf, inf],
  [inf, inf, 2, 1, 2, 7],
  [inf, inf, inf, 5, 2, inf],
  [inf, inf, 5, inf, inf, 3],
  [inf, inf, inf, inf, inf, 4],
  [inf, inf, inf, inf, inf, inf],
]
C2 = [
  [inf, 3, 1, inf, inf, inf],
  [inf, inf, 1, 4, 2, 2],
  [inf, inf, inf, 1, 7, inf],
  [inf, inf, 1, inf, inf, 2],
  [inf, inf, inf, inf, inf, 2],
  [inf, inf, inf, inf, inf, inf],
]


def smaller_or_equal_lex(x, y):
   return x[0] <= y[0] or x[1] <= y[1]


def find_smallest_lex(D):
   smallest = D[0]
   for i in range(1, len(D)):
       if smaller_or_equal_lex(D[i], smallest):
           smallest = D[i]
   return smallest


def remove_duplicated(D):
   for vertex in D:
       D[vertex] = list(set(D[vertex]))
   return D


def bi_obj_shortest_path(C1, C2, s, t):
   """
   return all non dominated paths from s to t
   """
   n = len(C1)
   D = {vertex : [] for vertex in range(n)} #add the distances to the vertices on the two objectives and the previous vertex
   D[s] = [(0, 0, None)]
   Q = bi_objective_priority_queue()
   Q.insert((0, 0, s))
   while len(Q) > 0:
       (d1, d2, u) = Q.extract()
       for v in range(n): #for each neighbor of u


           if C1[u][v] != inf: #if there is an edge from u to v for the first objective
               if D[v] == [] or smaller_or_equal_lex((d1 + C1[u][v], d2 + C2[u][v]), find_smallest_lex(D[v])):
                   D[v] += [(d1 + C1[u][v], d2 + C2[u][v], u)]
                   Q.insert((d1 + C1[u][v], d2 + C2[u][v], v))
               elif D[v][0][0] == d1 + C1[u][v]:
                   D[v].append((d1 + C1[u][v], d2 + C2[u][v], u))


           if C2[u][v] != inf:
               if D[v] == [] or smaller_or_equal_lex((d1 + C1[u][v], d2 + C2[u][v]), find_smallest_lex(D[v])):
                   D[v] += [(d1 + C1[u][v], d2 + C2[u][v], u)]
                   Q.insert((d1 + C1[u][v], d2 + C2[u][v], v))
               elif D[v][0][1] == d2 + C2[u][v]:
                   D[v].append((d1 + C1[u][v], d2 + C2[u][v], u))


   return remove_duplicated(D)


print(bi_obj_shortest_path(C1, C2, 0, 5))

def retro_propagation(D, s, t):
   """
   return the all non dominated paths from s to t found bi bi_obj_shortest_path
   """
   def aux(u):
       if u == s:
           return [[s]]
       else:
           paths = []
           for (d1, d2, v) in D[u]:
               for path in aux(v):
                   paths.append(path + [u])
           return paths


   return aux(t)
