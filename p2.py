def reverse_string_slicing(s):
    """
    Reverse a string using slicing (most efficient).
    
    Args:
        s (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    return s[::-1]


def reverse_string_loop(s):
    """
    Reverse a string using a loop.
    
    Args:
        s (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


def reverse_string_loop_builtin(s):
    """
    Reverse a string using reversed() builtin with join.
    
    Args:
        s (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    return "".join(reversed(s))


# Example usage
if __name__ == "__main__":
    test_string = "Hello, World!"
    print(f"Original: {test_string}")
    print(f"Reversed (slicing): {reverse_string_slicing(test_string)}")
    print(f"Reversed (loop): {reverse_string_loop(test_string)}")
    print(f"Reversed (reversed): {reverse_string_loop_builtin(test_string)}")
 