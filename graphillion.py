# 必要なモジュールのインポート
from graphillion import GraphSet
import graphillion.tutorial as tl

# グリッドのサイズを指定
from reportlab import xrange

universe = tl.grid(2, 2)
GraphSet.set_universe(universe)
# tl.draw(universe)

# 経路が何本あるのか?
start = 1  # スタート位置
goal = 9  # ゴールの位置
paths = GraphSet.paths(start, goal)
print(len(paths))  # 12通り

# 指定された２箇所を指定された順番で通る」という制約付きで道順が何通りあるか
key = 4  # 1箇所目
treasure = 2  # 2箇所目
paths_to_key = GraphSet.paths(start, key).excluding(treasure)
treasure_paths = paths.including(paths_to_key).including(treasure)
print("１回目")
print(len(treasure_paths))

import time  # 計算時間を調べる。

universe = tl.grid(8, 8)
GraphSet.set_universe(universe)
# tl.draw( universe )
start = 1
goal = 81
s = time.time()  # 計算開始時刻
paths = GraphSet.paths(start, goal)
print(time.time() - s)  # 計測時間

# len( paths )
print(len(paths))

# for path in paths:
#tl.draw(paths.choice())

key = 64
treasure = 18
paths_to_key = GraphSet.paths(start, key).excluding(treasure)
treasure_paths = paths.including(paths_to_key).including(treasure)
print(len(treasure_paths))

print("----------------↓？----------------")
#tl.draw(treasure_paths.choice())

print(treasure_paths < paths)

i = 0
data = []
for path in treasure_paths.rand_iter():
    data.append(tl.how_many_turns(path))  # count the number of turns on the path
    if i == 100: break
    i += 1
...
#tl.hist(data)

for path in treasure_paths.min_iter():
    print(tl.how_many_turns(path))

    break

# 配電ネットワーク上の電力の流れ
universe = tl.grid(8, 8, 0.37)  # 37 % of edges are randomly removed from 8x8 grid
GraphSet.set_universe(universe)
generators = [1, 9, 73, 81]
#tl.draw(universe)

forests = GraphSet.forests(roots=generators, is_spanning=True)  # a forest represents a power flow covering all houses without loop
print( len(forests) ) #54060425088
#tl.draw(forests.choice())

too_large_trees = GraphSet()
for substation in generators:
    too_large_trees |= GraphSet.trees(root=substation).larger(23)

safe_forests = forests.excluding(too_large_trees)
print( len(safe_forests))
#tl.draw(safe_forests.choice())

closed_switches = (forests - safe_forests).choice()
#tl.draw(closed_switches)

scores = {}  # scores for closed switches in the new configuration (default is 0)
for switch in universe:
    # if current status is closed then the score is 1, else -1
   scores[switch] = 1 if switch in closed_switches else -1
...
for forest in safe_forests.max_iter(scores):
    #tl.draw(forest)
    break  # if not break, multiple configs are yielded from the highest score
...
failures = safe_forests.blocking().minimal()  # a set of all minimal blocking sets
failure = failures.choice()  # a hitting set (a set of critical power lines)
for line in failure:
    safe_forests = safe_forests.excluding(line)  # remove a line in the hitting set
...
print ( len(safe_forests) ) #0

print( (failures.smaller(5)) ) #767


# Creating graphsets
from graphillion import GraphSet
universe = [(1, 2), (1, 4), (2, 3), (2, 5), (3, 6), (4, 5), (5, 6)]
GraphSet.set_universe(universe)

graph1 = [(1, 4)]
graph2 = [(1, 2), (2, 3)]
gs = GraphSet([graph1, graph2])
print (gs)

gs = GraphSet()
print (gs)


#Edge constraints エッジの制約
edges1 = [(1, 4)]
edges2 = [(1, 2), (2, 3)]
GraphSet({'include': edges1, 'exclude':edges2})
#GraphSet([[(1, 4)], [(1, 4), (2, 5)], [(1, 4), (3, 6)], ...

gs = GraphSet({})
print( len(gs) ) # 2^7

start = 1
end = 6
zero_or_two = xrange(0, 3, 2)
degree_constraints = {start: 1, end: 1,
                      2: zero_or_two, 3: zero_or_two,
                      4: zero_or_two, 5: zero_or_two}
print ( GraphSet.graphs(vertex_groups=[[start, end]],
                degree_constraints=degree_constraints,
                no_loop=True) )
# GraphSet([[(1, 2), (2, 3), (3, 6)], [(1, 2), (2, 5), (5, 6)], [(1, 4), (4, 5 ...


# NetworkXの操作
import networkx as nx
# for NetworkX version 1.x
GraphSet.converters['to_graph'] = nx.Graph
GraphSet.converters['to_edges'] = nx.Graph.edges
# for NetworkX version 2.x
GraphSet.converters['to_graph'] = nx.from_edgelist
GraphSet.converters['to_edges'] = nx.to_edgelist

g = nx.Graph()  # create a graph by NetworkX
GraphSet.set_universe(g)

gs.choice()  # return a NeworkX's graph object
#<networkx.classes.graph.Graph object at 0x100456d10>

nx.draw(gs.choice())
import matplotlib.pyplot as plt
plt.show()  # show a pop-up window
