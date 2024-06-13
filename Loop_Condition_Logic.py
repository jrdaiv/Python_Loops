# Task 1

# write a while loop with condition that will never be true(infinite loop)
# ask user a question until their answer triggers a break
# is an if statement to evaluate answer

while True:
    user_input = input("How's Your Day? ")
    if user_input == "great":
       print("Great to hear, so am I !! ")
    elif user_input == "bad":
        print("Sucks to hear, hope it gets better! ")
        break
# else:
#     print("thanks for answering, loop is now terminated :)")


# Task 2

candy = 1  
while candy <= 5:
    print(f"candy {candy}")
    candy += 1  

print("Loop terminated. I have 5 candies! ")



