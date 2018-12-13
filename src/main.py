c1 = "Fizz"
c2 = "Buzz"
r1 = 3
r2 = 5
cr = ""
count = 0
try:
    limit = int(input("Limit:\n>"))
except:
    limit = 100

while (count <= limit):
    count += 1
    cr = ""
    if (count%r1)==0:
        cr += c1
    if (count%r2)==0:
        cr += c2
    if(cr == ""):
        cr = str(count)
    print (cr)
input()
