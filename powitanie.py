def powitanie (wiek, plec, aktywnosc_ruchowa):
    if plec== "kobieta":
        if wiek<25 and aktywnosc_ruchowa>80:
            return print ("Hej dziewczyno")
        elif wiek<25 and aktywnosc_ruchowa <=80:
            return print ("hej dziewczyno , chodź pobiegać!!!!!")
        elif wiek>25 and wiek<50 and aktywnosc_ruchowa>80:
            return print ("witam Cie serdecznie")
        elif wiek>25 and wiek<50 and aktywnosc_ruchowa<=80:
            return print ("witam Cię serdecznie ruszamy się?")
        elif wiek>50 and aktywnosc_ruchowa>80:
            return print ("witam Panią")
        elif wiek>50 and aktywnosc_ruchowa<=80:
            return print ("Witam Panią, idziemy na spacer:)")
    elif plec=="mężczyzna":
        if wiek<20 and aktywnosc_ruchowa >80:
            return print ("Paka")
        elif wiek<20 and aktywnosc_ruchowa<=80:
            return print ("Paka, wyłaź z domu!")
        elif wiek>20 and wiek<49 and aktywnosc_ruchowa>80:
            return print ("Trzym się Chłopie")
        elif wiek>20 and wiek<49 and aktywnosc_ruchowa<=80:
            return print ("Chłopie na spacer marsz!")
        elif wiek>49 and aktywnosc_ruchowa>80:
            return print ("Witam Pana")
        elif wiek>49 and aktywnosc_ruchowa<=80:
            return print ("Witam Pana dbajmy o zdrowie :)")
    return print ("dane które podałeś były niepoprawne")
