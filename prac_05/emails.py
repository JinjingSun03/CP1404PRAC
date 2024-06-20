def extract_name(email):
    name = email.split('@')[0]
    name = name.replace('.', ' ').replace('_', ' ')
    name = ' '.join(word.capitalize() for word in name.split())
    return name

def main():
    user_data = {}

    while True:
        email = input("Email: ")
        if not email:
            break

        name_from_email = extract_name(email)
        confirmation = input(f"Is your name {name_from_email}? (Y/n) ").lower()

        if confirmation == '' or confirmation == 'y':
            user_data[email] = name_from_email
        else:
            name = input("Name: ")
            user_data[email] = name

    print("\nResults:")
    for email, name in user_data.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
