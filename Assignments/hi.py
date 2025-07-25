def table(**kwargs):
  return [kwargs['num']* i for i in range(1,11)]
  
num=int(input())
print(table(num=num))