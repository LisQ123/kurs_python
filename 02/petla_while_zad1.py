temp_f = 0
while temp_f >= 200:
    temp_c = 5/9 * (temp_f-32)  #wliczenie stopni cel
    temp_c = round(temp_c, 2)  # zaokraglanie do 2 miejsc
    print(temp_f, "F = ", temp_c, "C")
    temp_f = temp_f + 20  #aktualizacja