import json
import glob

def print_scores(dirName):
    # UNFINISHED BUSINESS!
    for fileName in glob.glob(f'{dirName}/*.json'):
   
        scores = {}
        with open(fileName) as infile:
            
            result = json.load(infile)
            
            scores[fileName] = result
            print(scores[fileName].get('science').get('max'))
        
        # print(scores)
                


print_scores('scores')