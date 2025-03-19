def bmi_calculator(height, weight):
    bmi = weight / (height / 100) ** 2

    if bmi < 18.5:
        return "too skinny"

    elif 27 > bmi >= 24:
        return "over weight"

    elif bmi >= 27:
        return "too heavy"

    else:
        return "normal"


if __name__ == "__main__":
    height = float(input("Your height? "))
    weight = float(input("Your weight? "))

    result = bmi_calculator(height, weight)
    print(result)
