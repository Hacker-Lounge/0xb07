import binascii
import codecs
import hunspell

def rot13(*args):
    given_string  =" ".join([x for x in args])
    return "```" + codecs.encode(given_string,'rot_13') + "```"

def hex_to_ascii(*args):
    given_string  =" ".join([x for x in args])
    return "```" + binascii.unhexlify(given_string) + "```"

def ascii_to_hex(*args):
    given_string  =" ".join([x for x in args])
    return "```" + str(binascii.hexlify(given_string.encode())) + "```"


def brute_rot(*args):
    enc_string  =" ".join([x for x in args])
    dec_strings = []
    for key in range(1,26):
        dec_string = ""
        for c in enc_string:
            if c.isalpha():
                if c.islower():
                    dec_string += chr((ord(c)+key-97)%26 + 97)
                else:
                    dec_string += chr((ord(c)+key-65)%26 + 65)
            else:
                dec_string+=c
        dec_strings.append(dec_string)
    
    # FIXME: sometimes it ranks non-words as words
    hobj = hunspell.HunSpell('/usr/share/hunspell/en_US.dic', '/usr/share/hunspell/en_US.aff')
    msg_table = []
    for i,dec_string in enumerate(dec_strings):
        curr_rank = 0 
        for word in dec_string.split():
            if hobj.spell(word):
                curr_rank+=1
        msg_table.append((curr_rank,i+1,dec_string))
    
    msg_table = sorted(msg_table,key = lambda x: x[0],reverse = True)

    formatted_msg_table = "rank | key | decrypted_string\n"
    for rank,key,dec_string in msg_table:
        formatted_msg_table += f"{rank:>4} | {key:>3} | {dec_string}\n"
    return ["```" + formatted_msg_table + "```"]