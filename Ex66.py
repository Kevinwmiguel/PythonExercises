"""
Ex 66 - Create a tuple filled with the top 20 in the table of the
Brazilian football championship, in the order of placement.
Then show:

A) The first five
B) the last four
C) The Teams in alphabetical order
4) What is position of Goias

"""
# ----- Var Zone -----
Brasileirao = ('Internacional', 'Atrletico-MG', 'Sao paulo',
               'Vasco da Gama', 'Flamengo', 'Palmeiras',
               'Santos', 'Fluminense','Ceara SC', 'Fortaleza',
               'Atletico-GO', 'Gremio', 'Athlretico-PR',
               'Sport Recife', 'Corinthians', 'Bahia',
               'Botafogo', 'Goias', 'Cutitiba',
               'Bragantino-SP')


# ----- Function zone -----
def line():
    print('-='*25)


# ----- Output Zone -----
print(f'The first five are: {Brasileirao[:5]}')
line()
print(f'the last four are: {Brasileirao[-1:-5:-1]}')
line()
print(f'Alphabetical teams {sorted(Brasileirao)}')  # SHow the teams in alphabetical order

print(f'The Goias are in {Brasileirao.index("Goias")}ª position')  # check the position (index) of Goias in tuple.

input()
