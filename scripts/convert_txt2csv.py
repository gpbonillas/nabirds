import re

with open('../parts/part_locs.txt', 'r') as f:
    texto = f.read()

pattern = r"^(.+?)\s+(.+)$"
replace_txt = r"\1,\2"

texto_convertido = re.sub(pattern, replace_txt, texto, flags=re.MULTILINE)

print(texto_convertido)

with open('parts/part_locs.csv', 'w') as f:
    f.write(texto_convertido)