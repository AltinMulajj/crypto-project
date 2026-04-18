import os


ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#"

def build_cube(key: str) -> list:
    """
    Ndërton kubin 3x3x3 bazuar në çelësin e dhënë.

    Logjika:
      - Çelësi vendoset i pari (pa shkronja të përsëritura)
      - Pastaj mbushen shkronjat e mbetura nga ALPHABET
      - Rezultati është një listë 3D: cube[layer][row][col]

    Shembull me key="KEY":
      Renditja: K, E, Y, A, B, C, D, F, G, H, I, J, ...
    """
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
    """
    Krijon fjalorin {shkronjë: (layer, row, col)} për kërkim të shpejtë.

    Pa këtë fjalor, do të duhet të kërkojmë nëpër të gjithë kubin
    për çdo shkronjë — O(27) per karakter. Me fjalor është O(1).
    """
    lookup = {}
    for l in range(3):
        for r in range(3):
            for c in range(3):
                lookup[cube[l][r][c]] = (l, r, c)
    return lookup




def encrypt(plaintext: str, key: str, period: int = 5) -> str:
    """
    Enkripton tekstin me Trifid Cipher.

    Args:
        plaintext : teksti origjinal
        key       : çelësi për ndërtimin e kubit
        period    : madhësia e grupeve (default 5)

    Returns:
        Teksti i enkriptuar (ciphertext)

    Si funksionon hap pas hapi:
      1. Pastrojmë tekstin — vetëm shkronja, J→I, uppercase
      2. Ndajmë në grupe sipas period (p.sh. period=5 → grupe prej 5)
      3. Për secilin grup:
         a. Çdo shkronjë → koordinata (layer, row, col)
         b. Grumbullojmë: layers=[], rows=[], cols=[]
         c. Bashkojmë: combined = layers + rows + cols
         d. Lexojmë combined me grupe prej 3 → shkronjë e re
    """
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
    """
    Dekripson tekstin e enkriptuar me Trifid Cipher.

    Args:
        ciphertext : teksti i enkriptuar
        key        : çelësi (duhet të jetë i njëjtë me enkriptimin)
        period     : madhësia e grupeve (duhet të jetë i njëjtë me enkriptimin)

    Returns:
        Teksti origjinal (plaintext)

    Si funksionon hap pas hapi:
      1. Çdo shkronjë e ciphertextit → koordinata (layer, row, col)
      2. Shpërndajmë koordinatat në listë të sheshtë (flat)
      3. Ndajmë flat në tri pjesë: layers, rows, cols (secila me n karaktere)
      4. Rindërtojmë shkronjat origjinale: cube[layers[j]][rows[j]][cols[j]]
    """
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
    """
    Shfaq kubin 3x3x3 në terminal në formë të lexueshme.
    Secili layer shfaqet si grid 3x3.
    """
    print("\n  Kubi 3x3x3 (Layer → Row → Col):\n")
    for l in range(3):
        print(f"  Layer {l + 1}:")
        for row in cube[l]:
            print("    " + " | ".join(row))
        print()


def clear():
    """Pastron ekranin e terminalit (Linux/Windows)."""
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print("=" * 54)
    print("       TRIFID CIPHER  —  Python Implementation")
    print("=" * 54)


def get_period() -> int:
    """
    Merr period-in nga përdoruesi me validim.
    Nëse përdoruesi shtyp Enter, përdoret vlera default 5.
    """
    while True:
        try:
            p = int(input("  Period (default 5, rekomandohet 3-10): ") or "5")
            if p < 1:
                raise ValueError
            return p
        except ValueError:
            print("  Fut një numër të plotë pozitiv!")


def menu():
    """
    Menyja kryesore interaktive e Trifid Cipher.
    Ofron enkriptim, dekriptim, shfaqje të kubit dhe demo.
    """
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