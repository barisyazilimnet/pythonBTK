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


list = []
while True:
    name = input("Ürün adı: ")
    price = float(input("Ürün fiyatı: "))
    img_url = input("Ürün resim adresi: ")
    description = input("Ürün açıklaması: ")
    list.append((name, price, img_url, description))

    result = input("Devam etmek istiyor musunuz? (e/h")
    if result == "h":
        print("Kayıtlarınız veritabanına aktarılıyor...")
        print(list)
        insert_products(list)
        break

# insert_product(name, price, img_url, description)