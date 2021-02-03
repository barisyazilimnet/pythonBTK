import mysql.connector

def insert_product(name, price, img_url, description):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "159753",
        database = "node-app"
    )
    cursor = connection.cursor()

    sql = "Insert Into Products (name, price, img_url, description) Values (%s,%s,%s,%s)" ## /insrt into /tablo ismi /kolon isimleri
    values = (name, price, img_url, description)

    cursor.execute(sql, values) 
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"Son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f"hata :{err}")
    finally:
        connection.close()
        print("Database baglantısı kesildi")

def insert_products(list):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "159753",
        database = "node-app"
    )
    cursor = connection.cursor()

    sql = "Insert Into Products (name, price, img_url, description) Values (%s,%s,%s,%s)" ## /insrt into /tablo ismi /kolon isimleri
    values = list
    cursor.executemany(sql, values) 
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi")
        print(f"Son eklenen kaydın id: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print(f"hata :{err}")
    finally:
        connection.close()
        print("Database baglantısı kesildi")

def get_products():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "159753",
        database = "node-app"
    )
    cursor = connection.cursor()

    # cursor.execute("select * from products") ## select /secmek istedigim kolonlar (hepsini secmek için * konulmalıdır) /from /seçmek istediginiz tablo ismi
    cursor.execute("select name,price from products")

    print(cursor.fetchone()) ## buldugu ilk kaydı getirir
    
    # for x in cursor.fetchall(): ## fetchall() bütün kayıtlar gelir
    #     # print(x[1])
    #     print(x)

get_products()