from colorama import Back, init
import json

init(autoreset=True)


def bmi_calculator(height, weight):

    if not isinstance(height, (int, float)) or not isinstance(weight, (int, float)):
        raise ValueError("Height and weight must be numbers.")

    bmi = round(weight / (height / 100) ** 2, 2)

    if bmi < 18.5:
        category = "underweight"

    elif 18.5 <= bmi < 24:
        category = "normal"

    elif 24 <= bmi < 27:
        category = "overweight"

    else:
        category = "obese"

    return {"height": height, "weight": weight, "bmi": bmi, "category": category}


if __name__ == "__main__":

    data = []

    try:
        height = float(input("Your height? "))
        weight = float(input("Your weight? "))

        while isinstance(height, float) and isinstance(weight, float):

            result = bmi_calculator(height, weight)
            data.append(result)
            print(result)

            height = float(input("Your height? "))
            weight = float(input("Your weight? "))

    except ValueError:
        print(f"{Back.RED}The program stops")
        if data:
            bmi_sum = 0
            underweight, normal, overweight, obese = 0, 0, 0, 0
            for d in data:
                print(d)
                bmi_sum += d["bmi"]

                match d["category"]:
                    case "underweight":
                        underweight += 1

                    case "normal":
                        normal += 1

                    case "overweight":
                        overweight += 1

                    case "obese":
                        obese += 1

            with open("bmi_data.json", "w") as json_file:
                json.dump(data, json_file, indent=4)

            print(f"Average BMI is {bmi_sum / len(data):.2f}")
            print(f"underweight: {underweight}")
            print(f"normal: {normal}")
            print(f"overweight: {overweight}")
            print(f"obese: {obese}")
