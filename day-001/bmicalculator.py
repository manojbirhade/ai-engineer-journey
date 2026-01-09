#वक्रतुण्ड महाकाय, सूर्यकोटि समप्रभ ।, निर्विघ्नं कुरु मे देव, सर्वकार्येषु सर्वदा ॥
try:
 name = input("Enter your name: ")
 age = int(input("Enter your age: "))
 height_cm = float(input("Enter your height in cm: "))
 weight_kg = float(input("Enter your weight in kg: "))
 bmi = round((weight_kg) / ((height_cm) / 100) ** 2,2)
 if bmi < 18.5:
    print(f"Hello {name}, Your BMI is {bmi} and you are Underweight")
 elif bmi >= 18.5 and bmi <= 24.9:
    print(f"Hello {name}, Your BMI is {bmi} and you are Healthy")
 elif bmi >=25 and bmi <= 29.9:
    print (f"Hello {name}, yout BMI is {bmi} and you are Overweight")
 elif bmi >=30 and bmi <= 34.9:
    print (f"Hello {name}, yout BMI is {bmi} and you are Obese")
except (ValueError, TypeError) as vte:
    print(f"Value or Type Error: {vte} Enter a Valid Number/Numeric Value")
except Exception as e:
   print(f"An unexpected Error Occurred: {e}")
    