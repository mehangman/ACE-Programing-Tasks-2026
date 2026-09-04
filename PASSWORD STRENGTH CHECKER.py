# ============================================================
#  Password Strength Checker - Basic Level Python Code
# ============================================================

def check1(password):      # Check minimum length
    if len(password) >= 8:
        return True
    else:
        return False

def check2(password):      # Check uppercase letter
    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            return True        # exits the function IMMEDIATELY if found
    return False               # only reaches here if loop finishes without finding one

def check3(password):      # Check lowercase letter
    for ch in password:
        if ch >= 'a' and ch <= 'z':
            return True
    return False

def check4(password):      # Check digit
    for ch in password:
        if ch >= '0' and ch <= '9':
            return True
    return False

def check5(password):      # Check special character
    special = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    for ch in password:
        if ch in special:
            return True
    return False

def check6(password):      # Check at least 3 digits, not consecutive
    count = 0
    for i in range(len(password)):
        if password[i] >= '0' and password[i] <= '9':
            count = count + 1                         # count all digits
            if i + 1 < len(password):                 # if next character exists
                next_digit = str(int(password[i]) + 1)
                if next_digit == password[i + 1]:
                    return False                      # consecutive pair found
    if count >= 3:
        return True
    else:
        return False

# ---- Main Program ----

print("\nPassword Strength Checker")
print("-" * 45)
print("A strong password must have:")
print("  - At least 8 characters")
print("  - One uppercase letter (A-Z)")
print("  - One lowercase letter (a-z)")
print("  - One number (0-9)")
print("  - One special character (!@# etc.)")
print("  - 3 or more digits, none consecutive")
print("-" * 45)

password = input("Enter your password: ")

# Store all check results in a list
checks = [check1(password), check2(password), check3(password),
          check4(password), check5(password), check6(password)]

labels = ["At least 8 characters", "Contains uppercase letter",
          "Contains lowercase letter", "Contains a number",
          "Contains special character", "3+ digits, none consecutive"]

# To display results
print("\nPassword Analysis")
print("-" * 35)
for i in range(6):
    if checks[i] == True:
        print("  [✔]", labels[i])
    else:
        print("  [✘]", labels[i])

# Calculating score using for loop
score = 0
for result in checks:
    if result == True:
        score = score + 1

# Overall strength rating
print("-" * 35)
print("Score :", score, "/ 6")

if score <= 2:
    print("Strength : WEAK")
elif score <= 4:
    print("Strength : MEDIUM")
elif score == 5:
    print("Strength : STRONG")
else:
    print("Strength : EXTREME")

print("-" * 35)
