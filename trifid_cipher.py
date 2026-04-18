import os


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#"

def build_cube(key: str) -> list:

    key = key.upper().replace("J", "I")  

    seen = []
    for ch in key + ALPHABET:
        if ch not in seen:
            seen.append(ch)
        if len(seen) == 27:
            break

    cube = []
    idx = 0
    for layer in range(3):
        grid = []
        for row in range(3):
            grid.append(seen[idx:idx + 3])
            idx += 3
        cube.append(grid)

    return cube


def build_lookup(cube: list) -> dict:
  
    lookup = {}
    for l in range(3):
        for r in range(3):
            for c in range(3):
                lookup[cube[l][r][c]] = (l, r, c)
    return lookup




def encrypt(plaintext: str, key: str, period: int = 5) -> str:
   
    cube   = build_cube(key)
    lookup = build_lookup(cube)


    clean = ""
    for ch in plaintext.upper():
        if ch == "J":
            ch = "I"
        if ch in lookup:
            clean += ch

    if not clean:
        raise ValueError("Teksti nuk përmban karaktere të vlefshme!")

    ciphertext = ""

    for i in range(0, len(clean), period):
        group = clean[i:i + period]

        # Hapi 1: Gjejmë koordinatat për çdo shkronjë në grup
        layers, rows, cols = [], [], []
        for ch in group:
            l, r, c = lookup[ch]
            layers.append(l)
            rows.append(r)
            cols.append(c)

        # Hapi 2: Bashkojmë të gjitha koordinatat: layers + rows + cols
        combined = layers + rows + cols

        # Hapi 3: Lexojmë grupe prej 3 nga combined → shkronjë e re
        for j in range(0, len(combined), 3):
            l, r, c = combined[j], combined[j + 1], combined[j + 2]
            ciphertext += cube[l][r][c]

    return ciphertext



def decrypt(ciphertext: str, key: str, period: int = 5) -> str:
    
    cube   = build_cube(key)
    lookup = build_lookup(cube)

    clean = ""
    for ch in ciphertext.upper():
        if ch == "J":
            ch = "I"
        if ch in lookup:
            clean += ch

    if not clean:
        raise ValueError("Ciphertext nuk përmban karaktere të vlefshme!")

    plaintext = ""

    for i in range(0, len(clean), period):
        group = clean[i:i + period]
        n = len(group)


        flat = []
        for ch in group:
            l, r, c = lookup[ch]
            flat.extend([l, r, c])


        layers = flat[0:n]
        rows   = flat[n:2 * n]
        cols   = flat[2 * n:3 * n]


        for j in range(n):
            plaintext += cube[layers[j]][rows[j]][cols[j]]

    return plaintext


def display_cube(cube: list):
   
    print("\n  Kubi 3x3x3 (Layer → Row → Col):\n")
    for l in range(3):
        print(f"  Layer {l + 1}:")
        for row in cube[l]:
            print("    " + " | ".join(row))
        print()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print("=" * 54)
    print("       TRIFID CIPHER  —  Python Implementation")
    print("=" * 54)


def get_period() -> int:
    
    while True:
        try:
            p = int(input("  Period (default 5, rekomandohet 3-10): ") or "5")
            if p < 1:
                raise ValueError
            return p
        except ValueError:
            print("  Fut një numër të plotë pozitiv!")


def menu():
    
    while True:
        clear()
        banner()
        print()
        print("  [1]  Enkriptim (Encrypt)")
        print("  [2]  Dekriptim (Decrypt)")
        print("  [3]  Shfaq Kubin")
        print("  [4]  Demo e shpejtë")
        print("  [0]  Kthehu")
        print()
        choice = input("  Zgjidhni opsionin: ").strip()

        if choice == "1":
            clear()
            banner()
            print("\n  -- ENKRIPTIM --\n")
            try:
                text   = input("  Teksti origjinal : ").strip()
                key    = input("  Çelësi           : ").strip()
                period = get_period()

                if not text or not key:
                    raise ValueError("Teksti dhe çelësi nuk mund të jenë bosh!")

                result = encrypt(text, key, period)
                print(f"\n  Ciphertext : {result}")
            except ValueError as e:
                print(f"\n  Gabim: {e}")
            input("\n  [Enter për të vazhduar]")

        elif choice == "2":
            clear()
            banner()
            print("\n  -- DEKRIPTIM --\n")
            try:
                text   = input("  Ciphertext       : ").strip()
                key    = input("  Çelësi           : ").strip()
                period = get_period()

                if not text or not key:
                    raise ValueError("Teksti dhe çelësi nuk mund të jenë bosh!")

                result = decrypt(text, key, period)
                print(f"\n  Plaintext  : {result}")
            except ValueError as e:
                print(f"\n  Gabim: {e}")
            input("\n  [Enter për të vazhduar]")

        elif choice == "3":
            clear()
            banner()
            key = input("\n  Çelësi për kubin: ").strip() or "KEY"
            cube = build_cube(key)
            display_cube(cube)
            input("  [Enter për të vazhduar]")

        elif choice == "4":
            clear()
            banner()
            print("\n  -- DEMO --\n")
            demo_text   = "HELLO"
            demo_key    = "PYTHON"
            demo_period = 5

            enc = encrypt(demo_text, demo_key, demo_period)
            dec = decrypt(enc, demo_key, demo_period)

            print(f"  Plaintext  : {demo_text}")
            print(f"  Çelësi     : {demo_key}")
            print(f"  Period     : {demo_period}")
            print(f"  Encrypted  : {enc}")
            print(f"  Decrypted  : {dec}")
            print(f"\n  {'Decryption korrekte!' if dec == demo_text else 'Gabim në decryption!'}")
            input("\n  [Enter për të vazhduar]")

        elif choice == "0":
            break

        else:
            print("\n  Opsion i pavlefshëm, provo përsëri.")
            input("  [Enter]")



if __name__ == "__main__":
    menu()