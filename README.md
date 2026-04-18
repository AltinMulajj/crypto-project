# Crypto Project — Trifid Cipher & Columnar Transposition

Implementim i dy algoritmeve klasike të kriptografisë në Python:
**Trifid Cipher** dhe **Columnar Transposition Cipher**.

---

## Si ekzekutohet programi

### Kërkesat
- Python 3.x (pa librari të jashtme — vetëm modulet standarde)

### Ekzekutimi

```bash
# Klono projektin (herën e parë)
git clone https://github.com/username/crypto-project.git
cd crypto-project

# Ekzekuto programin kryesor
python3 main.py
```

### Opsione alternative

```bash
# Vetëm Trifid Cipher
python3 trifid_cipher.py

# Vetëm Columnar Transposition
python3 columnar_transposition.py
```

### Struktura e projektit

```
crypto-project/
├── main.py                    # Pika kryesore e hyrjes
├── trifid_cipher.py           # Implementimi i Trifid Cipher
├── columnar_transposition.py  # Implementimi i Columnar Transposition
├── README.md                  # Ky dokument
└── .gitignore
```

---

## Përshkrimi i algoritmeve

### 1. Trifid Cipher

Trifid Cipher është një algoritëm kriptografik klasik i shpikur nga
Felix Delastelle në vitin 1901. Bën pjesë në kategorinë e **fractionation ciphers** —
ai e "copëton" çdo shkronjë në koordinata dhe i rikombimon ato.

**Si funksionon:**

1. Ndërtohet një **kub 3×3×3** me 27 karaktere (A–Z + `#`)  
   Çelësi vendoset i pari, pastaj mbushen shkronjat e mbetura.

2. Çdo shkronjë ka një **adresë 3D**: `(layer, row, col)` — tre shifra nga 0 deri 2.

3. Teksti ndahet në **grupe sipas period-it** (default: 5).

4. Për secilin grup, koordinatat grupohen:  
   `combined = [layers...] + [rows...] + [cols...]`

5. Çdo treshe e re nga `combined` → shkronjë e re nga kubi → **ciphertext**.

**Dekriptimi** është procesi i kundërt: koordinatat e ciphertextit ndahen
përsëri në layers/rows/cols dhe rindërtojnë shkronjat origjinale.

**Parametrat:**
- `key` — çelësi për ndërtimin e kubit (çdo fjalë)
- `period` — madhësia e grupeve (rekomandohet 3–10, default: 5)

---

### 2. Columnar Transposition Cipher

Columnar Transposition është një algoritëm i tipit **transposition** —
ndryshe nga Trifid, ai nuk i zëvendëson shkronjat, vetëm i **rirendit** ato.
Përdorej gjerësisht gjatë Luftës së Dytë Botërore.

**Çelësi i projektit: `ANANASI`**

**Si funksionon:**

1. Teksti shkruhet **rresht pas rreshti** në një tabelë me 7 kolona  
   (7 = gjatësia e çelësit `ANANASI`).

2. Nëse rreshti i fundit nuk plotësohet, shtohet **padding** me `X`.

3. Kolonat **lexohen sipas renditjes alfabetike** të çelësit:  
   `ANANASI` → renditja: `A(0) A(2) A(4) I(6) N(1) N(3) S(5)`  
   → order: `[0, 2, 4, 6, 1, 3, 5]`

4. Rezultati i leximit kolona-kolona = **ciphertext**.

**Dekriptimi** rindërton tabelën origjinale duke vendosur kolonat
në pozicionet e tyre origjinale, pastaj lexon rresht pas rreshti.

---

## Shembuj të ekzekutimit

### Trifid Cipher — Enkriptim

```
===== CRYPTO MENU =====
Zgjidhni opsionin: 1

-- TRIFID CIPHER: Enkriptim i shpejte --

Teksti         : HELLO
Celesi         : PYTHON
Period (default 5): 5

Ciphertext : OECEI
```

### Trifid Cipher — Dekriptim

```
===== CRYPTO MENU =====
Zgjidhni opsionin: 2

-- TRIFID CIPHER: Dekriptim i shpejte --

Ciphertext     : OECEI
Celesi         : PYTHON
Period (default 5): 5

Plaintext  : HELLO
```

### Trifid Cipher — Shembull tjetër

```
Teksti     : ATTACK
Celesi     : PYTHON
Period     : 5
Encrypted  : PTTSSK
Decrypted  : ATTACK
```

---

### Columnar Transposition — Enkriptim

```
===== CRYPTO MENU =====
Zgjidhni opsionin: 3

-- COLUMNAR TRANSPOSITION: Enkriptim i shpejte --

Teksti         : WEAREDISCOVERED
Celesi (default ANANASI):

Ciphertext : WSDAOXEEXIEXECXRVXDRX
Gjatesia   : 21 karaktere
```

### Columnar Transposition — Dekriptim

```
===== CRYPTO MENU =====
Zgjidhni opsionin: 4

-- COLUMNAR TRANSPOSITION: Dekriptim i shpejte --

Ciphertext     : WSDAOXEEXIEXECXRVXDRX
Celesi (default ANANASI):

Plaintext  : WEAREDISCOVEREDXXXXXX
Shenim: shkronjat 'X' ne fund mund te jene padding.
```

### Columnar Transposition — Tabela vizuale

```
Zgjidhni opsionin: 6 -> [3] Shfaq Tabelen

Teksti origjinal : WEAREDISCOVERED

  Tabela e enkriptimit:

  A(1)   N(5)   A(2)   N(6)   A(3)   S(7)   I(4)
  -------------------------------------------------
  W      E      A      R      E      D      I
  S      C      O      V      E      R      E
  D      X      X      X      X      X      X

  Kolonat lexohen sipas rendit: 1 -> 5 -> 2 -> 6 -> 3 -> 7 -> 4
```

### Demo e kombinuar (opsioni 7)

```
Zgjidhni opsionin: 7

-- DEMO E KOMBINUAR --

Teksti origjinal : CRYPTOGRAPHY

[ TRIFID CIPHER ]
Celesi     : PYTHON   Period: 5
Encrypted  : ATPBFNYFHDYY
Decrypted  : CRYPTOGRAPHY
Korrekte   : Po

[ COLUMNAR TRANSPOSITION ]
Celesi     : ANANASI
Encrypted  : CRYPTYGXRAPHOX
Decrypted  : CRYPTOGRAPHYXX
Korrekte   : Po
```

---

## Autorët

- Altin Mulaj
- Eldi Krueziu
- Elion Berisha

Projekt i realizuar si pjesë e kursit **Siguria e të dhënave**  
Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike
