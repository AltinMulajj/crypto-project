import os

KEY = "ANANASI"

def get_column_order(key):
    key = key.upper()
    indexed = sorted(enumerate(key), key=lambda x: (x[1], x[0]))
    return [i for i, _ in indexed]

def encrypt(plaintext, key=KEY, pad_char="X"):
    key = key.upper()
    n_cols = len(key)

    clean = "".join(ch.upper() for ch in plaintext if ch.isalpha())

    if not clean:
        raise ValueError("Teksti nuk permban shkronja te vlefshme!")

    remainder = len(clean) % n_cols
    if remainder != 0:
        clean += pad_char.upper() * (n_cols - remainder)

    n_rows = len(clean) // n_cols

    table = []
    for r in range(n_rows):
        table.append(list(clean[r * n_cols:(r + 1) * n_cols]))

    order = get_column_order(key)
    ciphertext = ""

    for col in order:
        for row in table:
            ciphertext += row[col]

    return ciphertext

def decrypt(ciphertext, key=KEY):
    key = key.upper()
    n_cols = len(key)

    clean = "".join(ch.upper() for ch in ciphertext if ch.isalpha())

    if not clean:
        raise ValueError("Ciphertext nuk permban shkronja te vlefshme!")

    if len(clean) % n_cols != 0:
        raise ValueError("Ciphertext invalid!")

    n_rows = len(clean) // n_cols
    order = get_column_order(key)

    columns = {}
    idx = 0

    for col_index in order:
        columns[col_index] = list(clean[idx:idx + n_rows])
        idx += n_rows

    plaintext = ""

    for r in range(n_rows):
        for c in range(n_cols):
            plaintext += columns[c][r]

    return plaintext

def clear():

    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        print("\n" * 5)

def banner():
    print("=" * 50)
    print("COLUMNAR TRANSPOSITION CIPHER")
    print("Key:", KEY)
    print("=" * 50)

def menu():
    while True:
        clear()
        banner()
        print("1. Encrypt")
        print("2. Decrypt")
        print("0. Exit")

        choice = input("Zgjedh: ")
        if choice == "1":
            text = input("Text: ")
            result = encrypt(text)
            print("Encrypted:", result)
            input("Press Enter...")

        elif choice == "2":
            text = input("Ciphertext: ")
            result = decrypt(text)
            print("Decrypted:", result)
            input("Press Enter...")

        elif choice == "0":
            break

        else:
            print("Opsioni i pavlefshem!")
            input("Press Enter...")

if __name__ == "__main__":
    menu()                        