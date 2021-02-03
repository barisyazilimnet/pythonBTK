"""students ={
    120 :{
        "ad" :"Ali",
        "surname" :"Yılmaz",
        "phone" :"532 000 000 01"
    }, 
    125 :{
        "name" :"Can",
        "surname" :"Korkmaz",
        "phone" :"532 000 000 02"
    },
    128 :{
        "name" :"Volkan",
        "surname" :"Yükselen",
        "phone" :"532 000 000 03"
    }
}"""

students ={}

number =input("Öğrenci no :")
name =input("Öğrenci ad :")
surname =input("Öğrenci soyad :")
phone =input("Öğrenci telefon :")

# students[number] ={
    # "name" : name,
    # "surname" : surname,
    # "phone" : phone
# }

students.update({
    number :{
        "name" : name,
        "surname" : surname,
        "phone" : phone
    }
})
print(students)

ogrno = input("Öğrenci no :")
student =students[ogrno]
print(student)