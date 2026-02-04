for _ in range(int(input())):
  n = int(input())
  a = list(map(str, input().split()))

  s = ""
  for i in range(n):
     s = min(a[i] + s, s + a[i])
  print(s)
   



    



    


  


