print("What's your problem ?\n")
problem = input()
print("Have you had this problem before (yes or no)")
answer = input()
if answer == "yes":
    print("Well, you have it again")
elif answer == "no":
    print("Well, you have it now")
else:
    print("kindly input yes or no")
