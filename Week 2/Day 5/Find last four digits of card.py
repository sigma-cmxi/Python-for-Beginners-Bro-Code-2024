credit_number = "1425453541549198"

masked_card = "X" * (len(credit_number) - 4) + credit_number[-4:]

print(masked_card)