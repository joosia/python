'''
+------------------+
|..................|
|..................|
|..................|
|..................|
|..................|
|..................|
|..................|
|..................|
+------------------+
'''

hori = "-"
vert = "|"
corn = "+"
fill = "."
mult = 18

print corn, hori * mult, corn
for i in range(0,8):
    print vert, fill * mult, vert
print corn, hori * mult, corn