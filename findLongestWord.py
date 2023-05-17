import os
    
def find_longest_word(fileName):

    with open(fileName) as f:

        longestWord = ''
            
        for line in f:

            if len(longestWord) < len(max(line.split(), key=len)):
                longestWord = max(line.split(), key=len) 

    return longestWord


def find_all_longest_words(directory):
    
    result = {}

    for fileName in os.listdir(directory):

        filePath = os.path.join(directory, fileName)    # native to OS
        result[fileName] = find_longest_word(filePath)

    return result


print(find_all_longest_words('testDirectory'))
