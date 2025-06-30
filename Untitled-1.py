def print_dictionary_top_n(sorted_word_list, n):
    """
    Prints the top n most frequent words in a given sorted dictionaray.
    :param sorted_word_list: Gets a sorted list of words with their counts,
    :param n: n most frequent words.
    :return: None
    """
    for word, count in sorted_word_list[:n]:
        print(f"Word: '{word}' appears {count} times")


def word_frequency_counter(file_path, top_n):
    """
      This function runs the full word frequency analysis:
      it reads a text file, counts how many times each word appears,
      sorts the words by frequency, and prints the top n most frequent words.

      :param file_path: A string with the path to the text file
      :param top_n: An integer indicating how many top frequent words to print
      :return: None (the function only prints output)
      """
    word_count = read_file_content_to_dictionary(file_path)
    sorted_words = sort_dictionary_by_value(word_count)
    print_dictionary_top_n(sorted_words, top_n)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <file_path> <top_n>")
    else:
        try:
            file_path = sys.argv[1]
            top_n = int(sys.argv[2])
            word_frequency_counter(file_path, top_n)
        except FileNotFoundError:
            print(f"Error: The file '{sys.argv[1]}' was not found.")
        except ValueError:
            print("Error: <top_n> must be a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
