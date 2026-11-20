# Named constants in UPPER_CASE for single-point rate revisions[span_30](start_span)[span_30](end_span)
BASE_RATE = 30.00[span_31](start_span)[span_31](end_span)[span_32](start_span)[span_32](end_span)
BASE_FAT = 3.5[span_33](start_span)[span_33](end_span)[span_34](start_span)[span_34](end_span)
BASE_SNF = 8.5[span_35](start_span)[span_35](end_span)[span_36](start_span)[span_36](end_span)

FAT_STEP_SIZE = 0.1[span_37](start_span)[span_37](end_span)[span_38](start_span)[span_38](end_span)
SNF_STEP_SIZE = 0.1[span_39](start_span)[span_39](end_span)[span_40](start_span)[span_40](end_span)

FAT_STEP_VALUE = 0.40[span_41](start_span)[span_41](end_span)[span_42](start_span)[span_42](end_span)
SNF_STEP_VALUE = 0.30[span_43](start_span)[span_43](end_span)[span_44](start_span)[span_44](end_span)

MIN_FAT = 2.0[span_45](start_span)[span_45](end_span)
MAX_FAT = 7.0[span_46](start_span)[span_46](end_span)
MIN_SNF = 6.0[span_47](start_span)[span_47](end_span)
MAX_SNF = 11.0[span_48](start_span)[span_48](end_span)

# Alternative dictionary representation mentioned in analysis[span_49](start_span)[span_49](end_span)
RATE_CARD = {
    "base": 30.00,[span_50](start_span)[span_50](end_span)
    "fat": 0.40,[span_51](start_span)[span_51](end_span)
    "snf": 0.30,[span_52](start_span)[span_52](end_span)
}

# Demonstration of dynamic typing and tuple swapping[span_53](start_span)[span_53](end_span)
sample_var = 10          # int[span_54](start_span)[span_54](end_span)
print(sample_var, type(sample_var))
sample_var = "F101"      # dynamically rebound to str[span_55](start_span)[span_55](end_span)
print(sample_var, type(sample_var))

a, b = 3.5, 8.5
a, b = b, a              # Pythonic swap without temp variable[span_56](start_span)[span_56](end_span)
print(f"Swapped: a={a}, b={b}")
