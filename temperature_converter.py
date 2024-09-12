def convert_temperature(temperature, unit):
  """Converts a temperature to Celsius or Fahrenheit.

  Args:
    temperature: The temperature value.
    unit: The unit of the temperature (either "C" for Celsius or "F" for Fahrenheit).

  Returns:
    The converted temperature.
  """

  if unit == "C":
    fahrenheit = (temperature * 9/5) + 32
    return fahrenheit
  elif unit == "F":
    celsius = (temperature - 32) * 5/9
    return celsius
  else:
    print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    return None

# Get the temperature and unit from the user
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ")

# Convert the temperature
converted_temperature = convert_temperature(temperature, unit)

# Print the result
if converted_temperature is not None:
  print("Converted temperature:", converted_temperature)