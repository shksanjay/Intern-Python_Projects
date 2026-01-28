import random 

subjects =[
    "Elon Musk",
    "Balendra shah",
    "Kp Oli",
    "Ronaldo",
    "Mahesh Basnet",
    "Rajesh Hamal"
    
]
actions =[
    "launches",
    "dancels",
    "declares war",
    "orders",
    "celebrates",
    "invites",
    "calls",
    "fights"
]

places_or_things=[
    "at baluwatar",
    "in new road",
    "during NPL match",
    "a plate of momo", 
    "outside college",
    "at koteshwor",
  
]

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)
    
    headline=f"BREAKING NEWS:{subject} {action} {place_or_thing}"
    print('\n'+ headline)
    
    user_input=input("\nDo you want another headline?{yes/no}:").strip().lower()
    if user_input=="no":
        break

print("\n Thanks for using Fake News headline generator ")
