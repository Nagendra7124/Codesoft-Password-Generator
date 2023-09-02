import random
import string

def generate_password(length):
    
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    
    all_characters = ""
    while True:
        complexity = input("Enter complexity (low, medium, high): ").lower()
        if complexity == "Low":
            all_characters = lower_letters + digits
            break
        elif complexity == "Medium":
            all_characters = lower_letters + upper_letters + digits
            break
        elif complexity == "High":
            all_characters = lower_letters + upper_letters + digits + special_characters
            break
        else:
            print("Invalid complexity level. Choose from low, medium, or high.")

    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        print(input("Enter the User Name:-"))
        length = int(input("Enter the desired length of the password:- "))
        password = generate_password(length)
        print("Generated Password:-", password)
    except ValueError:
        print("Invalid input.")
        print("Please enter a valid length (an integer).")
