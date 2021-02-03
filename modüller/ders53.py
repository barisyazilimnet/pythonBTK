import random

# result = dir(random)
# result = help(random)

result = random.random() # 0.0  -- 1.0 
result = random.random() * 100 
# result = random.uniform(1,10)
result = int(random.uniform(1,10))
result = random.randint(1,100)

greeting = "Barış KURT"
names =["Ali", "Yağmur", "Deniz", "Cenk"]
# result = names[random.randint(0, len(names)-1)] # names listesinden eleman seçer
result = random.choice(names)
result = random.choice(greeting)

liste = list(range(11))
random.shuffle(liste)
result = liste

liste = range(101)
result = random.sample(liste, 3)

print(result)