
# Example 1: Simple function with parameters and return value
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b
result = add_numbers(5, 3)
print(result)

# Example 2: Function with default parameters
def greet_person(name, greeting="Hello"):
    """Greet a person with a customizable greeting."""
    return f"{greeting}, {name}!"


# Example 3: Function with multiple return values
def get_user_info(user_id):
    """Return multiple user information as a tuple."""
    name = "John Doe"
    age = 30
    email = "john@example.com"
    return name, age, email


# Test the examples
if __name__ == "__main__":
    # Test Example 1
  
    
    # Test Example 2
    message = greet_person("Alice")
    message2 = greet_person("Bob", "Hi")
    print(message)
    print(message2)
    
    # Test Example 3
    name, age, email = get_user_info(1)
    print(f"Name: {name}, Age: {age}, Email: {email}")