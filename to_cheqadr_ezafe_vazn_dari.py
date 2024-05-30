#https://quera.org/problemset/3404

w = float(input())
h = float(input())

BMI = w / (h ** 2)
print(f"{BMI:.2f}")

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Overweight")
else:
    print("Obese")
