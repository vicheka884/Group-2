fruits = [
    {"name": "apple","qty":2,"price":20},
    {"name": "banana","qty":0,"price":30},
    {"name": "pine Apple","qty":0,"price":40},
    {"name": "wood apple","qty":2,"price":10},
]
# arr=[]
# for i in range(len(fruits)):
#     if fruits[i]['qty']==0:
#         arr.append(fruits[i]['name'])
# print(f"expected result:{arr}")
# arr=[]
# for i in range(len(fruits)):
#     if fruits[i]['price']<=20:
#         arr.append(fruits[i]['name'])
# print(f"expected result:{arr}")
newArry=[]
for fruit in fruits:
    if fruit['qty']==0:
        fruit['qty'] = 5
        print(fruit)
    else:
        print(fruit)