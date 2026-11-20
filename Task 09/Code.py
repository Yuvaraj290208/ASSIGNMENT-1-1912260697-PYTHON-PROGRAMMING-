from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")[span_158](start_span)[span_158](end_span)[span_159](start_span)[span_159](end_span)
FAT_STEP_VALUE = Decimal("0.40")[span_160](start_span)[span_160](end_span)[span_161](start_span)[span_161](end_span)
SNF_STEP_VALUE = Decimal("0.30")[span_162](start_span)[span_162](end_span)[span_163](start_span)[span_163](end_span)

def validate_entry(litres, fat, snf) -> bool:
    if not all(isinstance(x, (int, float, Decimal)) and not isinstance(x, bool) for x in (litres, fat, snf)):
        return False
    return litres > 0 and (2.0 <= float(fat) <= 7.0) and (6.0 <= float(snf) <= 11.0)[span_164](start_span)[span_164](end_span)

def calculate_rate(fat: float, snf: float) -> Decimal:
    fat_steps = Decimal(str(round((fat - 3.5) / 0.1)))[span_165](start_span)[span_165](end_span)
    snf_steps = Decimal(str(round((snf - 8.5) / 0.1)))[span_166](start_span)[span_166](end_span)
    rate = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)[span_167](start_span)[span_167](end_span)
    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def calculate_payout(litres: float, fat: float, snf: float) -> Decimal:
    if not validate_entry(litres, fat, snf):
        raise ValueError(f"Invalid entry: litres={litres}, fat={fat}, snf={snf}")
    rate = calculate_rate(fat, snf)
    amount = Decimal(str(litres)) * rate
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def calculate_batch_total(entries: list) -> Decimal:
    total = Decimal("0.00")
    for litres, fat, snf in entries:
        total += calculate_payout(litres, fat, snf)
    return total

def run_tests():[span_168](start_span)[span_168](end_span)
    # 1. Normal entries (above and below standard)[span_169](start_span)[span_169](end_span)
    assert calculate_payout(8.5, 4.2, 8.7) == Decimal("283.90")[span_170](start_span)[span_170](end_span)[span_171](start_span)[span_171](end_span)
    assert calculate_payout(12.0, 3.1, 8.3) == Decimal("333.60")[span_172](start_span)[span_172](end_span)[span_173](start_span)[span_173](end_span)

    # 2. Boundary entries (3.5/8.5, lowest fat 2.0, highest fat 7.0)[span_174](start_span)[span_174](end_span)
    assert calculate_payout(10.0, 3.5, 8.5) == Decimal("300.00")[span_175](start_span)[span_175](end_span)[span_176](start_span)[span_176](end_span)
    assert calculate_rate(2.0, 8.5) == Decimal("24.00")[span_177](start_span)[span_177](end_span)
    assert calculate_rate(7.0, 8.5) == Decimal("44.00")[span_178](start_span)[span_178](end_span)

    # 3. Invalid entries (text, negative quantity, out-of-range fat)[span_179](start_span)[span_179](end_span)
    for bad in [("ten", 3.5, 8.5), (-5.0, 3.5, 8.5), (10.0, 1.9, 8.5), (10.0, 7.1, 8.5)]:[span_180](start_span)[span_180](end_span)
        try:
            calculate_payout(*bad)
            assert False, f"Expected ValueError for {bad}"
        except ValueError:
            pass

    # 4. Small set of 5 entries verified by hand[span_181](start_span)[span_181](end_span)
    five_entries = [
        (10.0, 3.5, 8.5),  # 300.00[span_182](start_span)[span_182](end_span)
        (8.5, 4.2, 8.7),   # 283.90[span_183](start_span)[span_183](end_span)
        (12.0, 3.1, 8.3),  # 333.60[span_184](start_span)[span_184](end_span)
        (5.0, 4.0, 9.0),   # 5 * (30 + 2.0 + 1.5) = 167.50
        (6.0, 3.0, 8.0),   # 6 * (30 - 2.0 - 1.5) = 159.00
    ]
    assert calculate_batch_total(five_entries) == Decimal("1244.00")[span_185](start_span)[span_185](end_span)
    print("All Task 9 assertions passed successfully!")[span_186](start_span)[span_186](end_span)

if __name__ == "__main__":
    run_tests()
  
