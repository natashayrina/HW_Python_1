# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

file = open("datas_for_compact.txt", "r")
s = file.readline()
file.close()

def encode(s):
    encoding = ""
    i = 0
    while i < len(s):
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1

        encoding += str(count) + s[i]
        i = i + 1

    return encoding

print(s)
message = encode(s)
print(message)

def decode(str):
    decoded_message = ""
    i = 0
    j = 0

    while i <= len(str) - 1:
        run_count = int(str[i])
        run_word = str[i + 1]

        for j in range(run_count):
            decoded_message = decoded_message+run_word
            j = j + 1
        i = i + 2
    return decoded_message

decoded_massage = decode(encode(s))
print(decoded_massage)
