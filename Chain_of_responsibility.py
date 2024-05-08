from abc import ABC, abstractmethod

class AccessHandler(ABC):
    @abstractmethod
    def handle_request(self,user):
        pass

class BasicAccessHandler(AccessHandler):
    def __init__(self,successor= None):
        self.successor = successor

    def handle_request(self, user):
        if user.role == "basic":
            print("Basic access granted")
        elif self.successor:
            self.successor.handle_request(user)
        else:
            print("Access denide.")

class PremiumAccessHandler(AccessHandler):
    def __init__(self, successor= None):
        self.successor= successor

    def handle_request(self, user):
        if user.role == "premium":
            print("premium access granted.")
        elif self.succssor:
            self.successor.handle_request(user)
        else:
            print("Access denied")
    
class User:
    def __init__(self, role):
        self.role = role

class OrderingSystem:
    def __init__(self):
        #Build chain of responsibility
        self.access_handler = BasicAccessHandler(PremiumAccessHandler())

    def proccess_order(self,user):
        print("Proccessing order...")
        self.access_handler.handle_request(user)
    

def main():
    ordering_system = OrderingSystem()

    user1 = User("basic")
    user2 = User("premium")

    ordering_system.proccess_order(user1)
    ordering_system.proccess_order(user2)

if __name__ =='__main__':
    main()

