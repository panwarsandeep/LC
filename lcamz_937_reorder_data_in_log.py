from string import ascii_lowercase
class Solution:
    def reorderLogFiles(self, logs):
        j = len(logs)-1
        i = j

        while True:
            while i > 0 and logs[i].split()[-1].isdigit():
                i -= 1
            j = i - 1
            while j >= 0 and not logs[j].split()[-1].isdigit():
                j -= 1

            if j < i and j >= 0:
                logs[i], logs[j] = logs[j], logs[i]
            
            i -= 1 if j >= 0 else 0
            if j <= 0:
                break

        i += 1
        logs[0:i] = sorted(logs[0:i], key=lambda x: ' '.join(x.split()[1:])+x.split()[0])
        print(logs[0:i])
        #logs[i:] = reversed(logs[i:])
        return logs


if __name__ == '__main__':
    sol = Solution()

    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
    logs = ["j je", "b fjt", "7 zbr", "m le", "o 33"]
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    logs = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]
    print(logs)
    r = sol.reorderLogFiles(logs)
    print(r)
    