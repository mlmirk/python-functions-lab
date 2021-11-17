




def sum_to():
  x=int(input('enter a number larger the 1 '))
  sum = 0
  for num in range(1,x+1):
    sum +=num
  return sum

#sum_to()


def largest_list(li):
  largest=li[0]
  for i in li:
    if largest < i:
      largest = i
  return largest

#largest_list([4,33,99,1])

def occurances(x,y):
  return x.count(y)
  


#occurances('pepe', 'e')

def product(*args):
  product=1
  for arg in args:
    product*= arg
  return product

#product(2,3,1.5)
def main():
  print(sum_to())
  print(largest_list([4,33,99,1]))
  print(occurances('pepe', 'e'))
  print(product(2,3,1.5))

    
if __name__ == "__main__":
  main()