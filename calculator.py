############################
# protein 1g/4cal          #
# fat     1g/9cal          #
# carbohydrate 1g/4cal     #
############################


TDEE=float(input("Please input your TDEE:"))
weight=float(input("Please input your weight in kg:"))

#每天攝取蛋白質的公克數
low_protein_g=round(float(weight*2.3))
hight_protein_g=round(float(weight*2.8))
print("protein per day:",low_protein_g,"~",hight_protein_g,"g")

#每天攝取脂肪的公克數
low_fat=float(TDEE*15/100)
hight_fat=float(TDEE*25/100)
print("fat per day:",round(low_fat/9),"~",round(hight_fat/9),"g")

#碳水化合物
carbohydrate_list=[]
carbohydrate_list.append(round((TDEE-(low_protein_g*4)-low_fat)/4))
carbohydrate_list.append(round((TDEE-(low_protein_g*4)-hight_fat)/4))
carbohydrate_list.append(round((TDEE-(hight_protein_g*4)-low_fat)/4))
carbohydrate_list.append(round((TDEE-(hight_protein_g*4)-hight_fat)/4))
print("carbohydrate per day",min(carbohydrate_list),"~",max(carbohydrate_list),"g")


