# a + b + c + d + e = 30
# c + e = 14
# b + c = 10
# d - b = 1 
# b2 = a - 1


#  a + b + d + 14 = 30
#  a + b + d = 16
#  

def pins_total(pins_digits):
    sum_digits = 0
    for k in pins_digits:
        sum_digits += pins_digits[k] 
    print(sum_digits)


def pin_is_ok(pins_digits):
    if pins_digits["fifth"] + pins_digits["third"] == 14 and \
    pins_digits["first"] == pins_digits["second"] * 2 - 1 and \
    pins_digits["forth"] - 1 == pins_digits["second"] and \
    pins_digits["second"] + pins_digits["third"] == 10 :
        if pins_total(pins_digits) == 30:
            return True

# zfill adds "0" before number
for pins in range(0, 100000):
    this_pin = str(pins).zfill(5)

    pins_digits = {}
    pins_digits["first"] = int(this_pin[0])
    pins_digits["second"] = int(this_pin[1])
    pins_digits["third"] = int(this_pin[2])
    pins_digits["forth"] = int(this_pin[3])
    pins_digits["fifth"] = int(this_pin[4])

