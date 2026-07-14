# code breaker
code_in = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
key_word = "friends"


def decodeit(his_code, keyword):
    offsets = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in keyword:
        position = alphabet.find(char)
        offsets.append(position)
    print(offsets)

    his_code_char_vals = []  # numbers designating index in alphabet
    decoded = ""  # letters
    j = 0  # index of keyword characters
    for char in his_code:
        position = alphabet.find(char)  # code character position in alphabet
        if position >= 0:  # if it's a letter within alphabet-string
            position += offsets[j % (len(keyword))]  # offset value of letter position
            position = position % len(alphabet)  # wrap to start of alphabet if req'd
            his_code_char_vals.append(position)  # append position of decoded letter
            decoded += alphabet[position]  # append letter to decoded
            j += 1  # advance in codekey if on a letter, not punctuation
        else:  # if it's a not a letter in alphabet-string
            his_code_char_vals.append(char)
            decoded += char
    print(decoded)


decodeit(code_in, key_word)


def encodeit(my_text, keyword):
    offsets = []  # numberical values of keyword letter positions in alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in keyword:
        position = alphabet.find(char)
        offsets.append(position)
    print(offsets)

    my_text_char_vals = []  # numbers designating index in alphabet
    encoded = ""  # letters of encoded text
    j = 0  # index of keyword characters
    for char in my_text:
        position = alphabet.find(char)  # code character position in alphabet
        if position >= 0:  # if it's a letter within alphabet-string
            position = (
                position - offsets[j % (len(keyword))]
            )  # offset value of letter position
            if position < 0:
                position = position + len(alphabet)  # wrap to end of alphabet if req'd
            my_text_char_vals.append(position)  # append position of encoded letter
            encoded += alphabet[position]  # append new letter to encoded string
            j += 1  # advance in keyword if on a letter in my_text, not on punctuation
        else:  # if it's a not a letter in alphabet-string
            my_text_char_vals.append(char)
            encoded += char
    print(encoded)


mytext = "you were able to decode this? nice"
encodeit(mytext, "friends")

print("hi", end="-----")
