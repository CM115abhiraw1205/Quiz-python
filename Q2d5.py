# Define constants for the colors red, blue, and yellow.
red = "red"
blue = "blue"
yellow = "yellow"

# Get input from the user for the first and second colors.
color1 = input("Enter the first color: ")
color2 = input("Enter the second color: ")

# Check if the first color input is valid.
if color1 not in [red, blue, yellow]:
    print("Error: Invalid Color1.")

# Check if the second color input is valid.
elif color2 not in [red, blue, yellow]:
    print("Error: Invalid Color2.")

# Check if both colors are the same.
elif color1 == color2:
    print("Error: The two colors you entered are same")

# If both colors are different, determine the result color.
else:
    if color1 == red:
        if color2 == blue:
            print("Purple")
        elif color2 == yellow:
            print("Orange")
    elif color1 == blue:
        if color2 == red:
            print("Purple")
        elif color2 == yellow:
            print("Green")
    elif color1 == yellow:
        if color2 == red:
            print("Orange")
        elif color2 == blue:
            print("Green")
