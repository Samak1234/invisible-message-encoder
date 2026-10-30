message = "Hi"

unicode_values = []
binary_values = []

for char in message:
    unicode_value = ord(char)
    unicode_values.append(unicode_value)

    binary = format(unicode_value, '08b')
    binary_values.append(binary)

print("Message:", message)
print("Unicode values:", unicode_values)
print("Binary values:", binary_values)