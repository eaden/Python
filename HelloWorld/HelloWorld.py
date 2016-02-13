# cin cout + string cast, string methods + math
print("Please type in your last name")
p = input()
p = p.lower()
p = p.capitalize()
print("Your last name is " + p)
print("Please type in a number that will be calculated by the power of 3")
p = int(input())
p = p**3
string = "The calculated number is {}".format(p)
print(string)
input()