import json
from colorama import Fore, Back, Style, init
from collections import Counter

# 初始化 colorama
init(autoreset=True)


def bmi_calculator(height, weight):
    """計算 BMI 並回傳字典格式結果"""
    if not isinstance(height, (int, float)) or not isinstance(weight, (int, float)):
        raise ValueError("Height and weight must be numbers.")

    bmi = round(weight / (height / 100) ** 2, 2)

    # 設定 BMI 類別與對應顏色
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


def get_user_input():
    """取得使用者輸入的身高與體重，並轉換成浮點數"""
    try:
        height = float(input("Your height (cm)? "))
        weight = float(input("Your weight (kg)? "))
        return height, weight
    except ValueError:
        return None, None  # 當輸入無效時返回 None


def save_to_json(data, filename="bmi_data.json"):
    """將 BMI 數據存入 JSON 檔案"""
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


def main():
    """主執行函數"""
    data = []

    while True:
        height, weight = get_user_input()

        if height is None or weight is None:
            print(f"{Fore.RED}The program stops.{Style.RESET_ALL}")
            break

        result = bmi_calculator(height, weight)
        data.append(result)

        # 美化輸出
        print(f"{Fore.CYAN}Height:{Style.RESET_ALL} {result['height']} cm")
        print(f"{Fore.CYAN}Weight:{Style.RESET_ALL} {result['weight']} kg")
        print(f"{Fore.CYAN}BMI:{Style.RESET_ALL} {result['bmi']:.2f}")
        print(
            f"{Fore.CYAN}Category:{Style.RESET_ALL} {result['color']}{result['category']}{Style.RESET_ALL}"
        )
        print("=" * 40)

    # 如果有有效數據才進行統計與儲存
    if data:
        bmi_sum = sum(d["bmi"] for d in data)
        avg_bmi = bmi_sum / len(data)

        # 統計分類次數
        category_counts = Counter(d["category"] for d in data)

        # 儲存結果至 JSON
        save_to_json(data)

        # 顯示統計結果
        print(f"{Fore.GREEN}Average BMI:{Style.RESET_ALL} {avg_bmi:.2f}")
        print("=" * 40)
        for category, count in category_counts.items():
            color = {
                "underweight": Fore.BLUE,
                "normal": Fore.GREEN,
                "overweight": Fore.YELLOW,
                "obese": Fore.RED,
            }[category]
            print(f"{color}{category}:{Style.RESET_ALL} {count}")


if __name__ == "__main__":
    main()
