t = int(input())
for i in range(t):
  n , k = map(int , input().split())
  arr = list( map(int , input().split()))
  x = 0
  for i in range(len(arr)):
     if (k - x) in arr:
       x += 1
  print(x)


  
