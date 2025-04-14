# Smartphone Class Example with Inheritance and Encapsulation

# Base class
class Device:
    def __init__(self, brand, model):
        self._brand = brand  # Encapsulated attribute
        self._model = model

    def device_info(self):
        return f"Device: {self._brand} {self._model}"

# Subclass inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)
        self.storage = storage
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"📸 Taking a photo with {self.camera_megapixels} MP camera.")

    def make_call(self, number):
        print(f" Calling {number} from {self._brand} {self._model}.")

# Example usage
my_phone = Smartphone("Samsung", "Galaxy S23", "256GB", 108)
print(my_phone.device_info())
my_phone.take_photo()
my_phone.make_call("+254712345678")
