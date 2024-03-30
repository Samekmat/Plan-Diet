def bmr_calc(sex, weight, height, age):
    weight = float(weight)
    height = float(height)
    age = float(age)
    if sex == "male":
        bmr = (9.99 * weight) + (6.25 * height) - (4.92 * age) + 5
        return round(bmr)
    elif sex == "female":
        bmr = (9.99 * weight) + (6.25 * height) - (4.92 * age) - 161
        return round(bmr)
