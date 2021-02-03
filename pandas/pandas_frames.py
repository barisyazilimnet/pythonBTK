import pandas as pd

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1, oranges = s2)
# df = pd.DataFrame(data)

# print(df)

# df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
data = [["Ahmet",50],["Ali",60],["Barış",100],["Yağmur",70]]
dict = {"name" : ["Ahmet","Ali","Barış","Yağmur"], "grade": [50,60,70,80]}
dict_list = [
    {"Name" : "Ahmet","Grade" : 50},
    {"Name" : "Ali","Grade" : 60},
    {"Name" : "Yağmur","Grade" : 70},
    {"Name" : "Barış","Grade" : 80},
    ]
# df = pd.DataFrame(data, columns = ["name","grade"], index = [1,2,3,4], dtype = float)
# df = pd.DataFrame(data,[1,2,3,4], ["name","grade"]) ## eger parametre isimleri verilmezse sırlama önemli
# df = pd.DataFrame(dict)
# df = pd.DataFrame(dict, index = ["212","232","236","456"])
# df = pd.DataFrame(dict_list)
df = pd.DataFrame(dict_list, index = ["212","232","236","456"])
print(df)