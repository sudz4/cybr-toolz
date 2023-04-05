"""bitwise XOR operator example"""

a = int('11011000', 2) # binary representation of 216
b = int('10010101', 2) # binary representation of 149

result = a ^ b # bitwise XOR operator

print(bin(result)[2:].zfill(8)) # convert result to binary and print it, padded with leading zeros to make it 8 bits
# the bin() function converts the result back to binary