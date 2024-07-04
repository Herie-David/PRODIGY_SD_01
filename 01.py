# Converts temperature between Celsius, Fahrenheit, and Kelvin
def convert_temperature(value, unit):
  
  """
  Args:
      value: The temperature value to convert
      unit: The original unit of measurement (C, F, or K)
  
  """
  converted = {}
  if unit.upper() == "C":
    converted["Fahrenheit"] = (value * 9/5) + 32
    converted["Kelvin"] = value + 273.15
  elif unit.upper() == "F":
    converted["Celsius"] = (value - 32) * 5/9
    converted["Kelvin"] = (value - 32) * 5/9 + 273.15
  elif unit.upper() == "K":
    converted["Celsius"] = value - 273.15
    converted["Fahrenheit"] = (value - 273.15) * 9/5 + 32
  else:
    print("Invalid unit. Please enter 'C', 'F', or 'K'.")
    return None
  
  """
  Returns:
      A dictionary containing the converted temperatures in Celsius, Fahrenheit, and Kelvin
  
  """
  return converted

# Get user input
while True:
  try:
    value = float(input("Enter temperature value: "))
    unit = input("Enter unit (C, F, or K): ")
    break
  except ValueError:
    print("Invalid input. Please enter a number for temperature value.")

# Convert temperature
converted_values = convert_temperature(value, unit)

if converted_values:
  # Display results
  print(f"{value:.2f} degrees {unit} is equivalent to:")
  for unit, converted_value in converted_values.items():
    print(f"\t{converted_value:.2f} degrees {unit}")