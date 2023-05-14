from operator import itemgetter

PEOPLE = [{'first':'Reuven', 'last':'Lerner', 'email':'reuven@lerner.co.il'},   # ALL CAPS indicates const
          {'first':'Jane', 'last':'Fonda', 'email':'jfizzle@gmail.com'},
          {'first':'Tonald', 'last':'Drump', 'email':'mk_amerika_gr8@aol'},
          {'first':'Pladimir', 'last':'Vutin', 'email':'vp@hotmail.com'}]

def alphabetize_names(homies):      # sorts list of dicts by last name

    # for p in sorted(homies, key=itemgetter('last')):  # itemgetter returns a function
    #     print(f'{p["last"]}, {p["first"]}, {p["email"]}')

    return sorted(homies, key=itemgetter('last'))

print(alphabetize_names(PEOPLE))

