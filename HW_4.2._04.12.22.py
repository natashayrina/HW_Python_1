# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def get_koeffs_from_file(file_path):
    file = open(file_path, "r")
    line = file.readline()
    file.close()

    slogaemie = line.split("+")
    koeffs = []
    for i in range(0, len(slogaemie) - 1):
        elems = slogaemie[i].split("*")
        koeffs.append(int(elems[0]))

    koeffs.append(int(slogaemie[-1]))

    return koeffs

koeffs_1 = get_koeffs_from_file("output.txt")
koeffs_2 = get_koeffs_from_file("output_1.txt")

# print(koeffs_1)
# print(koeffs_2)


file = open("output.txt", "r")
line = file.readline()
file.close()

file = open("output_1.txt", "r")
line_1 = file.readline()
file.close()

print(line)
print(line_1)


koeffs_itog = [x + y for x, y in zip(koeffs_1, koeffs_2)]

# print(koeffs_itog)

file_out = open("out.txt", "w")
str_res = ""
for i in range(len(koeffs_itog) - 1):
    str_res += str(koeffs_itog[i])
    str_res += '*x**' + str(len(koeffs_itog) - i - 1) + ' + '

str_res += str(koeffs_itog[-1])
print(str_res)
file_out.write(str_res)
file_out.close()








