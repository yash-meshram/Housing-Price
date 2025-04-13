from abc import ABC, abstractmethod

class Dining(ABC):
    def serve(self):
        self.serve_appetizer()
        self.serve_main_course()
        self.serve_dessert()
        self.serve_beverage()
    
    @abstractmethod
    def serve_appetizer(self):
        pass
    
    @abstractmethod
    def serve_main_course(self):
        pass
    
    @abstractmethod
    def serve_dessert(self):
        pass
    
    @abstractmethod
    def serve_beverage(self):
        pass
    

class ItalianFood(Dining):
    def serve_appetizer(self):
        print("Appetizer: Brushetta")
    
    def serve_main_course(self):
        print("Main course: Pasta")
    
    def serve_dessert(self):
        print("Dessert: Tiramisu")
    
    def serve_beverage(self):
        print("Beverage: Wine")
        

class ChineseFood(Dining):
    def serve_appetizer(self):
        print("Appetizer: Spring roll")
    
    def serve_main_course(self):
        print("Main course: Stir-fried noodles")
    
    def serve_dessert(self):
        print("Dessert: Fortune cookies")
    
    def serve_beverage(self):
        print("Beverage: Tea")
        
if __name__ == "__main__":
    print("Italian Dinner")
    food = ItalianFood()
    food.serve()
    
    print("\nChinese Dinner")
    food = ChineseFood()
    food.serve()