# -*- coding: utf-8 -*-

import string
_default_alphabet = string.ascii_uppercase.encode()
_default_size = 8
import utils

@utils.decorators


def _de_bruijn(alphabet = None, n = None):
    if alphabet is None:
        alphabet = _default_alphabet
    if n is None:
        n = _default_size

    if isinstance(alphabet, bytes):
        alphabet = bytearray(alphabet)

    k = len(alphabet)
    a = [0] * k * n
    def db(t, p):
        if t > n:
            if n % p == 0:
                for j in range(1, p + 1):
                    yield alphabet[a[j]]
        else:
            a[t] = a[t - p]
            for c in db(t + 1, p):
                yield c

            for j in range(a[t - p] + 1, k):
                a[t] = j
                for c in db(t + 1, t):
                    yield c

    return db(1,1)

def cyclic(length = None, alphabet = None, n = None, *args):
    
    if n is None:
        n = _default_size

    if alphabet is None:
        alphabet = _default_alphabet

    out = []
    for ndx, c in enumerate(_de_bruijn(alphabet, n)):
        if length != None and ndx >= length:
            break
        else:
            out.append(c)

    if isinstance(alphabet, str):
        return ''.join(out)
    elif isinstance(alphabet, bytes):
        return bytes(bytearray(out))
    else:
        return out

def _gen_find(subseq, generator):
    """Returns the first position of `subseq` in the generator or -1 if there is no such position."""
    if isinstance(subseq, bytes):
        subseq = bytearray(subseq)
    subseq = list(subseq)
    pos = 0
    saved = []

    for c in generator:
        saved.append(c)
        if len(saved) > len(subseq):
            saved.pop(0)
            pos += 1
        if saved == subseq:
            return pos
    return -1

def cyclic_find(subseq, alphabet = None, n = None, *args):
    

    if n is None:
        n = _default_size

    if len(subseq) != n:
        subseq = subseq[:n]

    if alphabet is None:
        alphabet = _default_alphabet

    if any(c not in alphabet for c in subseq):
        return -1

    n = n or len(subseq)

    return _gen_find(subseq, de_bruijn(alphabet, n))