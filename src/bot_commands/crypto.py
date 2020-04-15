import binascii
import codecs

def rot13(msg):
    return codecs.encode(':'.join(msg.split(':')[1:]), 'rot_13')


def h2a(msg):
    return binascii.unhexlify(':'.join(msg.split(':')[1:])).decode()

def a2h(msg):
    return [''.join([str(hex(i)) for i in binascii.hexlify((':'.join(msg.split(':')[1:])).encode())])]


def brute_rot(args):
    enc_string  =" ".join([x for x in args])
    dec_strings = []
    for key in range(1,26):
        dec_string = ""
        for c in enc_string:
            if c.isalpha():
                if c.islower:
                    dec_ord = ord(c)+key
                    if dec_ord > 122:
                        dec_ord -= 26
                    elif dec_ord<97:
                        dec_ord += 26
                    dec_string+=chr(dec_ord)
                else:
                    dec_ord = ord(c)+key
                    if dec_ord > 90:
                        dec_ord -= 26
                    elif dec_ord < 65:
                        dec_ord += 26
                    dec_string+=chr(dec_ord)
            else:
                dec_string+=c
        dec_strings.append((key,dec_string))
    formatted_table = \
        "```\n"+\
            "Key | decrypted_string\n" + \
            "".join([f" {key:02}" + " | " + dec_string + "\n" for key,dec_string in dec_strings ]) +\
        "```"
    return [formatted_table]