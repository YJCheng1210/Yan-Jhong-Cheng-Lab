warrior_lineups = {
    '2008': ['Kelenna Azubuike', 'Jamal Crawford', 'Monta Ellis', 'Stephen Jackson', 'Ronny Turiaf'],
    '2009': ['Stephen Curry', 'Monta Ellis', 'Chris Hunter', 'Corey Maggette', 'Anthony Tolliver'],
    '2010': ['Andris Biedriņš', 'Stephen Curry', 'Monta Ellis', 'David Lee', 'Dorell Wright'],
    '2011': ['Andris Biedriņš', 'Stephen Curry', 'Monta Ellis', 'David Lee', 'Dorell Wright'],
    '2012': ['Harrison Barnes',  'Andrew Bogut', 'Stephen Curry', 'David Lee', 'Klay Thompson'],
    '2013': ['Andrew Bogut', 'Stephen Curry', 'Andrew Iguodala', 'David Lee', 'Klay Thompson'],
    '2014': ['Harrison Barnes', 'Andrew Bogut', 'Stephen Curry', 'Draymond Green', 'Klay Thompson'],
    '2015': ['Harrison Barnes', 'Andrew Bogut', 'Stephen Curry', 'Draymond Green', 'Klay Thompson'],
    '2016': ['Stephen Curry', 'Kevin Durant', 'Draymond Green', 'Zaza Pachulia', 'Klay Thompson'],
    '2017': ['Stephen Curry', 'Kevin Durant', 'Draymond Green', 'Zaza Pachulia', 'Klay Thompson'],
    '2018': ['Stephen Curry', 'Kevin Durant', 'Draymond Green', 'Damian Jones', 'Klay Thompson'],
    '2019': ['Stephen Curry', 'Draymond Green', 'Kevon Looney', 'Glenn Robinson', 'DAngelo Russell'],
    '2020': ['Stephen Curry', 'Draymond Green', 'Kelly Oubre', 'Andrew Wiggins', 'James Wiseman'],
    '2021': ['Stephen Curry', 'Draymond Green', 'Kevon Looney', 'Jordan Poole', 'Andrew Wiggins'],
}

member = input('Enter a starting member: ')

print(f"Name: {member}")

years = []

for k, v in warrior_lineups.items():
    if member in v:
        years.append(k)

print(f"Starting Years: {years}")