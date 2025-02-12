#inline (Single line) comment
# hello
# This 
# is 
# amount

"""And this is is for multiple
lines quotation
"""
# We are declaring a list with Rosie's abilities
pets_love = {
    "Rosie": {
        "Cuteness": 10,
        "Smarts": 5,
        "Attitude": 8,
        "Luck": 5
    }
}
# We are adding Elmer and Sherman general love capacity
pets_love["Elmer"] = 11
pets_love["Sherman"] = 8

# Sherman losses a lots of love here
pets_love["Sherman"] = 2

# We are asking the user to share his/her Sherman's love-level
pets_love["Sherman"] = input ("Enter how much do you love this cat: ")
print("Joel loves Sherman", pets_love["Sherman"])
print("Rosie's smartness is ", pets_love["Rosie"]["Smarts"])