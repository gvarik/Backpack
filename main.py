''''Выведите максимальную стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
 помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.'''

import sys
import heapq


def knapsack(capacity, weights):
    order=[(-v/w,w) for v,w in weights]
    heapq.heapify(order)

    acc=0

    while order and capacity:
        vperw,w = heapq.heappop(order)
        can_take=min (w,capacity)
        acc-=vperw*can_take
        capacity-=can_take

    return acc


reader = (tuple(map(int,line.split())) for line in sys.stdin)
n, capacity = next(reader)
weights=list(reader)
assert len(weights)==n
optvalue=knapsack(capacity,weights)
print('{:.3f}'.format(optvalue))