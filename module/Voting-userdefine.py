from Voting import Voting

a = int(input("Enter your age : "))

v = Voting()

print("You are", v.eligibility(a))