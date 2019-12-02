dossiers = ['The Contessa', 'Double Trouble', 'Eartha Brute', 'Kneemoi', 'Patty Larceny', 'RoboCrook', 'Sarah Nade', 'Top Grunge', 'Vic the Slick', 'Wonder Rat']

for crook in dossiers:
    print(crook)

""" Equivalent to: """

list_iter = iter(dossiers)
# list_iter is an iterator that is returned by dossiers.__iter__()
# a list is also an iterable
while True:
    try:
        crook = next(list_iter)
        print(crook)
    except StopIteration:
        break    