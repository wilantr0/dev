n = int(input())
x = 0
list = []
counter = 0
if n % 2 == 0:
  x = int(n/2)
  list.append(str(n))
  list.append(str(x))
elif n % 2 != 0:
  x = int((n*3)+1)
  list.append(str(n))
  list.append(str(x))

while x>1:
  if x % 2 == 0:
    x = int(x/2)
    list.append(str(x))
    pass
  elif x % 2 != 0:
    x = int((x*3)+1)
    list.append(str(x))
    pass


  counter+=1
  n-=1


print(' -> '.join(list) + f' [{counter+1}]')