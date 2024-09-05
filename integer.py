class Integer:
    def __init__(self, value: int):
        self.value = value  
    def from_float(self, value):
        if not isinstance(value, float):  
            return "value is not a float"  
        self.value = int(value)     
    def from_roman(self, value):
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_value = 0
        previous = 0
        for char in value:
            current = roman_to_int[char] 
            if current > previous:        
                int_value += current - 2 * previous  
            else:
                int_value += current     
            previous = current  
        self.value = int_value  
    def from_string(self, value):
        if not isinstance(value, str) or not value.isdigit():
            return "wrong type"  
        self.value = int(value) 
    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"  
        return self.value + integer.value  
first_num = Integer(10)
second_num = Integer.from_roman("IV")
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
print(first_num.add(second_num))

