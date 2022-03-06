from powitanie import *
wiek= int(input("podaj swój wiek:  "))
plec=input("kobieta czy mezczyzna:  ")
while plec!= "kobieta" or plec!= "mężczyzna":
    plec = input("napisz kobieta albo mężczyzna:  ")
    break
aktywnosc_ruchowa= int(input("ocen swoja aktywnosc ruchowa od 0 do 100:  "))
powitanie(wiek, plec, aktywnosc_ruchowa)