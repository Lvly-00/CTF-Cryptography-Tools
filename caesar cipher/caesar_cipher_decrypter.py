# Caesar Cipher Decrypter using Al-Kindi's Frequency Analyzer
import string

def decrypt(msg):
    # This is the decrypting function.
    # Initializing variables.
    msg_dict = {}
    d_msg_f = []
    possible_shift = []
    alphabet = string.ascii_lowercase
    
    # Organizing freqeuncy of letters into a dictionary.
    freq_dict = {
        'e': 12.7,
        't': 9.1,
        'a': 8.2,
        'o': 7.5,
        'i': 7.0,
        'n': 6.7,
        's': 6.3,
        'h': 6.1,
        'r': 6.0,
        'd': 4.3,
        'l': 4.0,
        'c': 2.8,
        'u': 2.8,
        'm': 2.4,
        'w': 2.4,
        'f': 2.2,
        'g': 2.0,
        'y': 2.0,
        'p': 1.9,
        'b': 1.5,
        'v': 1.0,
        'k': 0.8,
        'j': 0.15,
        'x': 0.15,
        'q': 0.1,
        'z': 0.07
    }

    # Make the message all lower cased.
    msg = msg.lower()

    # Counting the frequency of letters in the orginial encrypted message and organizing them in a dictionary.
    for i in freq_dict.keys():
        count = 0
        for j in msg:
            if i == j:
                count += 1
            else:
                continue   
        msg_dict[i] = count

    # Sorting the msg_dict by the values from greatest to smallest to align with the freq_dict values.
    msg_dict = dict(sorted(msg_dict.items(), key=lambda x: x[1], reverse=True))

    print("\nFrequency of each letter in the encrypted message: ")
    print(msg_dict)
    print("")

    # Create lists for the keys of both msg_dict and freq_dict to keep it in order and identify index.
    # freq_list shows the letters in the order of most common to least common from the frequency table.
    # msg_list shows the letters in the order of the most common to the least common from the original encrypted message.
    freq_list = list(freq_dict.keys())
    msg_list = list(msg_dict.keys())

    # Find the shift between the most common letters e and t (from freq_list) and the top 2 most common letters from the original encrypted message (from msg_list).
    # Each of the top 2 most common letters will be examined to see how much they shifted from the e and t.
    x = alphabet.index(freq_list[0])
    y = alphabet.index(msg_list[0])
    z = alphabet.index(freq_list[1])
    w = alphabet.index(msg_list[1])

    # The below algorithm is based on the assumption that the most common letter in the original encrypted text (from msg_list) is either e or t, which are the 2 most common letters from the frequency table (from freq_list).
    # Performing operations to find the shift from most common letter in msg_list to e (most common letter from freq_list).
    # Performing operations to find the shift from most common letter in msg_list to t (2nd most common letter from freq_list).
    # Performing operations to find the shift from 2nd most common letter in msg_list to e.
    # Performing operations to find the shift from 2nd most common letter in msg_list to t.
    # The direction is determined with respect to e and t.
    # The result of each case is stored in possible_shift list.
    if y > x:
        diff_1 = y - x
        possible_shift.append(diff_1)
        possible_shift.append("right")
    elif y < x:
        diff_1 = x - y
        possible_shift.append(diff_1)
        possible_shift.append("left")
    else:
        diff_1 = 0
        possible_shift.append(diff_1)
        possible_shift.append("none")

    if y > z:
        diff_2 = y - z
        possible_shift.append(diff_2)
        possible_shift.append("right")
    elif y < z:
        diff_2 = z - y
        possible_shift.append(diff_2)
        possible_shift.append("left")
    else:
        diff_2 = 0
        possible_shift.append(diff_2)
        possible_shift.append("none")

    if w > x:
        diff_3 = w - x
        possible_shift.append(diff_3)
        possible_shift.append("right")
    elif w < x:
        diff_3 = x - w
        possible_shift.append(diff_3)
        possible_shift.append("left")
    else:
        diff_3 = 0
        possible_shift.append(diff_3)
        possible_shift.append("none")

    if w > z:
        diff_4 = w - z
        possible_shift.append(diff_4)
        possible_shift.append("right")
    elif w < z:
        diff_4 = z - w
        possible_shift.append(diff_4)
        possible_shift.append("left")
    else:
        diff_4 = 0
        possible_shift.append(diff_4)
        possible_shift.append("none")

    # The below loop runs each case from possible_shift list. Each letter from the original encrypted message will be shifted by each case in the possible_shift list.
    # Each result for each case is saved in d_msg_f list.
    for index, i in enumerate(possible_shift):
        d_msg = []
        if isinstance(i, int):
            if possible_shift[index+1] == 'right':
                for j in msg:
                    if j not in alphabet:
                        d_msg.append(j)
                    else:
                        d_alpha = alphabet[alphabet.index(j) - i]
                        d_msg.append(d_alpha)
                d_msg_str = ''.join(d_msg)
                d_msg_f.append(d_msg_str)
                d_msg_f.append("Shift: " + str(i))
                d_msg_f.append('Direction: Right')
            
            elif possible_shift[index+1] == 'left':
                for j in msg:
                    if j not in alphabet:
                        d_msg.append(j)
                    else:
                        if alphabet.index(j) + i > 25:
                            d_alpha = alphabet[alphabet.index(j) + i - 26]
                        else:
                            d_alpha = alphabet[alphabet.index(j) + i]
                        d_msg.append(d_alpha)
                d_msg_str = ''.join(d_msg)
                d_msg_f.append(d_msg_str)
                d_msg_f.append("Shift: " + str(i))
                d_msg_f.append('Direction: Left')
                
            else:
                d_msg_str = msg
                d_msg_f.append(d_msg_str)
                d_msg_f.append("Shift: 0")
                d_msg_f.append('Direction: None')
        else:
            continue

    return d_msg_f

