def pay(amount):
    print("\n--- Payment ---")
    print(f"Total Amount: {amount}")
    print("1. Cash")
    print("2. Card")
    print("3. UPI")

    choice = int(input("Choose payment method: "))

    if choice == 1:
        print("Payment successful with Cash.")
    elif choice == 2:
        print("Payment successful with Card.")
    elif choice == 3:
        print("Payment successful with UPI.")
    else:
        print("Invalid choice. Payment failed.")