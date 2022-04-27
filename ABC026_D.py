import io
import sys

_INPUT = """\
6
1 1 1
53 82 49
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import math
  A,B,C=map(int,input().split())
  def f(t):
    return A*t+B*math.sin(C*t*math.pi)
  l,r=0,1000
  for i in range(100):
    mid=(l+r)/2
    if f(mid)<100: l=mid
    else: r=mid
  print(l)