class Pet:
    """Parent class representing a general Pet."""
    def __init__(self, name: str, age: int, health_status: str):
        self.name = name
        self.age = age
        self.__health_status = health_status 

    def get_health_status(self) -> str:
        return self.__health_status

    def set_health_status(self, new_status: str):
        valid_statuses = ["Healthy", "Sick", "Recovering", "Under Treatment"]
        if new_status in valid_statuses:
            self.__health_status = new_status
        else:
            print(f"⚠️ Invalid health status '{new_status}'. Remaining as '{self.__health_status}'.")

    def perform_checkup(self) -> str:
        return f"Performing a standard physical exam on {self.name}."

class Dog(Pet):
    """Child class representing a Dog."""
    def __init__(self, name: str, age: int, health_status: str, breed: str):
        super().__init__(name, age, health_status)
        self.breed = breed

    def perform_checkup(self) -> str:
        return f"🐾 Examining {self.name} the {self.breed}: Checking tail wag frequency and heart rate."

class Cat(Pet):
    """Child class representing a Cat."""
    def __init__(self, name: str, age: int, health_status: str, is_indoor: bool):
        super().__init__(name, age, health_status)
        self.is_indoor = is_indoor

    def perform_checkup(self) -> str:
        location = "Indoor" if self.is_indoor else "Outdoor"
        return f"🐱 Examining {self.name} ({location} Cat): Checking coat condition and stress levels."

if __name__ == "__main__":
    buddy = Dog(name="Buddy", age=3, health_status="Healthy", breed="Golden Retriever")
    whiskers = Cat(name="Whiskers", age=5, health_status="Sick", is_indoor=True)
    
    whiskers.set_health_status("Recovering")
    
    dashboard_pets = [buddy, whiskers]
    for pet in dashboard_pets:
        print(f"Pet: {pet.name} | Health: {pet.get_health_status()} | Action: {pet.perform_checkup()}")
