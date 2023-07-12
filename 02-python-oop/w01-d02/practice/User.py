class user:
    def __init__(self,first_name,last_name,email,age):
        #*attributes
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.age=age
        #*attributes with Default Values
        self.is_rewards_member=False
        self.gold_card_points=0
    def display_info(self):
        print(f"user's first name = {self.first_name}")
        print(f"user's last name = {self.last_name}")
        print(f"user's email = {self.email}")
        print(f"user's age = {self.age}")
        print(f"user's member status = {self.is_rewards_member}")
        print(f"user's gold card points={self.gold_card_points}")
    def enroll(self):
        if self.is_rewards_member:
            print("user already a member")
            return False
        self.is_rewards_member=True
        self.gold_card_points=200
    def spend_points(self,amount):
        if (self.gold_card_points>=amount):
            self.gold_card_points-=amount
        else:
            print("User don't have enough points")
            return False
Yosra=user("yosra","goblin","gremlin123@gmail.com",20)
Yosra.display_info()
Yosra.spend_points(50)
Houyem=user("Houyem","artist","acrylicpaint@gmail.com",21)
Houyem.display_info()
Houyem.enroll()
Houyem.spend_points(80)
Hakim=user("Hakim","gymrat","browniemonster@gmail.com",22)
Houyem.spend_points(40)
Hakim.display_info()

