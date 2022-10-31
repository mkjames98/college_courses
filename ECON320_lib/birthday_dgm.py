import math

import pandas as pd

# function that finds the variance using my birthday,
# note that "scale" parameter in rng.normal is standard deviation
# so we have to square root the result to use it in rng.normal, since I return the Variance.
def birthday_str_variance_srm(birthday_string):
    for b in list(birthday_string):
        if b != "0":
            var_x = int(b)
            break
    for revb in reversed(list(birthday_string)):
        if revb != "0":
            var_u = int(revb)
            break
    return var_x, var_u


def generate_srm_birthday(
    birthday_string, rng, x_mean, u_mean, size
):  # x_mean = 10, u_mean =0
    # beta0 is addition of 3rd and 4th digit of my birthday
    pop_beta0 = int(birthday_string[2]) + int(birthday_string[3])
    # beta1 is addition of 1st and 2nd digit of my birthday
    pop_beta1 = int(birthday_string[0]) + int(birthday_string[1])
    # set scale, scale should be std, so sqrt the result
    var_x, var_u = birthday_str_variance_srm(birthday_string)
    scale_x = math.sqrt(var_x)
    scale_u = math.sqrt(var_u)

    x = rng.normal(loc=x_mean, scale=scale_x, size=size)
    print(
        f"x is normally distributed with a mean of {x_mean} and variance of {round(var_x,3)}"
    )
    u = rng.normal(loc=u_mean, scale=scale_u, size=size)
    print(
        f"u is normally distributed with a mean of {u_mean} and variance of {round(var_u,3)}"
    )

    y = pop_beta0 + pop_beta1 * x + u
    print(f"y = {int(pop_beta0)} + {int(pop_beta1)}*x + u ")
    gdata = {"x": x, "u": u, "y": y}
    df = pd.DataFrame(data=gdata)
    return df, pop_beta0, pop_beta1


# refactored for mrm
def birthday_str_variance_mrm(birthday_string):
    for b in list(birthday_string):
        if b != "0":
            var_x1 = int(b)
            break
    for revb in reversed(list(birthday_string)):
        if revb != "0":
            var_u = int(revb)
            break
    var_x2 = int(birthday_string[0]) + int(birthday_string[1])
    return var_x1, var_x2, var_u


# refactored for mrm
def generate_mrm_birthday(
    birthday_string, rng, x1_mean, x2_mean, u_mean, size
):  # x_mean = 10, u_mean =0
    # beta0 is addition of 3rd and 4th digit of my birthday
    pop_beta0 = int(birthday_string[2]) + int(birthday_string[3])
    # beta1 is addition of 1st and 2nd digit of my birthday
    pop_beta1 = int(birthday_string[0]) + int(birthday_string[1])
    # beta2 is addition of 5th and 6th digit of my birthday
    pop_beta2 = int(birthday_string[4]) + int(birthday_string[5])
    # set scale, scale should be std, so sqrt the result
    var_x1, var_x2, var_u = birthday_str_variance_mrm(birthday_string)
    scale_x1 = math.sqrt(var_x1)
    scale_x2 = math.sqrt(var_x2)
    scale_u = math.sqrt(var_u)

    x_1 = rng.normal(loc=x1_mean, scale=scale_x1, size=size)
    print(
        f"x_1 is normally distributed with a mean of {x1_mean} and variance of {round(var_x1,3)}"
    )
    x_2 = rng.normal(loc=x2_mean, scale=scale_x2, size=size)
    print(
        f"x_2 is normally distributed with a mean of {x2_mean} and variance of {round(var_x2,3)}"
    )
    u = rng.normal(loc=u_mean, scale=scale_u, size=size)
    print(
        f"u is normally distributed with a mean of {u_mean} and variance of {round(var_u,3)}"
    )

    y = pop_beta0 + pop_beta1 * x_1 + pop_beta2 * x_2 + u
    print(f"y = {int(pop_beta0)} + {int(pop_beta1)}*x_1 + {int(pop_beta2)}*x_2 + u ")
    gdata = {"x_1": x_1, "x_2": x_2, "u": u, "y": y}
    df = pd.DataFrame(data=gdata)
    return df, pop_beta0, pop_beta1, pop_beta2
