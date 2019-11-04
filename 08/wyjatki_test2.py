import sys

try:
    x = float(input("podaj liczbe"))
    result = 4/x

except Exception as e:  # nazwa moze byc dowolna, zamiast e cokolwiek
    print("Blad to:", sys.exc_info()[0])  # zamiast sys.exc_info()[0] moze byc np type(e)


