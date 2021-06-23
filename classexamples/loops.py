myints = [3, 4, 7, 9]
for i in myints:
  print(i*2)
print('\n')

student = "Raga"
for x in student:
  print(x,end="")
print('\n')

for i in range(2,15,3):
  print(i, end=" ")


grocery = ['bread', 'milk', 'butter']
print('\n')
for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

for count, item in enumerate(grocery, 100):
  print(count, item)
print('\n')


#homework 06/22

#Create a for loop that prints off the numbers 89, 41, 73, and 90 - each on their own line
for i in [89, 41, 73, 90]:
  print(i)
print('\n')

#Create a for loop that prints off the numbers 5 up-to but not including 15
for i in range (5,15):
  print(i)
print('\n')

#Create a for loop that prints off the numbers 100 to 200 by 10's
for i in range(100,210,10):
  print(i)
print('\n')

#Create a for loop that prints off the numbers from 80 to 32 by 8's
for i in range(80,31,-8):
  print(i)
print('\n')

#Create a for loop that prints off the word Alright three times.
for i in range(3):
  print("Alright", end=" ")
print('\n')

#Using range, create a for loop that prints off the numbers 1, 4, 9, 16.
for i in range(1,5):
  print(i**2)