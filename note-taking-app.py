notes = []

while True:
    print("\n--- Note Tracking App ---")
    print("1. Add a note")
    print("2. View all notes")
    print("3. Clear all notes")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        note = input("Enter your note: ")
        notes.append(note)
        print("✅ Note added successfully!")

    elif choice == "2":
        if not notes:
            print("📭 No notes available.")
        else:
            print("\n📒 Your Notes:")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

    elif choice == "3":
        notes.clear()
        print("🗑️ All notes cleared!")

    elif choice == "4":
        print("👋 Exiting the app. Goodbye!")
        break

    else:
        print("❌ Invalid choice! Please enter a number from 1 to 4.")