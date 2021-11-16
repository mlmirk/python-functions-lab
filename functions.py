def sum_to():
  x=int(input('enter a number larger the 1 '))
  sum = 0
  for num in range(1,x):
    sum +=num
  print(sum)

#sum_to()


def largest_list(li):
  largest=li[0]
  for i in li:
    if largest < i:
      largest = i
  print(largest)

#largest_list([4,33,99,1])

def occurances(x,y):
  occ=x.count(y)
  print(occ)


occurances('epe', 'ee')

