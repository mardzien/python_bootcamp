from faker import Faker

fake = Faker("pl_Pl")

print(fake.name())
print(fake.text(25))
print(fake.ascii_free_email())
print(fake.words(3))
print(fake.opera())
print(fake.user_name())
print(fake.random_int())
print(dir(fake))
