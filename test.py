# Handling invalid input example
# With Valid Integer

# try:
#     result = int(input("enter a numer"))
# except ValueError:
#     result=0
#     print("input is not a number")

x= input("Choose Row where you want to put your bet:")
# x = None
row =int( x or 4)
print(row)
