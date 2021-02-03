# 1 - Workbench ide ile schooldb isminde database oluşturup student tablosunu oluşturunuz
    # id, student_number, name, surname, birth_date, gender

# 2 - Database baglantısını oluşturunuz

# 3 - Aşagıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz
    # (101, "Ahmet", "Yılmaz", datetime.datetime(2005, 5, 17), "E")
    # (102, "Ali", "Can", datetime.datetime(2005, 6, 17), "E")
    # (103, "Canan", "Tan", datetime.datetime(2005, 7, 7), "K")
    # (104, "Ayşe", "Taner", datetime.datetime(2005, 9, 23), "K")
    # (105, "Bahadır", "Toksöz", datetime.datetime(2004, 7, 27), "E")
    # (106, "Ali", "Cenk", datetime.datetime(2003, 8, 25), "E")

# 4 - Aşagıdaki sorguları yazınız
#   a - Tüm ögrenci kayıtlarını alınız
#   b - Tüm ögrencilerin sadece ögrenci no, ad ve soyad bilgilerini alınız
#   c - Sadece kız ögrencilerin ad ve soyad bilgilerini alınız
import mysql.connector
from datetime import datetime
from connection import connection # database baglantısı 

class student: 
    connection = connection
    my_cursor = connection.cursor()
    
    def __init__(self, id, student_number, name, surname, birth_date, gender):
        if id is None: ## eger id belirtilmediyse
            self.id = 0
        else:
            self.id = id
            self.student_number = student_number
            self.name = name
            self.surname = surname
            self.birth_date = birth_date
            self.gender = gender

    def save_student(self):
        sql = "Insert Into student(student_number, name, surname, birth_date, gender) values (%s,%s,%s,%s,%s)"
        values = (self.student_number, self.name, self.surname, self.birth_date, self.gender)
        student.my_cursor.execute(sql, values)

        try:
            student.connection.commit()
            print(f"{student.my_cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print(f"Hata :{err}")
        finally:
            student.connection.close()

    @staticmethod
    def save_students(students):
        sql = "Insert Into student(student_number, name, surname, birth_date, gender) values (%s,%s,%s,%s,%s)"
        values = students
        student.my_cursor.executemany(sql, values)

        try:
            student.connection.commit()
            print(f"{student.my_cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print(f"Hata :{err}")
        finally:
            student.connection.close()

# 4 - Aşagıdaki sorguları yazınız
#   a - Tüm ögrenci kayıtlarını alınız
#   b - Tüm ögrencilerin sadece ögrenci no, ad ve soyad bilgilerini alınız
#   c - Sadece kız ögrencilerin ad ve soyad bilgilerini alınız
#   d - 2003 doğumlu ögrencilerin bilgilerini alınız
#   e - İsmi ali ve dogum tarihi 2005 olan ögrenci bilgilerini alınız
#   f - ad veya soyad içinde "an" ifadesi geçen kayıtları alınız
#   g - Kaç erkek ögrenci vardır ?
#   h - Kız ögrencileri harf sırasına göre getiriniz

    @staticmethod
    def student_info(): 
        # sql = "select * from student" # a
        # sql = "select student_number,name,surname from student" # b
        # sql = "select name,surname from student where gender = 'k'" # c
        # sql = "select * from student where year(birth_date) = 2003" # d ## dogum günü bilgisinin sadece yılını alır => year()
        # sql = "select * from student where name = 'Ali' and year(birth_date) = 2005" # e
        # sql = "select * from student where name like '%an%' or surname like '%an%'" # f
        # sql = "select * from student where gender = 'e'" # g
        # sql = "select count(*) from student where gender = 'e'" # g
        # sql = "select * from student where gender = 'k' order by name,surname" # h
        sql = "select * from student limit 5" ## ilk 5 kayıt gelir 
        student.my_cursor.execute(sql)

        try:
            # results = student.my_cursor.fetchone()
            # print(results)
            results = student.my_cursor.fetchall()
            for x in results:
                print(x)
        except mysql.connector.Error as err:
            print(f"hata :{err}")
        finally:
            student.connection.close()
            print("Database baglantınız kesildi")

# 5 - Aşağıdaki güncelleme sorularını yapınız
#   a - id' ye göre aldıgınız bir ögrencinin bilgilerini güncelleyiniz
#   b - cinsiyete göre aldıgınız bir ögrencinin bilgilerini güncelleyiniz
    @staticmethod
    def get_student_by_id(id):
        sql = "select * from student where id = %s"
        values = (id,)
        student.my_cursor.execute(sql, values)

        try:
            obj = student.my_cursor.fetchone()
            return student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print(f"hata :{err}")
        

    def update_student(self):
        sql = "update student set student_number =%s, name =%s, surname =%s, birth_date =%s, gender =%s where id =%s"
        values = (self.student_number, self.name, self.surname, self.birth_date, self.gender, self.id)
        student.my_cursor.execute(sql, values)

        try:
           student.connection.commit()
           print(f"{student.my_cursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print(f"hata :{err}")
        
    @staticmethod
    def get_student_gender(gender):
        sql = "select * from student where gender = %s"
        values = (gender,)
        student.my_cursor.execute(sql, values)

        try:
            return student.my_cursor.fetchall()
           
        except mysql.connector.Error as err:
            print(f"hata :{err}")

    @staticmethod
    def update_students(liste):
        sql = "update student set student_number =%s, name =%s, surname =%s, birth_date =%s, gender =%s where id =%s"
        values = []
        order = [1,2,3,4,5,0]
        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        student.my_cursor.executemany(sql, values)

        try:
           student.connection.commit()
           print(f"{student.my_cursor.rowcount} tane kayıt güncellendi")
        except mysql.connector.Error as err:
            print(f"hata :{err}")

Student = student.get_student_gender("E")
print(Student)
liste = []
for std in Student:
    std = list(std)
    std[2] = 'Mr' + std[2]
    liste.append(std)

student.update_students(liste)
# stdnt = student.get_student_by_id(5)
# # print(obj)
# stdnt.name = "Barış"
# stdnt.surname = "Kurt"
# stdnt.update_student()
# student.student_info()
# ahmet = student("202","Ahmet", "Yılmaz",datetime(2005, 5, 17),"e")
# ahmet.save_student()

# students = [
#     (301, "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E"),
#     (302, "Ali", "Can", datetime(2005, 6, 17), "E"),
#     (303, "Canan", "Tan", datetime(2005, 7, 7), "K"),
#     (304, "Ayşe", "Taner", datetime(2005, 9, 23), "K"),
#     (305, "Bahadır", "Toksöz", datetime(2004, 7, 27), "E"),
#     (306, "Ali", "Cenk", datetime(2003, 8, 25), "E")
# ]
# student.save_students(students)
# my_cursor.executemany(sql, students)

# try:
#     connection.commit()
#     print(f"{my_cursor.rowcount} tane kayıt eklendi.")
# except mysql.connector.Error as err:
#     print(f"Hata :{err}")
# finally:
#     connection.close()