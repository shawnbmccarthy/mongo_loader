#
# 3.5 and earlier does not have secrets
#
import os
import binascii

def token_hex(sz):
    return binascii.hexlify(os.urandom(sz)).decode('ascii')