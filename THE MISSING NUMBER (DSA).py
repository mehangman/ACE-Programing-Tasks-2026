# ============================================================
#  THE MISSING NUMBER (DSA)
#  Two approaches: 1) Mathematical (Sum Formula)
#                  2) Data-Structure Based (Sort + Gap Check)
# ============================================================


def find_missing_mathematical(n, numbers):
    """
    Approach 1: Mathematical (Sum Formula)
    Logic: Sum of 1 to n = n*(n+1)/2 (expected sum).
    Subtract the actual sum of given numbers from expected sum.
    The difference is exactly the missing number.
    """
    expected_sum = n * (1 + n) // 2   # formula-based expected total [AP formula: n/2(1rst term + last term as n)]

    actual_sum = 0
    for num in numbers:               # manually add numbers (no built-in sum())
        actual_sum += num

    return expected_sum - actual_sum  # gap = missing number


def find_missing_dsa(n, numbers):
    """
    Approach 2: Data-Structure Based (Sorting + Gap Detection)
    Logic: Sort the list first. In a complete 1..n sequence,
    each number should be exactly 1 more than the previous one.
    Scan the sorted list; the first place this pattern breaks
    reveals the missing number.
    """
    numbers.sort()  # arrange numbers in ascending order (data structure step)

    # Edge case: if 1 itself is missing, first element won't be 1
    if numbers[0] != 1:
        return 1

    # Walk through sorted list checking for a break in sequence
    for i in range(1, len(numbers)):
        if numbers[i] != numbers[i - 1] + 1:
            return numbers[i - 1] + 1   # gap found here

    # Edge case: if n itself is missing, sequence never breaks
    return n


def get_input():
    """Takes n and the list of numbers as input from the user."""
    n = int(input("Enter the value of n: "))
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    return n, numbers


# ---------------- Main Program (Menu Driven) ----------------

print("\n" + "=" * 45)
print("        THE MISSING NUMBER (DSA)")
print("=" * 45)

while True:
    print("\n  1 - Mathematical Approach (Sum Formula)")
    print("  2 - DSA Approach (Sort + Gap Check)")
    print("  3 - Exit")
    print("-" * 45)

    choice = input("  Enter your choice: ")

    if choice == '1':
        n, numbers = get_input()
        missing = find_missing_mathematical(n, numbers)
        print(f"  Missing number: {missing}")

    elif choice == '2':
        n, numbers = get_input()
        missing = find_missing_dsa(n, numbers)
        print(f"  Missing number: {missing}")

    elif choice == '3':
        print("\n  Thank you for using THE MISSING NUMBER program!")
        print("=" * 45)
        break

    else:
        print("  Invalid choice. Please enter 1, 2, or 3.")
