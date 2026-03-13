def get_valid_input(prompt, input_type=float, min_value=None, max_value=None):
    while True:
        try:
            value = input_type(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a value between {min_value} and {max_value}.")
            else:
                return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    print("Welcome to the BMI Calculator")

    weight = get_valid_input("Please enter your weight in kilograms: ", float, 0.1, 500)
    height = get_valid_input("Please enter your height in meters: ", float, 0.1, 3)

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")

if __name__ == "__main__":
    main()