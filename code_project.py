# code breaker
alphabet = "abcdefghijklmnopqrstuvwxyz"
# his_code = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
# offset = 14

# his_code = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."


his_code = (
    "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
)

# some tests of alphabet indexing:
# print(alphabet[5])
# print(alphabet[15])
# print("alphabet[23] >>> ", alphabet[33 % 26])
# print(len(alphabet))
# print(len(his_code))
# print(his_code[len(his_code) - 1])


def new_alpha_index(code_index, offset):
    return (code_index + offset) % len(alphabet)
    # value of right-shifted position using remainder operation, %


def coded_alpha_index(position, offset):
    return (position - offset + len(alphabet)) % len(alphabet)
    # value of left-shifted position using remainder operation, %
    # making sure to prevent negative values


def caesar_decode(message, offset):
    alpha_index = 0
    solved = ""
    for i in range(0, len(message)):
        code_alpha_index = alphabet.find(message[i])  # finds letter index in 'alphabet'
        if code_alpha_index >= 0:
            solved += alphabet[new_alpha_index(code_alpha_index, offset)]
        else:
            solved += message[i]
    print(solved)
    return solved


def caesar_encode(message, offset):
    out_alpha_index = 0
    coded_reply = ""
    for i in range(0, len(response)):
        out_alpha_index = alphabet.find(response[i])
        if out_alpha_index >= 0:
            coded_reply += alphabet[coded_alpha_index(out_alpha_index, offset)]
        else:
            coded_reply += response[i]
    print(coded_reply)
    return coded_reply


# caesar_decode(his_code, offset)

response = alphabet + " ! _"
# caesar_encode(response, offset)

unknown = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."


for i in range(8):
    caesar_decode(unknown, i)
