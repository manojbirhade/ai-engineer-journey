#वक्रतुण्ड महाकाय, सूर्यकोटि समप्रभ ।, निर्विघ्नं कुरु मे देव, सर्वकार्येषु सर्वदा ॥

name = input("Hi, What's your Name: ")
print()
print(f"Hello {name}, Welcome to our Mood Based Recommendation Engine", end="\n\n")

try:
 mood = input(f"So {name}, How are you feeling today?: ")
 mood = mood.lower().strip()

 match mood:
  case "sad":
   print("Help Someone in Need")
  case "bored":
   print("Challenge Yourself")
  case "happy":
   print("Celebrate")
  case "anxious":
   print("Go for a Walk or Hike")
  case "tired":
   print("Take a Hot Shower & Drink Hot Chocolate Milk")
  case "angry":
   print("Take Deep Breaths")
  case _:
   print("Unknown Mood")
  
except (TypeError, ValueError) as tve:
  print("Please Enter Proper Values")

