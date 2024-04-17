def bmr_calc(sex: str, weight: float, height: float, age: int) -> float:
    weight = float(weight)
    height = float(height)
    age = int(age)
    if sex == "male":
        bmr = (9.99 * weight) + (6.25 * height) - (4.92 * age) + 5
        return round(bmr)
    elif sex == "female":
        bmr = (9.99 * weight) + (6.25 * height) - (4.92 * age) - 161
        return round(bmr)
