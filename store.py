class Store:
    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {} 
    def from_size(name: str, type: str, size: int):
        return f"{name} of type {type} with capacity {size // 2}"
    def add_item(self, item_name: str):
     if item_name in self.items:
        self.capacity += 1
     else:
        self.items[item_name] = 1
        return f"{item_name} added to the store"
        current_quantity = sum(self.items.values())
     if current_quantity + 1 > self.capacity:
        return "Not enough capacity in the store"
    def remove_item(self, item_name: str, amount: int):
     if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f"{amount} {item_name} removed from the store"
     else:
            return f"Cannot remove {amount} {item_name}"

    def __repr__(self) -> str:
        return f"{self.name} of type {self.type} with capacity {self.capacity}"

first_store = Store("First store", "f and v", 20)
second_store = Store("Second store", "c", 500)
print(first_store)  
print(second_store)  
print(first_store.add_item("p"))  
print(second_store.add_item("j"))  
print(first_store.remove_item("t", 1)) 
print(second_store.remove_item("j", 1)) 