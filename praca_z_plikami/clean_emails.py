

with open("emails.txt") as f:
    cleaned_emails = set()
    for line in f:
        email = line.strip().lower()
        if email.count("@") == 1:
            cleaned_emails.add(email)
    for email in sorted(cleaned_emails):
        print(email)