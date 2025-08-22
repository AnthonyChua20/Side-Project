Sugar = 1.5
Butter = 1
Flour = 2
TotalCookies = 48
SingleSugar = Sugar / TotalCookies
SingleButter = Butter / TotalCookies    
SingleFlour = Flour / TotalCookies

NoOfCookies = int(input("How many cookies do you want to make? "))
TotalSugar = SingleSugar * NoOfCookies
TotalButter = SingleButter * NoOfCookies   
TotalFlour = SingleFlour * NoOfCookies
print("To make", NoOfCookies, "cookies you will need:")
print(round(TotalSugar,2), "cups of sugar")
print(round(TotalButter,2), "cups of butter")
print(round(TotalFlour,2), "cups of flour")

