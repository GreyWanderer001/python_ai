import re

neapstrādāts_teksts = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

def tīrīt_tekstu(teksts):

    teksts_tīrs = re.sub(r'@\w+', '', teksts)
    teksts_tīrs = re.sub(r'http\S+', '', teksts_tīrs)
    teksts_tīrs = re.sub(r'[^\w\sāčēģīķļņūž]', '', teksts_tīrs)

    teksts_tīrs = re.sub(r'\s+', ' ', teksts_tīrs).strip()

    teksts_tīrs = teksts_tīrs.lower()
    return teksts_tīrs

tīrs_teksts = tīrīt_tekstu(neapstrādāts_teksts)
print("Tīrs teksts:")
print(tīrs_teksts)
