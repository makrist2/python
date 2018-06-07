def group_by_surname(list_of_enrollees):
    first = 'ABCDEFGHI'
    f = 0
    second = 'JKLMNOP'
    s = 0
    third = 'QRST'
    t = 0
    fourth = 'UVWXYZ'
    fo = 0
    for _ in list_of_enrollees:
        for j in list_of_enrollees:
            sur = j.split()[1][0]
            print(sur)
            if sur in first:
                f += 1
            elif sur in second:
                s += 1
            elif sur in third:
                t += 1
            elif sur in fourth:
                fo += 1
        return f, s, t, fo


lst = ['Johnny Depp', 'Al Pacino', 'Kevin Spacey', 'Denzel Washington', 'Russell Crowe', 'Brad Pitt', 'Angelina Jolie', 'Leonardo DiCaprio', 'Tom Cruise', 'John Travolta', 'Arnold Schwarzenegger', 'Sylvester Stallone', 'Kate Winslet', 'Christian Bale', 'Morgan Freeman', 'Keanu Reeves', 'Hugh Jackman', 'Edward Norton', 'Bruce Willis', 'Tom Hanks', 'Charlize Theron', 'Will Smith', 'Sean Connery', 'Keira Knightley', 'Vin Diesel', 'Matt Damon', 'Richard Gere', 'Catherine Zeta-Jones', 'Clive Owen', 'Mel Gibson', 'George Clooney', 'Jack Nicholson', 'Scarlett Johansson', 'Tom Hardy', 'Samuel Jackson', 'Sandra Bullock', 'Meg Ryan', 'Nicole Kidman', 'Simon Baker', 'Cameron Diaz', 'Anthony Hopkins']
print(group_by_surname(lst))

