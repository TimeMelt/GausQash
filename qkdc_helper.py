import numpy as np
import struct
from binascii import b2a_base64

# process output of quantum circuits into proper hash
def processOutput(output, format):
    hex_params = {
        "unpack_long_long": '<Q',
        "pack_double": '<d',
    }
    output_alt = []
    for value in output: # process complex into hex
        val_alt = value*100
        if val_alt < 0:
            output_alt.append(hex(struct.unpack(hex_params['unpack_long_long'], struct.pack(hex_params['pack_double'], -val_alt))[0]))
        else:
            output_alt.append(hex(struct.unpack(hex_params['unpack_long_long'], struct.pack(hex_params['pack_double'], val_alt))[0]))
    output_string = ''.join(output_alt)
    output_string = output_string.replace('0x', "") # remove hex markers
    output_string = output_string.replace(output_string[:4], "", 1) # remove chars for increased hash security 
    if format == 'hex':
        pass
    elif format == 'base64':
        output_string = b2a_base64(bytes(output_string, 'utf-8')).decode('utf-8')# convert to base64
    else:
        print("invalid format...")
    return output_string

# convert chars to unicode
def createData(text): 
    arr = np.array([])
    for ch in text:
        arr = np.append(arr, ord(ch)/100) # divide ord() by 100 to bring values matrix back into positive definite
    return arr

# pad data based on desired hash length
def padData(txt_arr, pad_count): 
    if pad_count == 0:
        return txt_arr
    else:
        new_arr = txt_arr
        for q in range(pad_count):
            new_arr = np.append(new_arr, txt_arr[q] * np.tan(txt_arr[q]))
        return new_arr

# convert to unicode and pad
def createAndPad(text, pad_count):
    arr = createData(text)
    arr1 = padData(arr, pad_count)
    return arr1