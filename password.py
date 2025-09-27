import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True):
    """Generate a password using letters and numbers only."""
    
    char_sets = []
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    
    if not char_sets:
        raise ValueError("At least one character type must be selected.")

    # Ensure at least one character from each selected set
    password_chars = [random.choice(s) for s in char_sets]

    # Fill the remaining length
    all_chars = ''.join(char_sets)
    remaining_length = length - len(password_chars)
    password_chars += [random.choice(all_chars) for _ in range(remaining_length)]

    # Shuffle to randomize positions
    random.shuffle(password_chars)

    return ''.join(password_chars)

# CLI Usage
if __name__ == "__main__":
    try:
        length = int(input("Enter desired password length (default 12): ") or 12)
    except ValueError:
        length = 12

    password = generate_password(length)
    print("\nGenerated Password:\n")
    print(password)
