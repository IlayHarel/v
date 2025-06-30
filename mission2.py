import sys


def read_file_content_to_dictionary(file_path):
    """
     Reads a text file line by line, splits each line into words,
     counts the occurrences of each word,
     and returns a dictionary where the keys are words and the values are their frequencies.

     :param file_path: A string representing the path to the text file
     :return: A dictionary mapping each word to the number of times it appears in the file
     """
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    return word_count


def sort_dictionary_by_value(word_count):
    """
       Gets a dictionary of words and how many times each one appeared,
       and returns a sorted list from most to least frequent.

       :param word_count: A dictionary where keys are words and values are their counts
       :return: A list of (word, count) pairs sorted by count, from highest to lowest
       """

    return sorted(word_count.items(), key=lambda item: item[1], reverse=True)


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
      Runs the full word frequency analysis:
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
