"""Read and Say sequence

The look-and-say sequence is defined as a = [1, 11, 21, 1211, 111221, ...], please include code in your application that calculates len(a[30]).

""" 


def read_and_say(n):
    """Read and say sequence.

        REACTO

        Repeat:
        Example:
            1 -> one 1 ->(11) 
            11 -> two 1 -(21)
            21 -> one 2 one 1 (1211)
            1211 -> one 1 one 2 two one (111221)
            111221 -> ...
            <count> <number>
        Action:
            - count consecutive same characters
            - assemble count and value of the characters in the order from left to right
            - scenario 1: the char is never shown before
            - scenario 2: the char has show before
            - scenario 3: the current char is not the same as the previous char (shown char)
            - scenario 4: the current char is the last in the string
        Test code:
        Optimization: time complexity O(m*n), space complexity O(n)
        
    :param n: [description]
    :return: [description]
    """
    a = ["1"]

    if n > len(a) - 1:
        # iterate n - len(a) times
        for idx in range(0, n - 1, 1):
            # count
            string = ""
            count = 0
            shown_char = None
            for digit, char in enumerate(a[idx]):
                if shown_char != char: # scenario 3
                    if shown_char: # scenario 1
                        # write the char when the current char doesn't equal to the previous
                        string += str(count)
                        string += shown_char
                        
                    shown_char = char
                    count = 1
                else: # scenario 2
                    # The char has shown before. It means the char is repetitive
                    count += 1

                if len(a[idx]) == digit + 1: # scenario 4
                    # write the char when the current char is the last of the string
                    string += str(count)
                    string += char

            a.append(string)

    print(a)
    return a


def main():
    result = read_and_say(31)

    print(len(result[30]))

if __name__ == "__main__":
    main()