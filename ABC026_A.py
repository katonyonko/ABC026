import io
import sys

_INPUT = """\
6
10
60
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A=int(input())
  ans=0
  for x in range(1,A):
    ans=max(ans,x*(A-x))
  print(ans)