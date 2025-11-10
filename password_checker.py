def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Too short"
    if not any(c.isupper() for c in password):
        return "Weak: No uppercase letters"
    return "Strong"

# Example usage
print(check_password_strength("Passw0rd!"))
