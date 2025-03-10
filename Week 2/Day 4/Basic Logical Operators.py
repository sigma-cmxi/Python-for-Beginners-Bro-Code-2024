age = int(input("Enter your age: "))  
citizenship = input("Are you American? (Y or N): ").strip().upper()  

if age >= 18 and citizenship == "Y":  
    print("You can vote")  
else:  
    print("You cannot vote")  
