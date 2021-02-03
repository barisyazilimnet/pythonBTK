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

    cursor.execute("select * from products order by price desc") ## ASC => standart artan sırlama // DESC => azalan sıralama
    # cursor.execute("select * from products order by name") ## /order by /kolona göre sıralama 
    # cursor.execute("select * from products where name = 'Samsung S6' and price > 1000") 
    ## select /secmek istedigim kolonlar (hepsini secmek için * konulmalıdır) /from /seçmek istediginiz tablo ismi /where / filtre (and veya or) operatorü kullanılarak filtreler birleştirebilir
    ## cursor.execute("select * from products where name like '%Samsung%'") ## where /aranmak istenen kolon /like /'%arancak kelime%' ## içinde 'aranak kelime geçen bütün degerler'
    ## cursor.execute("select * from products where name like 'Samsung%'") ## where /aranmak istenen kolon /like /'arancak kelime%' ## 'aranacak kelime ile başlayan degerler'
    ## cursor.execute("select * from products where name like '%Samsung'") ## where /aranmak istenen kolon /like /'%arancak kelime' ## 'aranacak kelime ile biten degerler'
    ## cursor.execute("select * from products where name like '%Samsung' and price = 3000")
    # cursor.execute("select name,price from products")

    # print(cursor.fetchone()) ## buldugu ilk kaydı getirir
    
    for x in cursor.fetchall(): ## fetchall() bütün kayıtlar gelir
    #     # print(x[1])
        print(x)

def get_products_by_id(id):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "159753",
        database = "node-app"
    )
    cursor = connection.cursor()

    sql ="select * from products where id = %s"
    params = (id,)
    cursor.execute(sql, params)

    x = cursor.fetchone()
    print(f"id :{x[0]} name :{x[1]} price :{x[2]}") 

get_products()