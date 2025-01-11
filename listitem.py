listfruit=["orange","apple","banana","pineapple","mango","pawpaw","groundnut"]
listme=["orange","yam","chiz","chiz","pineapple","pineapple","mango","pawpaw","groundnut"]

for i in listfruit:
    if i=="orange":
        print(i)
        listfruit.remove(i)
        
print(listfruit)