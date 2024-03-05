binlist = ["0000", "0001", "0010", "0011", "0100", "0101", "0110", "0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]
hexlist = "0123456789ABCDEF"

nums = [bin(int(input("Please input a number 0-255\n"))),
        bin(int(input("Please input another number 0-255\n"))),
        bin(int(input("Please input another number 0-255\n")))]

def binToHex(bin):
    bin = bin.replace("0b", "")
    bin = "0"*(8-len(bin))+ bin

    bin1 = bin[0]+bin[1]+bin[2]+bin[3]
    bin2 = bin[4]+bin[5]+bin[6]+bin[7]

    hex1 = hexlist[binlist.index(bin1)]
    hex2 = hexlist[binlist.index(bin2)]

    return hex1 + hex2


hexstring = binToHex(nums[0]) + binToHex(nums[1]) + binToHex(nums[2])
print(hexstring)