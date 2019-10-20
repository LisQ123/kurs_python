# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
#
# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""

dict = {}
wiersz = "Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce"

txt = list(wiersz.replace(",", " ").lower().split())
for x in txt:
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1
print(dict)
for keys, values in dict.items():
    print(keys+":", values)