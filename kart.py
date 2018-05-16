a = int(input())
b = int(input())
c = int(input())
 
if (a > b and a > c):
          print("the largest number is: ",a)
elif (b > a and b > c):
          print("the largest number is: ",b)
elif (c > a and c > b):
          print("the largest number is: ",c)
else:
          print("all the three values are equal")