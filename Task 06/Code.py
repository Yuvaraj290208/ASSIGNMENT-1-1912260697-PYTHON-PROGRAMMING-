BASE_RATE = 30.00[span_92](start_span)[span_92](end_span)[span_93](start_span)[span_93](end_span)
BASE_FAT = 3.5[span_94](start_span)[span_94](end_span)[span_95](start_span)[span_95](end_span)
BASE_SNF = 8.5[span_96](start_span)[span_96](end_span)[span_97](start_span)[span_97](end_span)
FAT_STEP_VALUE = 0.40[span_98](start_span)[span_98](end_span)[span_99](start_span)[span_99](end_span)
SNF_STEP_VALUE = 0.30[span_100](start_span)[span_100](end_span)[span_101](start_span)[span_101](end_span)

def is_valid_entry(litres: float, fat: float, snf: float) -> bool:
    """Returns True if litres, fat %, and SNF % fall within valid cooperative bounds."""
    return litres > 0 and (2.0 <= fat <= 7.0) and (6.0 <= snf <= 11.0)[span_102](start_span)[span_102](end_span)

def rate_per_litre(fat: float, snf: float) -> float:[span_103](start_span)[span_103](end_span)[span_104](start_span)[span_104](end_span)
    """Computes and returns the milk rate per litre rounded to 2 decimal places.""[span_105](start_span)"[span_105](end_span)
    fat_steps = round((fat - BASE_FAT) / 0.1)[span_106](start_span)[span_106](end_span)[span_107](start_span)[span_107](end_span)
    snf_steps = round((snf - BASE_SNF) / 0.1)[span_108](start_span)[span_108](end_span)[span_109](start_span)[span_109](end_span)
    rate = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)[span_110](start_span)[span_110](end_span)
    return round(rate, 2)[span_111](start_span)[span_111](end_span)

def payout(litres: float, fat: float, snf: float) -> float:[span_112](start_span)[span_112](end_span)[span_113](start_span)[span_113](end_span)
    """Calculates and returns the payout for a single milk delivery rounded to 2 decimal places.""[span_114](start_span)"[span_114](end_span)
    if not is_valid_entry(litres, fat, snf):
        raise ValueError("Invalid milk entry parameters.")
    return round(litres * rate_per_litre(fat, snf), 2)[span_115](start_span)[span_115](end_span)

def ten_day_total(entries: list[tuple[float, float, float]]) -> float:[span_116](start_span)[span_116](end_span)
    """Returns the total payout across all valid entries in a ten-day billing cycle."""
    total = 0.0
    for litres, fat, snf in entries:
        total = round(total + payout(litres, fat, snf), 2)
    return total

if __name__ == "__main__":
    farmer_deliveries = [(10.0, 3.5, 8.5), (8.5, 4.2, 8.7), (12.0, 3.1, 8.3)][span_117](start_span)[span_117](end_span)
    print("Ten-day total:", ten_day_total(farmer_deliveries))
