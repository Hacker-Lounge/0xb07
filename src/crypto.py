import binascii
import codecs

def rot13(msg):
    return codecs.encode(':'.join(msg.split(':')[1:]), 'rot_13')


def h2a(msg):
    return binascii.unhexlify(':'.join(msg.split(':')[1:])).decode()

def a2h(msg):
    return [''.join([str(hex(i)) for i in binascii.hexlify((':'.join(msg.split(':')[1:])).encode())])]