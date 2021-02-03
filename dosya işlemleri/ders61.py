def calculate_note(line):
    line = line[:-1]
    liste = line.split(":")
    
    name = liste[0]
    notes = liste[1].split(",")

    note1 = int(notes[0])
    note2 = int(notes[1])
    note3 = int(notes[2])

    average = int((note1 + note2 + note3)/3)
    
    if average >= 84 and average <= 100:
        letter ="AA"
    elif average >= 77 and average <= 83:
        letter ="AB"
    elif average >= 71 and average <= 76:
        letter ="BA"
    elif average >= 66 and average <= 70:
        letter ="BB"
    elif average >= 61 and average <= 65:
        letter ="BC"
    elif average >= 56 and average <= 60:
        letter ="CB"
    elif average >= 50 and average <= 55:
        letter ="CC"
    elif average >= 46 and average <= 49:
        letter ="CD"
    elif average >= 40 and average <= 45:
        letter ="DC"
    elif average >= 33 and average <= 39:
        letter ="DD"
    elif average >= 0 and average <= 32:
        letter ="FF"

    return name +" :"+ letter +"\n"

def read_averages():
    with open("sinav_notlari.txt", encoding="utf-8") as file:
        for line in file:
            print(calculate_note(line))

def insert_note():
    name = input("Öğrenci adı :")
    surname = input("Öğrenci soyadı :")
    note1 = input("Not 1:")
    note2 = input("Not 2:")
    note3 = input("Not 3:")

    with open("sinav_notlari.txt", "a", encoding="utf-8") as file:
        file.write(name +" "+ surname +":"+ note1 +", "+ note2 +", "+ note3 +"\n")

def save_notes():
    with open("sinav_notlari.txt", encoding="utf-8") as file:
        liste =[]

        for i in file:
            liste.append(calculate_note(i))

        with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    process = input("1- Notları Oku \n2- Notları Gir \n3- Notları Kayıt Et \n4- Çıkış\n")

    if process == "1":
        read_averages()
    elif process == "2":
        insert_note()
    elif process == "3":
        save_notes()
    else:
        break
