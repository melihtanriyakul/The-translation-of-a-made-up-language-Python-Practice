import string
import sys
dictionary = sys.argv[1]
binarian_transmission = sys.argv[2]
peace_message = sys.argv[3]

myfile = open(dictionary, "r")
myfile1 = open(binarian_transmission, "r")
myfile2 = open(binarian_transmission, "r")
myfile3 = open(dictionary, "r")
myfile4 = open(peace_message, "r")
output = open("binarian_message.txt", "w")
output2 = open("calculations.txt", "w")
output3 = open("message.txt", "w")

d = {}
k = {}
list1 = []


def read_dictionary(file):
    for line in file.readlines():
        a = line.split(" ")
        d[a[0]] = a[1]


def read_dictionary1(file):
    for line in file.readlines():
        b = line.split(" ")
        k[b[1]] = b[0]


def binarian_to_english(text):
    for line in text.readlines():
        line = line.strip("\n")
        list_items = line.split(" ")
        for i in list_items:
            if i[0] == "#":
                break
            elif i[0] == "+":
                break
            elif i not in d:
                if (list_items.index(i)) == len(list_items) - 1:
                    print(i)
                    output.write(i)
                else:
                    print(i, end=" ")
                    output.write(i + " ")
            else:
                if (list_items.index(i)) == len(list_items) - 1:
                    print(d[i])
                    output.write(d[i])
                else:
                    print(d[i], end=" ")
                    output.write(d[i] + " ")
        if list_items[0][0] != "+"and list_items[0][0] != "#":
            output.write("\n")
    print("")


def english_to_binarian(text):
    for line in text.readlines():
        for a in string.punctuation:
            line = line.replace(a, "")
        line = line.strip("\n")
        list_items = line.split(" ")
        for i in list_items:
            if i.isdigit():
                a = decimal_to_binary(int(i))
                if (list_items.index(i)) == len(list_items) - 1:
                    print(a)
                    output3.write(str(a))
                else:
                    print(a, end=" ")
                    output3.write(str(a) + " ")
            elif i.lower() not in k:
                if (list_items.index(i)) == len(list_items) - 1:
                    print(i)
                    output3.write(i)
                else:
                    print(i, end=" ")
                    output3.write(i + " ")
            else:
                if (list_items.index(i)) == len(list_items) - 1:
                    print(k[i])
                    output3.write(k[i])
                else:
                    i = i.lower()
                    print(k[i], end=" ")
                    output3.write(k[i] + " ")
        output3.write("\n")
    print("")


def binary_to_decimal(value):
    total = 0
    count = 1
    while value >= 1:
        a = value % 10
        total += (a * count)
        count *= 2
        value //= 10
    return total


def decimal_to_binary(value):
    exponent = 0
    total = 0
    while value > 0:
        remainder = value % 2
        remainder *= (10 ** exponent)
        total += remainder
        exponent += 1
        value //= 2
    return total


def decimal_to_scientific(value):
    count = 0
    while value >= 10:
        value /= 10
        count += 1
    return str(value) + "e+" + str(count)


def ly_to_km(text):
    a = text.split("e")
    b = float(a[0])
    c = int(a[1])
    total = b * (10 ** c)
    return total


def data_about_binarian_planet(text):
    print("Data about Binarian planet:")
    output2.write("Data about Binarian planet:\n")

    for line in text.readlines():
        line = line.rstrip("\n")
        list_items = line.split(" ")

        for j in list_items:
            if j[0] == "+":
                if "chuqD" in list_items:
                    c = list_items.index("chuqD")
                    z = binary_to_decimal(int(list_items[c+1])) * ly_to_km("9.4607e+12")
                    list1.insert(0, z)
                if "Hata" in list_items:
                    a = list_items.index("Hata")
                    x = binary_to_decimal(float(list_items[a+1]))
                    list1.insert(1, x)
                if "bav'Do" in list_items:
                    b = list_items.index("bav'Do")
                    y = binary_to_decimal(float(list_items[b+1]))
                    list1.insert(2, y)
    print("Distance from the Earth: " + str(decimal_to_scientific(list1[0])) + " km")
    output2.write("Distance from the Earth: " + str(decimal_to_scientific(list1[0])) + " km\n")
    print("Planet temperature: " + str(list1[1]) + " degrees Celsius")
    output2.write("Planet temperature: " + str(list1[1]) + " degrees Celsius\n")
    print("Orbital speed: " + str(list1[2]) + " km/s")
    output2.write("Orbital speed: " + str(list1[2]) + " km/s")
    print("")

read_dictionary(myfile)
binarian_to_english(myfile1)
data_about_binarian_planet(myfile2)
read_dictionary1(myfile3)
english_to_binarian(myfile4)

myfile.close()
myfile1.close()
myfile2.close()
myfile3.close()
myfile4.close()
output.close()
output2.close()
output3.close()
