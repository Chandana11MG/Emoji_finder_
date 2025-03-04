import locale

MAX_EMOJIS = 100
MAX_DESC_LENGTH = 50

class Emoji:
    def __init__(self, emoji, description):
        self.emoji = emoji
        self.description = description


emoji_dataset = [
    Emoji("😀", "grinning face"),
    Emoji("😂", "face with tears of joy"),
    Emoji("😍", "smiling face with heart-eyes"),
    Emoji("😎", "smiling face with sunglasses"),
    Emoji("😊", "smiling face with smiling eyes"),
    Emoji("😢", "crying face"),
    Emoji("😡", "pouting face"),
    Emoji("👍", "thumbs up"),
    Emoji("👏", "clapping hands"),
    Emoji("🙏", "folded hands"),
    Emoji("❤", "heart")
]
emoji_count = len(emoji_dataset)

def add_emoji():
    global emoji_count
    if emoji_count >= MAX_EMOJIS:
        print("Emoji dataset is full!")
        return
    emoji = input("Enter the emoji: ")
    description = input("Enter the description: ")
    emoji_dataset.append(Emoji(emoji, description[:MAX_DESC_LENGTH]))
    emoji_count += 1
    print("Emoji added successfully!")

def delete_emoji():
    global emoji_count
    description_to_delete = input("Enter the description of the emoji to delete: ")
    global emoji_dataset

    for i, emoji in enumerate(emoji_dataset):
        if emoji.description == description_to_delete:
            del emoji_dataset[i]
            emoji_count -= 1
            print("Emoji deleted successfully!")
            return
    print(f"No emoji found with description \"{description_to_delete}\"")

def search_emojis_divide_and_conquer(keyword, start, end):
    if start > end:
        return []

    mid = (start + end) // 2
    result = []


    if keyword in emoji_dataset[mid].description:
        result.append(emoji_dataset[mid])


    left_results = search_emojis_divide_and_conquer(keyword, start, mid - 1)
    right_results = search_emojis_divide_and_conquer(keyword, mid + 1, end)

    return result + left_results + right_results

def search_emojis():
    keyword = input("Enter a description keyword to find matching emojis: ")

    emoji_dataset.sort(key=lambda x: x.description)
    results = search_emojis_divide_and_conquer(keyword, 0, emoji_count - 1)

    if results:
        for emoji in results:
            print(f"{emoji.emoji} : {emoji.description}")
    else:
        print(f"No emojis found for \"{keyword}\"")

def display_emojis():
    print("Displaying all emojis:")
    for emoji in emoji_dataset:
        print(f"{emoji.emoji} : {emoji.description}")

def menu():
    while True:
        print("\nEmoji Finder Menu")
        print("1. Add an Emoji")
        print("2. Delete an Emoji")
        print("3. Search for Emojis")
        print("4. Display All Emojis")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_emoji()
        elif choice == '2':
            delete_emoji()
        elif choice == '3':
            search_emojis()
        elif choice == '4':
            display_emojis()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')
    menu()
