def bmi_calculator(height, weight):
    bmi = weight / (height / 100) ** 2

    if bmi < 18.5:
        return "underweight"

    elif 18.5 <= bmi < 24:
        return "normal weight"

    elif 24 <= bmi < 27:
        return "overweight"

    else:
        return "obese"


if __name__ == "__main__":
    height = float(input("Your height? "))
    weight = float(input("Your weight? "))

    result = bmi_calculator(height, weight)
    print(result)
