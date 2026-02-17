
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        try:
            return self._items.pop()
        except IndexError:
            raise IndexError("Cannot pop from an empty stack")

    def peek(self):
        try:
            return self._items[-1]
        except IndexError:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return not self._items

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"

#-------------------------------------------------------------------------------------------
schoolbooks = Stack()
schoolbooks.push('history')
schoolbooks.push('painting')
schoolbooks.push('math')
schoolbooks.push('biology')
schoolbooks.push('geography')
schoolbooks.push('chemistry')
schoolbooks.push('physics')
print(len(schoolbooks))
print(schoolbooks) # Stack(['history', 'painting', 'math', 'biology', 'geography', 'chemistry', 'physics'])
schoolbooks.pop()
schoolbooks.pop()
schoolbooks.pop()
print(schoolbooks) # Stack(['history', 'painting', 'math', 'biology'])
#-------------------------------------------------------------------------------------------
# solve valid parentheses with stack
# Given a string like: "({[]})"
# Determine if the brackets are valid.
# Why a stack?
# Push opening brackets.
# When you see a closing bracket → check if it matches the last opening one.
# If not → invalid.

def is_valid_parentheses(input_string):
    stack = []
    pairs = { # the dictionary maps: closing → opening ,since we process the string left → right, we only know something is wrong when we hit a closing bracket.
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in input_string:
        if char in pairs.values():  # opening bracket (the values in dictionary)
            stack.append(char)
        elif char in pairs:         # closing bracket (Is this character one of the dictionary keys?)
            if not stack or stack.pop() != pairs[char]: # empty list or the last opening(pop) != expected opening for this closing
                return False
    return not stack # It returns True only when the stack is empty at the end:
    # Every opening bracket had a matching closing bracket
    # They were closed in the correct order
    # No mismatches happened
    # No extra opening brackets remain

print(is_valid_parentheses('({[]})')) # True
print(is_valid_parentheses('({[)]})')) # False
#-------------------------------------------------------------------------------------------
