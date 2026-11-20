import random
import time[span_188](start_span)[span_188](end_span)
from decimal import Decimal, ROUND_HALF_UP

def generate_dataset(n: int):
    random.seed(42)
    return [
        (
            round(random.uniform(2.0, 25.0), 1),
            round(random.uniform(2.5, 6.5), 1),
            round(random.uniform(7.5, 9.5), 1),
        )
        for _ in range(n)
    ]

def run_float_unrounded_entries(data):
    total = 0.0
    for litres, fat, snf in data:
        rate = 30.00 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30[span_189](start_span)[span_189](end_span)
        total += litres * rate
    return round(total, 2)

def run_float_rounded_entries(data):
    total = 0.0
    for litres, fat, snf in data:
        rate = round(30.00 + round((fat - 3.5) / 0.1) * 0.40 + round((snf - 8.5) / 0.1) * 0.30, 2)[span_190](start_span)[span_190](end_span)
        total += round(litres * rate, 2)
    return round(total, 2)

def run_decimal_exact(data):
    total = Decimal("0.00")
    for litres, fat, snf in data:
        fat_steps = Decimal(str(round((fat - 3.5) / 0.1)))[span_191](start_span)[span_191](end_span)
        snf_steps = Decimal(str(round((snf - 8.5) / 0.1)))[span_192](start_span)[span_192](end_span)
        rate = Decimal("30.00") + fat_steps * Decimal("0.40") + snf_steps * Decimal("0.30")[span_193](start_span)[span_193](end_span)
        pay = (Decimal(str(litres)) * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        total += pay
    return total

def run_lookup_table(data):
    # Precompute O(1) lookup dictionary for all valid (fat, snf) pairs[span_194](start_span)[span_194](end_span)
    rate_table = {}[span_195](start_span)[span_195](end_span)
    for f_int in range(20, 71):
        for s_int in range(60, 111):
            f, s = f_int / 10, s_int / 10
            rate_table[(f, s)] = Decimal("30.00") + Decimal(f_int - 35) * Decimal("0.40") + Decimal(s_int - 85) * Decimal("0.30")
    total = Decimal("0.00")
    for litres, fat, snf in data:
        pay = (Decimal(str(litres)) * rate_table[(fat, snf)]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        total += pay
    return total

for size in (300, 6000, 150000):[span_196](start_span)[span_196](end_span)[span_197](start_span)[span_197](end_span)
    dataset = generate_dataset(size)

    t0 = time.perf_counter()[span_198](start_span)[span_198](end_span)
    f_res = run_float_rounded_entries(dataset)
    t_float = time.perf_counter() - t0[span_199](start_span)[span_199](end_span)

    t0 = time.perf_counter()[span_200](start_span)[span_200](end_span)
    d_res = run_decimal_exact(dataset)
    t_dec = time.perf_counter() - t0[span_201](start_span)[span_201](end_span)

    t0 = time.perf_counter()[span_202](start_span)[span_202](end_span)
    l_res = run_lookup_table(dataset)
    t_lookup = time.perf_counter() - t0[span_203](start_span)[span_203](end_span)

    diff = abs(Decimal(str(f_res)) - d_res)
    print(f"N={size:<6} | Float: {f_res:<12} ({t_float:.4f}s) | Decimal: {d_res:<12} ({t_dec:.4f}s) | Lookup: {t_lookup:.4f}s | Diff: Rs {diff}")[span_204](start_span)[span_204](end_span)
