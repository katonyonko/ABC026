import io
import sys

_INPUT = """\
6
5
1
1
1
1
7
1
1
2
2
3
3
6
1
2
3
3
2
10
1
2
3
4
5
6
7
8
9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import sys
  sys.setrecursionlimit(1000000)
  N=int(input())
  G=[[] for _ in range(N)]
  for i in range(N-1):
    B=int(input())
    G[B-1].append(i+1)
  minmax=[-1 for _ in range(N)]
  def rec(k):
    if minmax[k]!=-1: return minmax[k]
    minmax[k]=1
    tmpmin,tmpmax=10**20,0
    if len(G[k])>0:
      for v in G[k]:
        tmpmin=min(tmpmin,rec(v))
        tmpmax=max(tmpmax,rec(v))
      minmax[k]+=tmpmin+tmpmax
    return minmax[k]
  print(rec(0))