from operator import itemgetter

PEOPLE = [('Donald', 'Trump', 7.85),    # (last, first, est. arrival time)
          ('Donalc', 'Trump', 8),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(records):
    # sorts records - a list of tuples - and prints them in a particular format 
    output = []
    for person in sorted(records, key=itemgetter(1, 0)):    # two arguments incase last name is same
        output.append(f'{person[1]:10} {person[0]:10} {person[2]:5.2f}')    # elem:char spacing|decimal digs

    return '\n'.join(output)


print(format_sort_records(PEOPLE))