def check_grade(score):
  """Checks the grade based on the given score.

  Args:
    score: The student's score.

  Returns:
    The corresponding grade.
  """

  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
## def is the way to declare a function
# Get the student's score
score = float(input("Enter the student's score: "))

# Check the grade and print the result
grade = check_grade(score)
print("Grade:", grade)