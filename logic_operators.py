def check_age(age):
  """Checks if the given age is valid for voting.

  Args:
    age: The person's age.

  Returns:
    True if the age is valid for voting, False otherwise.
  """

  if age >= 18 and age <= 65:
    return True
  else:
    return False

# Get the person's age
age = int(input("Enter your age: "))

# Check if the age is valid for voting
if check_age(age):
  print("You are eligible to vote.")
else:
  print("You are not eligible to vote.")