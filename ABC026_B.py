import io
import sys

_INPUT = """\
6
3
1
2
3
6
15
2
3
7
6
9
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  import math
  N=int(input())
  R=[int(input()) for _ in range(N)]
  R.sort(reverse=True)
  ans=0
  for i in range((N+1)//2):
    ans+=R[2*i]**2*math.pi
    if 2*i+1<N:
      ans-=R[2*i+1]**2*math.pi
  print(ans)