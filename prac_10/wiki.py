import wikipedia


def main():
    while True:
        search_query = input("Enter a page title or search phrase (blank to exit): ")

        if not search_query:
            break

        try:
            page = wikipedia.page(search_query, autosuggest=False)

            print("Title:", page.title)
            print("Summary:", page.summary)
            print("URL:", page.url)

        except wikipedia.exceptions.DisambiguationError as e:
            print("Disambiguation Page. Options:")
            options = e.options
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")


if __name__ == "__main__":
    main()
