"""
main.py
This program analyzes a text from a file using the module analyzer.
"""

import analyzer

def main():
    """
    This function runs the program to analyze a text from a file.
    """

    file_name = "phil.txt"

    while True:
        print("lines) Count lines.")
        print("words) Count words.")
        print("letters) Count letters.")
        print("word_frequency) Find 7 most used words.")
        print("letter_frequency) Find 7 most used letters.")
        print("all) Do everything.")
        print("change) Change file.")
        print("q) Quit.")

        choice = input("--> ").strip()

        if choice == "q":
            print("Bye, bye - and welcome back anytime!")
            break

        if choice == "change":
            try:
                file_name = input("Enter filename: ").strip()
            except FileNotFoundError:
                print("Invalid filename.")
                
        if choice == "lines":
            content = analyzer.file_content(file_name)
            print(analyzer.count_lines(content))
            
        elif choice == "words":
            content = analyzer.file_content(file_name)
            print(analyzer.count_words(content))

        elif choice == "letters":
            content = analyzer.file_content(file_name)
            print(analyzer.count_letters(content))

        elif choice == "word_frequency":
            content = analyzer.file_content(file_name)
            print(analyzer.word_frequency(content))

        elif choice == "letter_frequency":
            content = analyzer.file_content(file_name)
            print(analyzer.letter_frequency(content))

        elif choice == "all":
            content = analyzer.file_content(file_name)
            print(analyzer.all_results(content))

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        if choice != "q":
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
