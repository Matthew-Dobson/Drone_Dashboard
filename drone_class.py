import random

class Drone:
    def __init__(self, coords, height, speed):
        self.coords = coords
        self.height = height
        self.speed = speed

    def update_position(self):
        """Simulates movement by slightly changing coordinates, height, and speed."""
        self.coords[0] += random.randint(-5, 5)
        self.coords[1] += random.randint(-5, 5)
        self.height += random.randint(-2, 2)
        self.height = max(0, self.height)  # Prevents negative height
        self.speed = random.randint(0, 20)

    def retrieve_data(self):
        """Returns current drone telemetry as a dictionary."""
        return {
            "coords": self.coords,
            "height": self.height,
            "speed": self.speed
        }
    

