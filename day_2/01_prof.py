import json
from collections import Counter
from colorama import Fore, Style, init

# 初始化 colorama
init(autoreset=True)


def get_user_data():
    """取得使用者輸入的身高與體重，允許輸入多筆資料"""
    data = []

    while True:
        try:
            height = input("Enter height in cm (or 'q' to quit): ")
            if height.lower() == "q":  # 允許用戶退出輸入
                break
            weight = input("Enter weight in kg: ")

            height, weight = float(height), float(weight)

            result = bmi_calculator(height, weight)
            data.append(result)

            # 顯示輸出
            print(f"{Fore.CYAN}Height:{Style.RESET_ALL} {result['height']} cm")
            print(f"{Fore.CYAN}Weight:{Style.RESET_ALL} {result['weight']} kg")
            print(f"{Fore.CYAN}BMI:{Style.RESET_ALL} {result['bmi']:.2f}")
            print(
                f"{Fore.CYAN}Category:{Style.RESET_ALL} {result['color']}{result['category']}{Style.RESET_ALL}"
            )
            print("=" * 40)

        except ValueError:
            print(
                f"{Fore.RED}Invalid input. Please enter numbers for height and weight.{Style.RESET_ALL}"
            )

    return data


def bmi_calculator(height, weight):
    """計算 BMI 並分類"""
    bmi = round(weight / (height / 100) ** 2, 2)

    if bmi < 18.5:
        category, color = "underweight", Fore.BLUE
    elif 18.5 <= bmi < 24:
        category, color = "normal", Fore.GREEN
    elif 24 <= bmi < 27:
        category, color = "overweight", Fore.YELLOW
    else:
        category, color = "obese", Fore.RED

    return {
        "height": height,
        "weight": weight,
        "bmi": bmi,
        "category": category,
        "color": color,
    }


def save_to_json(data, filename="bmi_data.json"):
    """儲存 BMI 結果到 JSON 檔案"""
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"{Fore.GREEN}Data successfully saved to {filename}.{Style.RESET_ALL}")


def analyze_bmi_data(filename="bmi_data.json"):
    """讀取 JSON 檔案並分析數據"""
    try:
        with open(filename, "r") as json_file:
            data = json.load(json_file)

        if not data:
            print(f"{Fore.YELLOW}No data found in {filename}.{Style.RESET_ALL}")
            return

        # 計算平均 BMI
        bmi_sum = sum(d["bmi"] for d in data)
        avg_bmi = bmi_sum / len(data)

        # 使用 Counter 計算各分類人數
        category_counts = Counter(d["category"] for d in data)

        # 顯示結果
        print(f"\n{Fore.MAGENTA}=== BMI Data Analysis ==={Style.RESET_ALL}")
        print(f"{Fore.GREEN}Average BMI:{Style.RESET_ALL} {avg_bmi:.2f}")
        for category, count in category_counts.items():
            color = {
                "underweight": Fore.BLUE,
                "normal": Fore.GREEN,
                "overweight": Fore.YELLOW,
                "obese": Fore.RED,
            }[category]
            print(f"{color}{category}:{Style.RESET_ALL} {count}")

    except FileNotFoundError:
        print(f"{Fore.RED}Error: {filename} not found.{Style.RESET_ALL}")
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error: {filename} is not a valid JSON file.{Style.RESET_ALL}")


def main():
    """主執行流程"""
    print(f"{Fore.MAGENTA}Welcome to the BMI Calculator!{Style.RESET_ALL}")

    # 取得使用者輸入並計算 BMI
    user_data = get_user_data()

    if user_data:
        save_to_json(user_data)
        analyze_bmi_data()


if __name__ == "__main__":
    main()
