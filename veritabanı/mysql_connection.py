import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", ## uygulama veya program yayınlandıgı zaman server hizmeti alıcanak ve server hizmetinde verilen ip adresi bura yazılacak
    user = "root",
    password = "159753",
    database = "node-app"
)

my_cursor = mydb.cursor()
# my_cursor.execute("Show Databases") ## veritabanındaki database leri görüntelemek için kullanılır
# my_cursor.execute("Create Database my_database")  ## veritabanında yeni database oluşturma ## create / database / ismi
# my_cursor.execute("Create Table custormes (name Varchar(255), address Varchar(255))") ## database de tablo oluşturmak için kullanılır ## create / table / ismi / özellikleri

