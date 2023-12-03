calibration_values = []

# Read in lines to list
infile = open("01_trebuchet/input.txt", "r")
for calibration in infile:
  calibration_values.append(calibration.strip()) # Ensures no newline characters
infile.close()

# Clean up list entries (remove non-numbers)
calibration_values_clean = []
allowed_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

for value in calibration_values:
  clean_value = ""
  for character in value:
    if character in allowed_values:
      clean_value += character
  calibration_values_clean.append(clean_value)

print(calibration_values_clean)

# Get rid of unwanted numbers, expand single digits to two-digit numbers
true_calibration_values = []

for value in calibration_values_clean:
  true_value = ""
  if len(value) == 1:
    true_value = value * 2
  elif len(value) > 1:
    true_value += value[0]
    true_value += value[-1]
  true_calibration_values.append(true_value)

# Convert string values to int values
int_values = [int(num) for num in true_calibration_values]

# Sum all calibration values
print("Sum of Calibration Values: ", sum(int_values))
