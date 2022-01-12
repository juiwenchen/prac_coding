class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        # String replacement
        if 1 <= len(command) <=100:
            interpreted_str = ""
            skip = 0
            for i in range(len(command)):
                if (skip + i) == len(command):
                    break
                if skip:
                    skip -= 1
                    continue
                if command[i] == "G":
                    interpreted_str += "G"
                elif command[i] == "(":
                    if command[i + 1] == ")":
                        interpreted_str += "o"
                        skip = 1
                    elif command[i+1:i+4] == "al)":
                        # string extraction [start_idx:end_idx] the char of end_idx is not extracted
                        interpreted_str += "al"
                        skip = 3
            
            return interpreted_str
                

def main():
    command = "G()(al)"
    interpreted_str = Solution().interpret(command=command)
    print(interpreted_str)


if __name__ == '__main__':
    main()