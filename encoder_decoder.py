# Encode and main function created by Mathew Santana.

def encode(password): # Encodes the passwords
    if len(password) != 8 or not password.isdigit():
        return "Issue"

    encoded_password = ''

    for digit in password:
        encoded_password += str((int(digit) + 3) % 10)

    return encoded_password


def decode(password):
    # TODO: Implement implement decode functionality (Comment can be deleted)
    pass


def print_menu(): # Prints the menu that displays options for the user to select
    print("\nMenu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")


def main():

    stored_password = None
    continue_program = True
    while continue_program:

        print_menu() # Calls a function to print the menu

        menu_selection = int(input("Please enter an option: "))

        if menu_selection == 1: # Encodes password
            password = input("Please enter your password to encode: ")
            # Calls the encode function using the password the user inputted as the parameter.
            encoded_password = encode(password)

            if encoded_password == "Issue":
                print("Password must be an 8-digit password containing only integers")
                continue
            else:
                # Stores the encoded password in the stored_password variable
                stored_password = encoded_password
                print("Your password has been encoded and stored!")

        elif menu_selection == 2: # Decodes password
            if stored_password is None:
                print("No password has been encoded yet.")
                continue
            else:
                # Calls decode function using the stored encoded password as the parameter.
                decoded_password = decode(stored_password)
                print(f"The encoded password is {stored_password}, and the original password is {decoded_password}")

        elif menu_selection == 3: # Exits program
            break

        else:
            print("Error!")
            continue


if __name__ == '__main__':
    main()