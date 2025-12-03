# Caesar Cipher Encrypter

def caesar_cipher(message, shift):
    # This function will encrypt the user input message to Caesar Cipher.
    # First create a list of all alphabets.
    alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Turn the message string into a list.
    message = list(message)

    # Initilizing the final encrypted message list.
    final_msg = []

    # If shift is negative, shift to the left. If shift is positive, shift to the right.
    # Run a for loop to encrypt each character in the input message.
    for i in message:
        # Make sure to ignore spaces, punctuations, and special characters.
        if i not in alpha_list:
            final_msg.append(i)
        else:
            # Get the index of each character in the input message in the alpha_list to be able to shift right or left.
            c_ind = alpha_list.index(i)
            
            # Make sure that index does not go out of range. If it goes beyond range, it should circle back to the beginning or the end of the alpha_list.
            c_ind_sh = c_ind + shift
            if c_ind_sh > 25:
                # Run a loop to make sure the index value circles around until within alphabet index limits.
                while c_ind_sh > 25:
                    c_ind_sh = c_ind_sh - 26
                final_msg.append(alpha_list[c_ind_sh])
            elif c_ind_sh < 0:
                # Run a loop to make sure the index value circles around until within alphabet index limits.
                while c_ind_sh < 0:
                    c_ind_sh = c_ind_sh + 26
                final_msg.append(alpha_list[c_ind_sh])
            else:
                # If already within alphabet index limits, no need to circle around.
                final_msg.append(alpha_list[c_ind_sh])

    # Convert the final encrypted message into a string.
    final_msg = ''.join(final_msg)

    return final_msg

def main():
    # The main function
    # Inputfield for the user to enter the message. Make the message into all lower case.
    msg_input = input("Enter the message that you'd like to encrypt: ")
    msg_input = msg_input.lower()

    try:
        # Inputfield for the user to enter the amount of shift. Make sure value is a positive integer.
        shift_input = int(input("Enter the shift value (value must be an integer): "))

        # Call the caesar_cipher() function to encrypt the input message.
        result = caesar_cipher(msg_input, shift_input)

    # If input is not an integer, throw error message and end the program.
    except ValueError:
        result = "Invalid input. Please adhere to the rules. Ending program..."

    return result

if __name__ == "__main__":
    result = main()
    print("Your Caesar Cipher encrypted message is: " + result)