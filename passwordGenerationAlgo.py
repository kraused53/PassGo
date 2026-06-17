# By Neil Patil
# Version 2 - updated to include common password check and be more modular.
import random
import csv
import os

def load_common_passwords(filepath='common_passwords.csv'):
    """
    Loads common passwords from a CSV file into a set for O(1) lookups.
    Returns a set of lowercase password strings.
    """
    common_pwds = set()
    try:
        # Determine path relative to script if not absolute
        if not os.path.isabs(filepath):
            # Assumes common_passwords.csv is in the same directory as this script - will be that way when user installs and runs it from github files
            filepath = os.path.join(os.path.dirname(__file__), filepath)
            
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # Skip header row
            next(reader, None) 
            
            for row in reader:
                if row:
                    pwd = row[0].strip().lower()
                    if pwd:
                        common_pwds.add(pwd)
    except FileNotFoundError:
        print(f"Warning: Common passwords file '{filepath}' not found. Skipping check.")
    except Exception as e:
        print(f"Warning: Error reading common passwords file: {e}")
        
    return common_pwds

# Load common passwords once when the module is imported
COMMON_PASSWORDS = load_common_passwords()

def generate_password(min_len, max_len, include_lower, include_upper, include_numbers, include_special):
    """
    Generates a password based on provided constraints.
    Checks against common passwords. If a match is found, 
    it attempts to regenerate exactly once to avoid loops.
    
    Returns the generated password string.
    Raises ValueError if inputs are invalid.
    """
    # 1. Input Validation
    try:
        min_len = int(min_len)
        max_len = int(max_len)
    except ValueError:
        raise ValueError("Lengths must be integers. ")

    if min_len < 6:
        raise ValueError("Minimum length must be at least 6. ")
    if min_len > max_len:
        raise ValueError("Minimum length cannot be greater than maximum length. ")
    if not (include_lower or include_upper or include_numbers or include_special):
        raise ValueError("At least one character type must be included. ")
    if max_len > 64:
        raise ValueError("Maximum length should not exceed 64 characters. ")

    # Helper function to perform the actual generation logic
    def _create_candidate():
        # 2. Define Character Sets
        lowercase_chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        uppercase_chars = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        number_chars = [str(i) for i in range(10)]
        special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

        # 3. Build Pool and Required Characters
        char_pool = []
        required_chars = []

        if include_lower:
            char_pool.extend(lowercase_chars)
            required_chars.append(random.choice(lowercase_chars))
            
        if include_upper:
            char_pool.extend(uppercase_chars)
            required_chars.append(random.choice(uppercase_chars))
            
        if include_numbers:
            char_pool.extend(number_chars)
            required_chars.append(random.choice(number_chars))
            
        if include_special:
            char_pool.extend(special_chars)
            required_chars.append(random.choice(special_chars))


        # 4. Determine Length
        password_length = random.randint(min_len, max_len)

        # Edge Case: Password length shorter than required categories
        if password_length < len(required_chars):
            password_length = len(required_chars)

        # 5. Fill Remaining Characters
        other_chars = [random.choice(char_pool) for _ in range(password_length - len(required_chars))]

        # 6. Combine and Shuffle
        all_chars = required_chars + other_chars
        random.shuffle(all_chars)
        
        return ''.join(all_chars)

    # Generate initial candidate
    candidate = _create_candidate()
    
    # Check against common passwords
    # We compare case-insensitively because common password lists are usually lowercase
    if COMMON_PASSWORDS and candidate.lower() in COMMON_PASSWORDS:
        # If it's common, generate ONE replacement. 
        # This avoids infinite loops while still providing a safety check.
        candidate = _create_candidate()
        
    return candidate

if __name__ == "__main__":
    # Example usage
    try:
        pwd = generate_password(8, 12, True, True, True, True)
        print(f"Generated Password: {pwd}")
    except ValueError as e:
        print(e)