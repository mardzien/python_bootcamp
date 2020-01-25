
# try:
#     f = open("nazwa_pliku.txt")
#     1/0
# except:
#     pass
# finally:
#     f.close()

# context manager
with open("logs.txt", encoding="utf-8") as fh:
    print(fh.read())


# print(fh)
#
# with open("text.txt", 'w') as fh:
#     fh.write("AAAAAAAAAAAXXXXXX")
#     fh.seek(0)
#     fh.write('X')



#
# with open("nazwa_pliku.txt") as fh:
#     for line in fh:
#         print(line, end="")
#
# with open("nazwa_pliku.txt") as fh:
#     for line in fh.read().splitlines():
#         print(line)