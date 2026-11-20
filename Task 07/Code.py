"""Rate card of the village milk co-operative (used as a module).""[span_120](start_span)"[span_120](end_span)

BASE_RATE = 30.00       # Rs per litre for milk with 3.5% fat and 8.5% SNF[span_121](start_span)[span_121](end_span)
FAT_STEP_VALUE = 0.40   # Rs per litre for every 0.1% of fat above or below 3.5[span_122](start_span)[span_122](end_span)
SNF_STEP_VALUE = 0.30   # Rs per litre for every 0.1% of SNF above or below 8.5[span_123](start_span)[span_123](end_span)

def rate_per_litre(fat, snf):[span_124](start_span)[span_124](end_span)
    """Returns the price per litre, rounded to 2 decimals.""[span_125](start_span)"[span_125](end_span)
    # TODO 1: Count the 0.1% steps of fat from 3.5 and of SNF from 8.5 (round to the
    # nearest whole step), add their values to BASE_RATE, and round to 2 decimals.[span_126](start_span)[span_126](end_span)
    fat_steps = round((fat - 3.5) / 0.1)[span_127](start_span)[span_127](end_span)
    snf_steps = round((snf - 8.5) / 0.1)[span_128](start_span)[span_128](end_span)
    rate = BASE_RATE + (fat_steps * FAT_STEP_VALUE) + (snf_steps * SNF_STEP_VALUE)[span_129](start_span)[span_129](end_span)
    return round(rate, 2)[span_130](start_span)[span_130](end_span)

def payout(litres, fat, snf):[span_131](start_span)[span_131](end_span)
    """Returns the amount payable to the farmer, rounded to 2 decimals.""[span_132](start_span)"[span_132](end_span)
    # TODO 2: Multiply litres by the rate per litre and round to 2 decimals.[span_133](start_span)[span_133](end_span)
    return round(litres * rate_per_litre(fat, snf), 2)[span_134](start_span)[span_134](end_span)

if __name__ == "__main__":[span_135](start_span)[span_135](end_span)
    for litres, fat, snf in [(10, 3.5, 8.5), (8.5, 4.2, 8.7), (12, 3.1, 8.3)]:[span_136](start_span)[span_136](end_span)
        rate, pay = rate_per_litre(fat, snf), payout(litres, fat, snf)[span_137](start_span)[span_137](end_span)
        print(f"{litres:5} L fat {fat} snf {snf} rate {rate:6.2f} pay {pay:8.2f}")[span_138](start_span)[span_138](end_span)
        
