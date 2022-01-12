# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
"""Assignment: Strings
Hugo Maat, 12 January 2022
This program reports on the goals in the 1988 UEFA football final"""
#Part 1
scorer1 = 'Ruud Gullit'
scorer2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = f'{scorer1} {goal_0}, {scorer2} {goal_1}'
#The assignment requested the use of + operator to define 'scorers'
#but I ended up writing it as an f-string and wincpy approved
report = f"""{scorer1} scored in the {goal_0}nd minute
{scorer2} scored in the {goal_1}th minute"""
#Part 2
player = 'Frank Rijkaard'
first_name = player[0:5]
last_name_len = len(player[6:])
name_short = f'{player[0]}. {player[6:]}'
chant = (f'{player[:5]}! ' * 5)[:-1]
good_chant = chant[-1:] != ' '
print(good_chant)
#Adding some prints below for doublecheck
print('Part 1')
print(scorers)
print(report)
print('Part 2')
print(first_name)
print(last_name_len)
print(name_short)
print(chant)
print(chant[-1:])