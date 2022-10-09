class Guitar:  # Parent Class
    def __init__(self):
        self.number_of_strings = 15
        self.material = "wood"
        
    def play_melody(self):
        print("Melody playing...")
        
class ElectricGuitar(Guitar):  # Child Class
        def __init__(self):
            super().__init__()
            self.colour = "brown"
    
        
electric = ElectricGuitar()
print(electric.colour)
electric.play_melody()