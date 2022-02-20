def BMI(height, weight): 
  bmi = weight / (height**2) 
  return bmi

height = 1.66
weight = 57

bmi = BMI(height, weight)

print("The BMI is " + str(round(bmi, 2)))

if (bmi < 18.5): 
  print("Underweight") 
elif ( bmi >= 18.5 and bmi < 24.9): 
  print("Healthy") 
elif ( bmi >= 24.9 and bmi < 30): 
  print("Overweight") 
elif ( bmi >=30): 
  print("Suffering from Obesity")