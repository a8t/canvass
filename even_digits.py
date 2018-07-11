all_digits_even = []

# None of the 1XXX or 29XXs will be included b/c 9 is odd, so don't bother checking
for x in range(2000, 2900):
    # int is truncated so 28 / 10 = 2, not 2.8; so this check is valid without floor operation
    if x % 2 == 0 and x / 10 % 2 == 0 and x / 100 % 2 == 0 and x / 1000 % 2 == 0:
        # Convert to string for convenience when joining.
        all_digits_even.append(str(x))

print(','.join(all_digits_even))
