import re

email_pattern = re.compile("[\w\.\-]+@(?:\w+\.)+\w+")
zip_code_pattern = re.compile("(?:^| )(\d{2}-\d{3})(?: |$)")
date_pattern = re.compile("\d{2} \w{3} \d{4}")

with open("input.txt") as f:
    text = f.read()
    print("emaile: ", email_pattern.findall(text))
    print("kody: ", zip_code_pattern.findall(text))
    print("daty: ", date_pattern.findall(text))


