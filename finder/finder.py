''' Find the 20 strongest words to use in Wordle based on value counts '''
import re
import pandas

with open('words.txt', 'r', encoding='utf8') as f:
    data = []
    words = {}
    for line in f:
        line = line.strip("\n").lower()
        if len(line) == 5:
            if re.match("[a-z]{5}", line):
                words[line] = 0
                for char in line:
                    data.append(char)
    df = pandas.DataFrame(data)
    count_value = df.value_counts()
    for word in words:
        for char in word:
            if word.count(char) > 1:
                words[word] -= count_value[char]
            else:
                words[word] += count_value[char]
    df2 = pandas.DataFrame(words.items())
    print(df2.sort_values(by=1, ascending=False).head(20))
