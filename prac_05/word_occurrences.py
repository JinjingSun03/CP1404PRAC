def count_word_occurrences(text):
    """
    Count the occurrences of words in a string and print the results with aligned output.
    param text: The input string from the user.
    """

    words = text.split()

    word_counts = {}

    for word in words:
        word = word.strip('.,!?').lower()

        word_counts[word] = word_counts.get(word, 0) + 1

    max_word_length = max(len(word) for word in word_counts.keys())

    sorted_word_counts = sorted(word_counts.items())

    for word, count in sorted_word_counts:
        print(f"{word:{max_word_length}} : {count}")

user_input = input("Enter a string: ")

count_word_occurrences(user_input)
