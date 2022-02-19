f = open("test.txt", 'w')

f.write("hiafdsfdsa \n")
f.write("hiiiiii")

f.close()

f = open("test.txt", 'r')

lines = f.readlines()

print(lines)

f = open("adf", 'a')

