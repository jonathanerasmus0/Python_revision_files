class User:
    active_users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def activate(self):
        if self not in User.active_users:
            User.active_users.append(self)

    def deactivate(self):
        if self in User.active_users:
            User.active_users.remove(self)

    def is_active(self):
        return self in User.active_users

me = User("Keith", "keith@example.com")

print(f"Active: {me.is_active()} Active Users: {User.active_users}")

me.activate()

print(f"Active: {me.is_active()} Active Users: {User.active_users}")

me.deactivate()

print(f"Active: {me.is_active()} Active Users: {User.active_users}")

# Accessing active_users both at the instance level and class level
print(f"Active users off of `me`: {me.active_users}, Class level: {User.active_users}")

# Assigning a new value to active_users at the instance level
me.active_users = "Just me"

# Accessing active_users again
print(f"Active users off of `me`: {me.active_users}, Class level: {User.active_users}")
