def find_cube_pairs(target):                 # adding a colon
    solutions = []                              # removing semicolon
    max_num = round(target ** (1/3))          # removing 1 * as *** isn't recognized by python and changig tar to target  

    for a in range(1, max_num + 1):         # adding a colon and changing ranges to range
        for b in range(a, max_num + 1):     # adding a colon and changing ranges to range
            if a**3 + b**3 == target:        # removing 1 * as *** isn't recognized by python and adding a colon
                solutions.append((a, b))    # changing sol to solutions and removing semicolon
    return solutions                        # changing sol to solutions

pairs = find_cube_pairs(1729)               # removing comma
print("Valid cube pairs for 1729:")        # removing comma and changing printf to print and changing 1728 to 1729
for a, b in pairs:                               # adding a colon and changing pair to pairs
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") # changing printf to print and changing 2 to 3 and changing 1728 to 1729

# """Submit your response here:  https://forms.office.com/Pages/ResponsePage.aspx?id=vDsaA3zPK06W7IZ1VVQKHFzW4INMf2JMjyL9qPnlPbNUMFU2TjI1WjQyUlczSFNIOFBEWkxTQ0lFQS4u"""
