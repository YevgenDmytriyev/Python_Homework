import re

#1 Task

strings = ["123", "abc456", "789xyz", "12", "1a2b3c"]
pattern = r"\d{3}"

for i in strings:
    print(i)
    match_result = re.search(pattern,i)
    print(match_result)

#2 Task

strings = ["HELLO", "WORLD", "123", "Hello", "UPPERCASE"]
pattern = r"\b[A-Z]+\b"

for i in strings:
    print(i)
    match_result = re.search(pattern,i)
    print(match_result)


#3 Task

emails = ["test@example.com", "john.doe@gmail.com", "invalid_email", "user@domain", "abc@123.xyz"]
pattern = r"[\w.]+@[\w]+\.[\w]+"

for i in emails:
    print(i)
    match_result = re.search(pattern,i)
    print(match_result)

#4 Task

dates = ["31-12-2022", "15-06-23", "02/05/2023", "2022-12-31", "01-13-2023"]
pattern = r"\d{2,4}[./-]\d{2}[./-]\d{2,4}"

for i in dates:
    print(i)
    match_result = re.search(pattern,i)
    print(match_result)



#5 Task

urls = ["http://www.example.com", "https://www.google.com", "ftp://invalid-url.com", "https://sub.domain.co.uk", "http://localhost"]
pattern = r"(www|https?|ftp)://[^\s/$.?#].[^\s]*"

for i in urls:
    print(i)
    match_result = re.search(pattern,i)
    print(match_result)


#6 Task

phone_numbers = ["+91-1234567890", "+44-9876543210", "+1-1234567890", "+12-9876543210", "+1-1234"]
pattern = r"(\+\d{1,2}[-]?)(\d{3})?\d{3}?\d{4}"

for i in phone_numbers:
    print(i)
    match_result = re.search(pattern,i)
    print(match_result)


#7 Task

ip_addresses = ["192.168.0.1", "10.0.0.0", "256.0.0.0", "172.16.0.0", "127.0.0.1", "0.0.0.0"]
pattern = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

for ip_address in ip_addresses:
    if re.match(pattern, ip_address):
        print(ip_address + " is a valid IPv4 address.")
    else:
        print(ip_address + " is not a valid IPv4 address.")


#8 Task

sentences = ["Hello, World!", "This is a Sentence.", "openAI", "python", "One Two Three"]
pattern = r"[A-Z][a-z]+"

for ip_address in sentences:
    if re.match(pattern, ip_address):
        print(f"{ip_address} is a valid IPv4 address.")
    else:
        print(f"{ip_address} is not a valid IPv4 address.")
#9 Task

passwords = ["Abcd1234!", "passWORD!123", "abc123", "Password", "12345678"]

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"

for password in passwords:
    if re.match(pattern, password):
        print(f"'{password}' is a valid password.")
    else:
        error_messages = []
        if len(password) < 8:
            error_messages.append("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", password):
            error_messages.append("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", password):
            error_messages.append("Password must contain at least one lowercase letter.")
        if not re.search(r"\d", password):
            error_messages.append("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*]", password):
            error_messages.append("Password must contain at least one special character (!@#$%^&*).")
        error_reasons = ", ".join(error_messages)
        print(f"'{password}' is an invalid password. Reason(s): {error_reasons}")