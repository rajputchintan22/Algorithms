class Solution:
    def fullJustify(self, words, maxWidth):
        lengths = []
        for i in words:
            lengths.append(len(i))
        ans = []
        word_Count = 0
        current_length = 0
        word_list = []
        potential_length = 0
        for i in range(len(words)):
            if word_Count < 1:
                potential_length += lengths[i]
            else:
                potential_length += lengths[i]+1
            if potential_length <= maxWidth:
                if word_Count < 1:
                    current_length += lengths[i]
                else:
                    current_length += lengths[i]+1
                word_Count += 1
                word_list.append(words[i])
            else:
                if word_Count == 1:
                    ans.append(word_list[0]+" "*(maxWidth-lengths[i-1]))
                else:
                    remaining_space = maxWidth - (current_length -(word_Count-1))
                    equal_space = remaining_space // (word_Count-1)
                    spaces = [" "*equal_space] * (word_Count-1)
                    additional_space = remaining_space % (word_Count-1)
                    for  j in range(additional_space):
                        spaces[j] = spaces[j]+" "
                    row = ""
                    for j in range(word_Count-1):
                        row += word_list[j] + spaces[j]
                    row += word_list[-1]
                    ans.append(row)
                word_Count = 1
                current_length = lengths[i]
                word_list = [words[i]]
                potential_length = current_length
        final_line = " ".join(word_list)
        ans.append(final_line + " "*(maxWidth-len(final_line)))
        return ans
    
print(Solution().fullJustify(words=["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth=20))