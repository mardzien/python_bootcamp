from faker import Faker


fake = Faker("pl_PL")

print(fake.name())
print(fake.ascii_free_email())
print(dir(fake))