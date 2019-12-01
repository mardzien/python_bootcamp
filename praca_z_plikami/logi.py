
# wersja 1

def print_total_time(user_total_time):
    for user, tt in sorted(user_total_time.items(), key=lambda x: x[1], reverse=True):
        print(f"- {user}: {tt}")

def zlicz_czasy_1(file_name):
    sum_login_time = {}
    sum_logout_time = {}

    with open(file_name) as f:
        for line in f:
            name, action, current_time = line.strip().split(";")
            current_time = int(current_time)
            if action == "LOGIN":
                sum_login_time[name] = sum_login_time.get(name, 0) + current_time
            if action == "LOGOUT":
                sum_logout_time[name] = sum_logout_time.get(name, 0) + current_time

    user_total_time = {}

    for user in sum_logout_time:
        user_total_time[user] = sum_logout_time[user] - sum_login_time[user]

    print_total_time(user_total_time)

def zlicz_czasy_2(file_name):

    last_login_time = {}
    user_total_time = {}
    with open(file_name) as f:
        for line in f:
            name, action, current_time = line.strip().split(";")
            current_time = int(current_time)
            if action == "LOGIN":
                last_login_time[name] = current_time
            if action == "LOGOUT":
                user_total_time[name] = user_total_time.get(name, 0) + current_time - last_login_time[name]
    print_total_time(user_total_time)

class User:
    def __init__(self, name):
        self.name = name
        self.last_login_time = 0
        self.total_time = 0

    def set_last_login_time(self, t):
        self.last_login_time = t

    def incr_total_time(self, t):
        self.total_time += t - self.last_login_time

class Users:

    def __init__(self):
        self.users = {}

    def zlicz_czasy(self, file_name):

        with open(file_name) as f:
            for line in f:
                name, action, current_time = line.strip().split(";")
                if name in self.users:
                    user = self.users[name]
                else:
                    user = User(name)
                    self.users[name] = user
                current_time = int(current_time)
                if action == "LOGIN":
                    self.users[name].set_last_login_time(current_time)
                elif action == "LOGOUT":
                    self.users[name].incr_total_time(current_time)

    def print_times(self):
        user_total_time = {name: self.users[name].total_time for name in self.users}
        print_total_time(user_total_time)


if __name__ == "__main__":
    import sys
    print(sys.argv)

    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = None
        print("""Podaj nazwe pliku który ma być analizowany
Użycie: 
python logi.py nazwa_pliku        
""")

    if file_name:
        zlicz_czasy_1(file_name)
        print()
        zlicz_czasy_2(file_name)
        print()
        users = Users()
        users.zlicz_czasy(file_name)
        users.print_times()



