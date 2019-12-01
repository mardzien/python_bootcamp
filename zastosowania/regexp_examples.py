import re

test_data = """111 111 111;123 23 123;123 123 123;23 23 23;999 999 999"""
test_data3 = """123 23 123;123 123 123;23 23 23;999 999 999"""
test_data2 = "123 123 123"

phone_pattern = "\d{3} (?:\d{3}) \d{3}"

pattern = re.compile(phone_pattern)
print(pattern.match(test_data))
print(pattern.search(test_data3))
print(pattern.findall(test_data))
print(pattern.finditer(test_data))
