print(len('00011010001011010001101101110110111001001101000110111101'))


def StoB(x):
    y = int(x, 16)
    z = ''
    for i in range(4):
        z = str(y % 2) + z
        y = y // 2
    return z

print(StoB('6'))