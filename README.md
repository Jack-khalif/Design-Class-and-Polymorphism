
#  Python OOP Assignments

This repository contains two Python Object-Oriented Programming (OOP) assignments focusing on **classes**, **inheritance**, **encapsulation**, and **polymorphism**.


##  Assignment 1: Design Your Own Class
##run file: DesigningClass.py

###  Description
This program defines a `Smartphone` class representing a real-world smartphone. It extends a base `Device` class, demonstrating inheritance, encapsulation, and method functionality.

### Features
- **Device class** (Base) with `brand` and `model` attributes.
- **Smartphone class** inherits from `Device`.
- Encapsulated attributes (`_brand`, `_model`).
- Unique methods:
  - `take_photo()` — simulates capturing a photo.
  - `make_call(number)` — simulates making a call.
- Uses **constructors** to initialize unique values.

### ▶ Example Usage
```python
my_phone = Smartphone("Samsung", "Galaxy S23", "256GB", 108)
print(my_phone.device_info())
my_phone.take_photo()
my_phone.make_call("+254712345678")
```

---

##  Activity 2: Polymorphism Challenge 
##Run file: polymorphism.py

###  Description
This program demonstrates **polymorphism** using an `Animal` base class and multiple subclasses (`Dog`, `Bird`, `Fish`). Each subclass defines its own version of the `move()` method.

###  Features
- **Animal class** (Base) with a `move()` method.
- Subclasses:
  - `Dog` → `🐕 Running on four legs!`
  - `Bird` → `🐦 Flying in the sky!`
  - `Fish` → `🐟 Swimming in the water!`
- Demonstrates polymorphism via method overriding.
- Uses a **for loop** to call `move()` on each animal object.

###  Example Usage
```python
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()
```

---

##  Requirements
- Python 3.x

---



## 📃 License
Open for educational and personal learning use.

---

