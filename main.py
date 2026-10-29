message = "Hi"

unicode_values = []

for char in message:
    unicode_values.append(ord(char))

binary_values = []

for n in unicode_values:
    dividend = n
    remainder = []

    while dividend > 0:
        remainder.append(dividend % 2)
        dividend = dividend // 2

    remainder.reverse()

    if n == 0:
        binary = "0"
    else:
        binary = ''.join(str(bit) for bit in remainder)

    target_length = 8
    additional_bits = target_length - len(binary)

    if additional_bits > 0:
        bits_need = "0" * additional_bits
        binary = bits_need + binary

    binary_values.append(binary)

print("Message:", message)
print("Unicode values:", unicode_values)
print("Binary values:", binary_values)