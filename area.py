#to find the area of 3 sides
Varside1 = float(input("Enter the First number: "))
Varside2 = float(input("Enter the Second number: "))
Varside3 = float(input("Enter the Third number: "))

Varsemiperi = (Varside1+Varside2+Varside3) / 2

print("The semiarea is",Varsemiperi)

Vaearea = (Varsemiperi* (Varsemiperi - Varside1) * (Varsemiperi - Varside2) * (Varsemiperi - Varside3)) ** 0.5
print("The area of the Triangle is: ", Vaearea)

