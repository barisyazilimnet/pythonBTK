import pandas as pd

# customers = {
#     "Customer_id" : [1,2,3,4],
#     "First_name" : ["Ahmet","Ali","Hasan","Canan"],
#     "Last_name" : ["Yılmaz","Korkmaz","Çelik","Toprak"]
# }

# orders = {
#     "Order_id" : [10,11,12,13],
#     "Customer_id" : [1,2,5,7],
#     "Order_date" : ["2010-07-04","2010-08-04","2010-09-04","2010-10-04"]
# }

# df_customers = pd.DataFrame(customers, columns = ["Customer_id","First_name","Last_name"])
# df_orders = pd.DataFrame(orders, columns = ["Order_id","Customer_id","Order_date"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers, df_orders, how = "inner") ## sadece eşi olan kayıtlar gelir yani müsteri numaraları tutan kayıtlar gelir
# result = pd.merge(df_customers, df_orders, how = "left") ##  müsterilerin hepsi gelir ama sipariş bilgileri bulunmayan müşteriye nan yazar siparişte müşteri bilgileryile uyuşanlar gelir
# result = pd.merge(df_customers, df_orders, how = "right") ## butun sipariş bilgileri gelir siparişler arasında müşteri bilgileri bulunmayan varsa nan yazar müşterilerdede şipariş bilgleriyle uyuşanları getirir
# result = pd.merge(df_customers, df_orders, how = "outer") ## kayıtların eşleşmesede bütün kayıtları getirir
# print(result)

customers_a = {
    "Customer_id" : [1,2,3,4],
    "First_name" : ["Ahmet","Ali","Hasan","Canan"],
    "Last_name" : ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customers_b = {
    "Customer_id" : [5,6,7,8],
    "First_name" : ["Veli","Yağmur","Barış","Can"],
    "Last_name" : ["Bilgi","Kurt","Yılmaz","Turan"]
}

df_customers_a = pd.DataFrame(customers_a, columns = ["Customer_id","First_name","Last_name"])
df_customers_b = pd.DataFrame(customers_b, columns = ["Customer_id","First_name","Last_name"])

result = pd.concat([df_customers_a,df_customers_b]) ## birleştirme işlemi ## axis = 0 dır altına eklenir
result = pd.concat([df_customers_a,df_customers_b], axis = 1) ## birleştirme işlemi ## axis = 1 dır yanına eklenir

print(result)