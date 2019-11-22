global window_size
global substring_list  # list of substrings that have all the characters


def subString(s):
    """
    for each window in each window size, find the smallest substring
    :param s: THe full string
    :return:  Shortest substring of type string
    """

    # initializing variables
    number_of_unique_characters = len(set([x for x in s]))
    window_size = number_of_unique_characters
    set_of_unique_characters_in_window = set()
    start = 0
    end = start + window_size
    # print("Start: {}".format(start))
    # print("End: {}".format(end))
    # print("Window Size: {}".format(window_size))

    # untill the window size reaches the length of the string itself, increment the window size
    while window_size < len(s):
        # each time all windows are completed, start and end become 0

        # check if the entire string is of the same character, then return
        if window_size == 1:
            return s[0]
        else:
            start = 0
            end = start + window_size
            substring = ""

            # for each window size in s
            for lengths in range(window_size, len(s), 1):
                # for each window traversed
                # start index and end index of window, find any window that has all the characters

                while end <= len(s):

                    # add the characters of the window into a set
                    for character in s[start:end]:
                        # adding characters in set, to see if the substring has all the characters
                        set_of_unique_characters_in_window.add(character)

                    # check if it has all the distinct characters and the window size is the same as the number of distinct characters
                    if len(set_of_unique_characters_in_window) == number_of_unique_characters:

                        # the smallest substring possible
                        return s[start:end]

                    # Move the window to the right
                    else:
                        start += 1
                        end += 1
                        set_of_unique_characters_in_window.clear()


print(subString("abbbccdddbca"))
