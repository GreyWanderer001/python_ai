import re


teksts1 = """Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."""
teksts2 = """Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."""

def attīrīt_tekstu(teksts):
    teksts_tīrs = re.sub(r'[^\w\s]', '', teksts).lower()
    return set(teksts_tīrs.split())

vārdi1 = attīrīt_tekstu(teksts1)
vārdi2 = attīrīt_tekstu(teksts2)


kopiegi_vārdi = vārdi1.intersection(vārdi2)


kopējais_skaits = len(vārdi1.union(vārdi2))
sakritības_procenti = (len(kopiegi_vārdi) / kopējais_skaits) * 100

print("Kopīgie vārdi:")
print(kopiegi_vārdi)
print(f"Sakritības līmenis: {sakritības_procenti:.2f}%")
