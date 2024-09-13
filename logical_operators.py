# logical operators = evaluate multiple conditions (or, and, not)
    # or = at least one condition must be True
    # and = both conditions must be True
    # not = inverts the condition (not False, not True)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("Picnic is cancelled")
else:
    print("Picnic is happening")

if temp > 20 and not is_raining:
    print("Picnic is happening again")