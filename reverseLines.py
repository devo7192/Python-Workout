def reverseLines(file1, file2):

    with open(file1) as infile, open(file2, 'w') as outfile:

            for line in infile:
                outfile.write(f'{line.rstrip()[::-1]}\n')
    

reverseLines('abc.txt', 'cba.txt')