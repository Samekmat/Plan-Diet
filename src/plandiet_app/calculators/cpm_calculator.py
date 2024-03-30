def cpm_calc(goal, bmr, activity):
    bmr = float(bmr)
    activity = float(activity)
    if goal == "reduce":
        cpm = bmr * activity
        cpm -= 0.1 * cpm
        return round(cpm)
    elif goal == "maintain":
        cpm = bmr * activity
        return round(cpm)
    else:
        cpm = bmr * activity
        cpm += 0.1 * cpm
        return round(cpm)
