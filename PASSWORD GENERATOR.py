import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("SIMPLE PYTHON PASSWORD GENERATOR")

    while True:
        input_length = input("Enter the desired length of the password: ")

        if input_length.isdigit() and int(input_length) > 0:
            length = int(input_length)
            break
        else:
            print("Invalid input. Please enter a positive integer for the length.")

    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
