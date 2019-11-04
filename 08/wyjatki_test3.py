try:
    x = 5 / 0
except ZeroDivisionError as e:
    print("Nie dziel przez zero! Twoj wyjatek to:", e)
    x = 0

finally:
    print("zawsze sie wyswietle")

print(x + 4)
