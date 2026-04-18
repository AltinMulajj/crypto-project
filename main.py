import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

import trifid_cipher
import columnar_transposition




def clear():
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        print("\n" * 5)


def banner():

    print("=" * 56)
    print("        CRYPTO PROJECT — Kriptografi Klasike")
    print("    Trifid Cipher  +  Columnar Transposition")
    print("=" * 56)




def quick_trifid_encrypt():

    clear()
    banner()
    print("\n  -- TRIFID CIPHER: Enkriptim i shpejtë --\n")
    try:
        text   = input("  Teksti         : ").strip()
        key    = input("  Çelësi         : ").strip()
        period = int(input("  Period (default 5): ").strip() or "5")

        if not text or not key:
            raise ValueError("Teksti dhe çelësi nuk mund të jenë bosh!")

        result = trifid_cipher.encrypt(text, key, period)
        print(f"\n  Ciphertext : {result}")
    except ValueError as e:
        print(f"\n  Gabim: {e}")
    input("\n  [Enter për të vazhduar]")


def quick_trifid_decrypt():

    clear()
    banner()
    print("\n  -- TRIFID CIPHER: Dekriptim i shpejtë --\n")
    try:
        text   = input("  Ciphertext     : ").strip()
        key    = input("  Çelësi         : ").strip()
        period = int(input("  Period (default 5): ").strip() or "5")

        if not text or not key:
            raise ValueError("Teksti dhe çelësi nuk mund të jenë bosh!")

        result = trifid_cipher.decrypt(text, key, period)
        print(f"\n  Plaintext  : {result}")
    except ValueError as e:
        print(f"\n  Gabim: {e}")
    input("\n  [Enter për të vazhduar]")


def quick_columnar_encrypt():

    clear()
    banner()
    print("\n  -- COLUMNAR TRANSPOSITION: Enkriptim i shpejtë --\n")
    try:
        text = input("  Teksti         : ").strip()
        key  = input(f"  Çelësi (default {columnar_transposition.KEY}): ").strip() or columnar_transposition.KEY

        if not text:
            raise ValueError("Teksti nuk mund të jetë bosh!")

        result = columnar_transposition.encrypt(text, key)
        print(f"\n  Ciphertext : {result}")
    except ValueError as e:
        print(f"\n  Gabim: {e}")
    input("\n  [Enter për të vazhduar]")


def quick_columnar_decrypt():

    clear()
    banner()
    print("\n  -- COLUMNAR TRANSPOSITION: Dekriptim i shpejtë --\n")
    try:
        text = input("  Ciphertext     : ").strip()
        key  = input(f"  Çelësi (default {columnar_transposition.KEY}): ").strip() or columnar_transposition.KEY

        if not text:
            raise ValueError("Ciphertext nuk mund të jetë bosh!")

        result = columnar_transposition.decrypt(text, key)
        print(f"\n  Plaintext  : {result}")
        print("  Shenim: shkronjat 'X' ne fund mund te jene padding.")
    except ValueError as e:
        print(f"\n  Gabim: {e}")
    input("\n  [Enter për të vazhduar]")




def combined_demo():

    clear()
    banner()
    print("\n  -- DEMO E KOMBINUAR --\n")

    demo_text = "CRYPTOGRAPHY"

    print(f"  Teksti origjinal : {demo_text}")
    print()


    t_key    = "PYTHON"
    t_period = 5
    t_enc = trifid_cipher.encrypt(demo_text, t_key, t_period)
    t_dec = trifid_cipher.decrypt(t_enc, t_key, t_period)

    print(f"  [ TRIFID CIPHER ]")
    print(f"  Çelësi     : {t_key}   Period: {t_period}")
    print(f"  Encrypted  : {t_enc}")
    print(f"  Decrypted  : {t_dec}")
    print(f"  Korrekte   : {'Po' if t_dec == demo_text else 'Jo'}")
    print()

    # Columnar Transposition demo
    c_key = columnar_transposition.KEY
    c_enc = columnar_transposition.encrypt(demo_text, c_key)
    c_dec = columnar_transposition.decrypt(c_enc, c_key)

    print(f"  [ COLUMNAR TRANSPOSITION ]")
    print(f"  Çelësi     : {c_key}")
    print(f"  Encrypted  : {c_enc}")
    print(f"  Decrypted  : {c_dec}")
    print(f"  Korrekte   : {'Po' if c_dec.rstrip('X') == demo_text else 'Jo'}")

    input("\n  [Enter për të vazhduar]")




def main():

    while True:
        clear()
        banner()
        print()
        print("  TRIFID CIPHER")
        print("  [1]  Encrypt")
        print("  [2]  Decrypt")
        print()
        print("  COLUMNAR TRANSPOSITION  (çelësi: ANANASI)")
        print("  [3]  Encrypt")
        print("  [4]  Decrypt")
        print()
        print("  OPSIONE TE TJERA")
        print("  [5]  Menu e plote — Trifid Cipher")
        print("  [6]  Menu e plote — Columnar Transposition")
        print("  [7]  Demo e kombinuar")
        print()
        print("  [0]  Dil")
        print()
        choice = input("  Zgjidhni opsionin: ").strip()

        if   choice == "1": quick_trifid_encrypt()
        elif choice == "2": quick_trifid_decrypt()
        elif choice == "3": quick_columnar_encrypt()
        elif choice == "4": quick_columnar_decrypt()
        elif choice == "5": trifid_cipher.menu()
        elif choice == "6": columnar_transposition.menu()
        elif choice == "7": combined_demo()
        elif choice == "0":
            clear()
            print("\n  Mirupafshim!\n")
            break
        else:
            print("\n  Opsion i pavlefshëm, provo përsëri.")
            input("  [Enter]")


if __name__ == "__main__":
    main()
