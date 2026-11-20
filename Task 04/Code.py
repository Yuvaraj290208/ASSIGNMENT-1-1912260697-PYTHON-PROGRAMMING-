import math[span_58](start_span)[span_58](end_span)

BASE_RATE = 30.00[span_59](start_span)[span_59](end_span)[span_60](start_span)[span_60](end_span)
BASE_FAT = 3.5[span_61](start_span)[span_61](end_span)[span_62](start_span)[span_62](end_span)
BASE_SNF = 8.5[span_63](start_span)[span_63](end_span)[span_64](start_span)[span_64](end_span)
FAT_STEP_VALUE = 0.40[span_65](start_span)[span_65](end_span)[span_66](start_span)[span_66](end_span)
SNF_STEP_VALUE = 0.30[span_67](start_span)[span_67](end_span)[span_68](start_span)[span_68](end_span)

def compute_payment_expressions(litres: float, fat: float, snf: float):
    # Correct step calculation using round() to eliminate float representation noise[span_69](start_span)[span_69](end_span)
    fat_steps = round((fat - BASE_FAT) / 0.1)[span_70](start_span)[span_70](end_span)[span_71](start_span)[span_71](end_span)
    snf_steps = round((snf - BASE_SNF) / 0.1)[span_72](start_span)[span_72](end_span)[span_73](start_span)[span_73](end_span)

    rate_per_litre = round(BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE), 2)[span_74](start_span)[span_74](end_span)
    amount = round(litres * rate_per_litre, 2)[span_75](start_span)[span_75](end_span)
    return fat_steps, snf_steps, rate_per_litre, amount

# Comparison of round() vs int() vs math.floor() on fat = 4.2 and fat = 3.1[span_76](start_span)[span_76](end_span)
for test_fat in (4.2, 3.1):[span_77](start_span)[span_77](end_span)
    raw_steps = (test_fat - 3.5) / 0.1[span_78](start_span)[span_78](end_span)
    print(f"Fat = {test_fat} | raw = {raw_steps!r}")[span_79](start_span)[span_79](end_span)
    print(f"  round(): {round(raw_steps)} -> Rate: {30.0 + round(raw_steps) * 0.40:.2f}")[span_80](start_span)[span_80](end_span)
    print(f"  int()  : {int(raw_steps)} -> Rate: {30.0 + int(raw_steps) * 0.40:.2f}")[span_81](start_span)[span_81](end_span)
    print(f"  floor(): {math.floor(raw_steps)} -> Rate: {30.0 + math.floor(raw_steps) * 0.40:.2f}")[span_82](start_span)[span_82](end_span)

# Three surprising expression demonstrations[span_83](start_span)[span_83](end_span)
print("\nSurprises:")
print("1. Float subtraction step:", (4.2 - 3.5) / 0.1)               # 7.000000000000001[span_84](start_span)[span_84](end_span)
print("2. Unary minus & power :", -3 ** 2, "vs", (-3) ** 2)         # -9 vs 9[span_85](start_span)[span_85](end_span)
print("3. Chained comparison  :", 2.0 <= 4.2 <= 7.0, 2.0 <= 8.0 <= 7.0)[span_86](start_span)[span_86](end_span)
