
def word_count(fileName):

    with open(fileName) as f:
        
        uniqueWords = set()
        totals = {'chars':0, 
                  'words':0, 
                  'lines':0}
        
        for line in f:

            for char in line:
                totals['chars'] += 1
            
            totals['words'] += len(line.split())
            totals['lines'] += 1
            uniqueWords.update(line.split())
        
        print(f'Number of characters (including whitespace): {totals.get("chars")}')
        print(f'Number of words (separated by whitespace): {totals.get("words")}')
        print(f'Number of lines: {totals.get("lines")}')
        print(f'Number of unique words: {len(uniqueWords)}')
        # print(f'{uniqueWords}')



        