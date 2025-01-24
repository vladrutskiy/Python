#inline (Single line) comment
# hello
# This 
# is 
# amount

"""And this is is for multiple
lines quotation
"""

pets_love = {
    "Rosie": {
        "Cuteness": 10,
        "Smarts": 5,
        "Attitude": 8,
        "Luck": 5
    }
}
pets_love["Elmer"] = 11
pets_love["Sherman"] = 8

pets_love["Sherman"] = 2
print("Joel loves Sherman", pets_love["Sherman"])
print("Rosie's smartness is ", pets_love["Rosie"]["Smarts"])