def hex_output(hexValue):
    decimalValue = 0
    for power, digit in enumerate(reversed(hexValue)):
        decimalValue += int(digit, 16) * 16**power

    print(decimalValue)


hex_output('18618')   # 0x...