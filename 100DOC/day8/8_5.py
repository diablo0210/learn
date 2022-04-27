# Caesar's Cipher (self)
#  failed attempt
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    text = list(text)
    output = []
    for i in range(0, len(text)):
        # text[i] = text[i+shift]
        # print(text[i])
        for j in range(0, len(alphabet)):
            if text[i] == alphabet[j]:
                output.append(alphabet[j + shift])
    print(output)
    print("".join(output))

encrypt(text, shift)