def main():
    # This is the main function.
    # Sample ciphertexts that user can choose from. User may also enter custom ciphertext.
    print('''
Sample ciphertext options below.
Please choose one from below and copy & paste into the inputfield or enter your own ciphertext.


If he had anything confidential to say, he wrote it in cipher, that is, by 
so changing the order of the letters of the alphabet, that not a word could be made out.
Shift: 3, Direction: Right

Li kh kdg dqbwklqj frqilghqwldo wr vdb, kh zurwh lw lq flskhu, wkdw lv, eb 
vr fkdqjlqj wkh rughu ri wkh ohwwhuv ri wkh doskdehw, wkdw qrw d zrug frxog eh pdgh rxw.


Method in which each letter in the plaintext is replaced by a letter some fixed number of 
positions down the alphabet. The method is named after Julius Caesar, who used it in his 
private correspondence.
Shift: 14, Direction: Left

Yqftap uz ituot qmot xqffqd uz ftq bxmuzfqjf ue dqbxmoqp nk m xqffqd eayq rujqp zgynqd ar 
baeufuaze paiz ftq mxbtmnqf. Ftq yqftap ue zmyqp mrfqd Vgxuge Omqemd, ita geqp uf uz tue 
bduhmfq oaddqebazpqzoq.
    
    ''')
    
    # Inputfield to enter encrypted message.
    enc_msg = input("Please enter encrypted message:\n")

    # Calls the decrypt() function.
    dec_msg = decrypt(enc_msg)
    
    print("\nPossible decrypted messages:\n")

    # Running a loop through dec_msg to show all possibilities of decrypted message for better readability
    cnt = 0
    for f in dec_msg:
        # Output the decrypted message and the number of shift and direction. Direction is indicated by positive or negative number.
        cnt += 1
        print(f)
        if cnt == 3:
            # New line is added every time after 3 outputs. Only for readability purpose.
            print("")
            cnt = 0
        else:
            pass
    
if __name__ == "__main__":
    main()