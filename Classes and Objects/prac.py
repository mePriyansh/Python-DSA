class Youtube:
    def __init__(self, user, subscribers=0,subscription=0):
        self.user = user
        self.subscribers = subscribers
        self.subscription = subscription
        
    def subscribe(self,user):
        user.subscribers += 1
        self.subscription += 1
        
user1 = Youtube("John")
user2 = Youtube("Jane", 100)
user1.subscribe(user2)
print(user1.user)
print(f"User 1 Subscribers:{user1.subscribers}")
print(f"User 1 Subscription:{user1.subscription}")

print(user2.user)
print(f"User 1 Subscribers:{user2.subscribers}")
print(f"User 1 Subscription:{user2.subscription}")