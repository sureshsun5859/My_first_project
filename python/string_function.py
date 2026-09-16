# 1. Using slicing

def reverse_string_slicing(text):
    return text[::-1]


# 2. Using a loop

def reverse_string_loop(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text


given_string = "suresh"

print("Original string:", given_string)
print("Reversed using slicing:", reverse_string_slicing(given_string))
print("Reversed using loop:", reverse_string_loop(given_string))
