text = "Zażółć gęślą jaźń"

with open("logs.txt", "w") as f:
    for l in text:
        f.write(l+"\n")
