def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result

# Example usage:
if __name__ == "__main__":
    print("🔐 Caesar Cipher Tool 🔐")
    choice = input("Type 'encrypt' or 'decrypt': ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    output = caesar_cipher(message, shift, mode=choice)
    print(f"\nResult: {output}")
