from crypto import encrypt_message, decrypt_message

def main():
    chat_log = []

    while True:
        print("\n--- Encrypted Chat ---")
        print("1. Alice sends a message")
        print("2. Bob sends a message")
        print("3. Show chat log (decrypted)")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            msg = input("Alice: ")
            encrypted = encrypt_message(msg)
            chat_log.append(("Alice", encrypted))
            print("Message encrypted and sent ✅")
        elif choice == "2":
            msg = input("Bob: ")
            encrypted = encrypt_message(msg)
            chat_log.append(("Bob", encrypted))
            print("Message encrypted and sent ✅")
        elif choice == "3":
            print("\n--- Chat Log ---")
            if not chat_log:
                print("No messages yet.")
            for sender, enc_msg in chat_log:
                print(f"{sender}: {decrypt_message(enc_msg)}")
        elif choice == "4":
            print("Exiting chat...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
