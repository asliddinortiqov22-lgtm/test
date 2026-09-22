# mening_fayilim = open("fayl.txt")
# print(mening_fayilim.read())
# mening_fayilim.close()



# with open("fayl.txt") as mening_fayilim:
#     print(mening_fayilim.read())






# with open("fayl.txt") as meni:
#     print(meni.readline())
#     print(meni.readline())
#     print(meni.readline())




# with open("fayl.txt") as meni:
#     for y in meni:
#         print(y)





# with open("fayl.txt", "a") as meni:
#     meni.write("Endi faylda koproq matn bor !")


# with open("fayl.txt") as meni:
#     print(meni.read())








# with open("fayl.txt", "w") as meni:
#     meni.write("Voy ! men mazmunni ochirib tashladim!")


# with open("fayl.txt") as meni:
#     print(meni.read())





# import os 
# os.remove("fayl.txt")




# import os 
# if os.path.exists("fayl.txt")
#     os.remove("fayl.txt")
# else:
#     print("Fayl mavjud emas")    












# with open("salom.txt", "w") as meni:
#     meni.write("Salom, Python!")


# with open("salom.txt") as meni:
#     print(meni.read())









# with open("kundalik.txt", "a") as meni:
#     meni.write("Bugun Pyhton organdim. \n")

# with open("kundalik.txt", "a") as meni:
#     meni.write("Sikllarni ham organdim. \n")    


# with open("kundalik.txt") as meni:
#     for x in meni:
#         print(meni.readline())












# import os 
# if os.path.exists("vaqtinchalik.txt"):
#     os.remove("vaqtinchalik.txt")
# else:
#     print("Fayl mavjud emas")    








# import os
# if os.path.exists("vaqtinvhalik.txt"):
#     os.remove("vaqtinchalik.txt")
# else:
#     print("Bunday fayl mavjud emas")    






# with open("sonlar.txt", "r") as exe:
#     jami=0
#     for x in exe:
#         jami += int(x)
#     print(jami)    




# with open("matn.txt", "r") as exe:
#     for x in exe:
#         print(x.upper())    


c = 0
k = 0

with open("sonlar.txt", "r") as exe:
   

    for x in exe:
        if int(x) > k:
            k = int(x)
        elif x < c:
            c = int(x)
    print(k,c)    

