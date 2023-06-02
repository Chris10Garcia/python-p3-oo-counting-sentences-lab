#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ''):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        return True if self.value.endswith(".") else False
    
    def is_question(self):
        return True if self.value.endswith("?") else False
    
    def is_exclamation(self):
        return True if self.value.endswith("!") else False
    
    def count_sentences(self):
        # split_value = re.split(r"(?:.\W){1}", self.value)
        split_value = [element for element in self.value.split(" ") 
                       if element.endswith(".") or element.endswith("?") or element.endswith("?") or element.endswith("!")]
        print(split_value)
        return len(split_value)

# test = MyString()

# test.value = 123

# test.set_value(123)

# print(test.value)