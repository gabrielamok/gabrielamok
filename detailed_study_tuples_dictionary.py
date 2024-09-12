def find_largest_number(numbers):
  """Finds the largest number in a list.

  Args:
    numbers: A list of numbers.

  Returns:
    The largest number in the list.
  """

  if not numbers:
    return None

  largest = numbers[0]
  for num in numbers:
    if num > largest:
      largest = num
  return largest

def store_student_info():
  """Stores student information in a dictionary.

  Returns:
    A dictionary containing student information.
  """

  students = []
  while True:
    name = input("Enter student name (or 'quit' to exit): ")
    if name.lower() == "quit":
      break

    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    student = {"name": name, "age": age, "grade": grade}
    students.append(student)

  return students

def main():
  # Find the largest number
  numbers = [12, 5, 34, 8, 27]
  largest_number = find_largest_number(numbers)
  print("Largest number:", largest_number)

  # Store student information
  students = store_student_info()
  print("Student information:")
  for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

if __name__ == "__main__":
  main()