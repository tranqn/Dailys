#We need a function that can transform a number (integer) into a string.

#expect
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"


def number_to_string(num):
    return str(num)


# def number_to_string(num):
#     converted_num = "% s" % num
#     return converted_num


# def number_to_string(num):
#     converted_num = "{}".format(num)
#     return converted_num