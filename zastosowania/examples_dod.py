text = "Zażółć gęślą jaźń"
with open("text.txt", "wb") as f:
    f.write(text.encode())


with open("text.txt", "rb") as f:
    print(f.read().decode())


# # 1110 0011
# print(256 * 256 * 256 * 259)
#
# # 01011

