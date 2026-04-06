# ============================================================
# Practice Task: Grade Calculator
# ============================================================
# Set a variable score = 85 (or any number).
#
# 1. Print the letter grade based on these rules:
#    90+      → A
#    80 - 89  → B
#    70 - 79  → C
#    below 70 → F
#
# Bonus: First check if the score is valid (between 0 and 100)
#        before calculating the grade.

score = 100

# check if score is between 0 and 100 first
if (0 <= score <= 100):
    if (score >= 90):
        print('A')
    elif (score >= 80):
        print('B')
    elif (score >= 70):
        print('C')
    else:
        print('F')
else:
    print('Score is out of range')