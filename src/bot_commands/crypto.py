import binascii
import codecs

def rot13(args):
    given_string  =" ".join([x for x in args])
    return codecs.encode(given_string,'rot_13')


def hex_to_ascii(args):
    given_string  =" ".join([x for x in args])
    return "```" + binascii.unhexlify(given_string) + "```"

def ascii_to_hex(args):
    given_string  =" ".join([x for x in args])
    return "```" + str(binascii.hexlify(given_string.encode())) + "```"


def brute_rot(args):
    # TODO: check for words in dictionary and rank results
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
    # Super Ugly
    formatted_table = \
        "```\n"+\
            "Key | decrypted_string\n" + \
            "".join([f" {key:02}" + " | " + dec_string + "\n" for key,dec_string in dec_strings ]) +\
        "```"
    return [formatted_table]