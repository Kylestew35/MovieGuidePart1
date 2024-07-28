# Kyle Stewart CIS216 Movie Guide Part 1

print("Welcome to the Movie List Program!\n")

def display_menu():
    print("Command Menu:")
    print("list - Display all titles")
    print("add - Add a title")
    print("del - Delete a title")
    print("exit - Exit program")

def display_titles(movie_list):
    print("\nMovie Titles:")
    for i, title in enumerate(movie_list, 1):
        print(f"{i}. {title}")

def add_title(movie_list):
    title = input("Enter the title of the movie: ")
    movie_list.append(title)
    print(f"'{title}' has been added to the list.")
    display_titles(movie_list)

def delete_title(movie_list):
    try:
        index = int(input("Enter the number of the movie title you want to delete: ")) - 1
        if index < 0 or index >= len(movie_list):
            print("Invalid number. Please try again.")
        else:
            print(f"'{movie_list[index]}' has been deleted from the list.")
            del movie_list[index]
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    movie_list = ["Monty Python and the Holy Grail", "On the Waterfront", "Cat on a Hot Tin Roof"]

    while True:
        display_menu()
        choice = input("Enter your command: ")

        if choice == "list":
            display_titles(movie_list)
        elif choice == "add":
            add_title(movie_list)
        elif choice == "del":
            delete_title(movie_list)
        elif choice == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid command. Please try again.")

        print()

if __name__ == "__main__":
    main()
