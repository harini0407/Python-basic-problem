# Lambda function to square a number
sq=lambda x:x**2

print(sq(2))

# Lambda function to add two numbers
add=lambda x,y:x+y

# Test
print(add(5, 3))  # Expected output: 8
print(add(10, 20))  # Expected output: 30

# Lambda function to check even or odd
even_or_odd=lambda x: "Even" if x%2==0 else "Odd"

# Test
print(even_or_odd(10))  # Expected output: Even
print(even_or_odd(11))  # Expected output: Odd

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Filter even numbers
evens = list(filter(lambda x:x%2==0,numbers))

print(list(evens))  # Expected output: [2, 4, 6, 8]

students = [("John", 85), ("Emma", 92), ("Chris", 78)]

# Sort by score
sorted_students = sorted(students,key=lambda x: x[1])

print(sorted_students)  

numbers = [1, 2, 3, 4, 5]

# Double the numbers
doubled =map(lambda x:x*2,numbers)

print(list(doubled))  # Expected output: [2, 4, 6, 8, 10]