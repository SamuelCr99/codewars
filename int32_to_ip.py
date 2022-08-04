from tkinter import W


def int32_to_IPv4(int32):
    binary_value = bin(int32)
    binary_value = binary_value[2 : ]
    len_to_add = 32 - len(binary_value)
    binary_value = "0" * len_to_add + binary_value
    octet1 = int(binary_value[ : 8],2)
    octet2 = int(binary_value[8 : 16],2)
    octet3 = int(binary_value[16 : 24],2)
    octet4 = int(binary_value[24 : 32],2)
    return str(octet1) + "." + str(octet2) + "." + str(octet3) + "." + str(octet4)

    

print(int32_to_IPv4(2149583361))

