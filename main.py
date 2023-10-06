#h=5
#a = input("napishi chislo" " " ":" " ")
#print(a)
#if a==str:
#    print("vvedite chislo")
#elif a==int:
#    print("da")
#else:
#    print("net")

# num1=[1,2,3,4,5,6,7,8,9,10]
# num2=list('gjvjygk')
# print(num1,"   ",num2)
# print(num1[0])
# print(num1[1])
# print(num1[-1])
# message=f"me {num2[0].title()}"
# print(message)
#
# for num3 in num1:
#     print(num3)
# print("                                                                                          ")
#
#
# i=0
# while i < len(num1):
#     print(num1[i])
#     i+=1
#
# #list[:end]
# #list[start:end]
# #list[start:end:step]
#
# nums1= num1[:3]
# print(nums1,"      ")
# nums2= num1[1:3]
# print(nums2,"     ")
# nums3= num1[1:5:2]
# print(nums3,"      ")
#
#
# num4=[1,2,1,3,1,4,1]
# num_count=num4.count(1)
# print(num_count)
#
# motor=['hond','yamaha','suzuki']
# print(motor)
# motor[0]='minsk'
# print(motor)
# motor.append('ducati')
# print(motor)

#git add .
#git commit -m "main"
#git push
# в терминал писать--------важно

# motor.insert(0,"bmw")
# print(motor)
# del motor[2]
# print(motor)
#
# index= motor.index("minsk")
# print(index)
# index2=motor.index("bmw",0)
# print(index2)
# popy=motor.pop(1)
# print(motor)
# motor.remove("bmw")
# print(motor)
# cars=["bmw","mersedes","subaru","toyota","audi"]
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# a=5
# b=7
# print("Обратите внимание сейчас будет пояснение по знакам в калькулятуре")
# print('Знак сложения +')
# print('Знак вычетания -')
# print('Знак умножения *')
# print('Знак деления :')
# input=input("введите знак ")
# if input=="+" :
#     print("Ответ : ", a+b)
# elif input=="-" :
#     print("Ответ : ", a-b)
# elif input=="*" :
#     print("Ответ : ", a*b)
# elif input==":" :
#     print("Ответ : ", a/b)
# elif input==int:
#     print("Введите знак,а не число")
# else:
#     print("У вас ошибка при вводе,перезапустите программу ")


shopping_list=[]
shopping_list.append('яблоко')
shopping_list.append('молоко')
shopping_list.append('хлеб')
shopping_list.append('яйца')
shopping_list.append('сок')
print(shopping_list)
i=0
while i < len(shopping_list):
     print(shopping_list[i])
     i+=1
del shopping_list[1]
shopping_list[0]="банан"
print(shopping_list)
z=0
while z < len(shopping_list):
     z+=1

print(z)



