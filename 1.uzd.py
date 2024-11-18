from collections import Counter
import re


teksts = """Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."""


teksts_tīrs = re.sub(r'[^\w\s]', '', teksts).lower()


vārdi = teksts_tīrs.split()


vārdu_biežums = Counter(vārdi)


print("Vārdu biežums tekstā:")
for vārds, skaits in vārdu_biežums.items():
    print(f"{vārds}: {skaits}")
