# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
"""Assignment: Strings
Hugo Maat, 12 January 2022
This program reports on the goals in the 1988 UEFA football final
Version 1.1
Updated "scorers" to use + operand concatenation instead of f-strings
Revised Part 2 to function for generic names"""
#Part 1
scorer1 = 'Ruud Gullit'
scorer2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer1 + ' ' + str(goal_0) + ', ' + scorer2 + ' ' + str(goal_1)
report = f"""{scorer1} scored in the {goal_0}nd minute
{scorer2} scored in the {goal_1}th minute"""
#Part 2
player = 'Ruud Gullit'
first_name = player[:player.find(' ')]
last_name_len = len(player[(player.find(' ') + 1):])
name_short = f"{player[0]}. {player[(player.find(' ') + 1):]}"
chant = ((first_name + '! ') * len(first_name)).strip()
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