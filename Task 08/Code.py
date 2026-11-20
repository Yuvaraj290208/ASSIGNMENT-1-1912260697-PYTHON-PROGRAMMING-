from milkrate import payout[span_151](start_span)[span_151](end_span)

# O(1) auxiliary space streaming implementation[span_152](start_span)[span_152](end_span)
def compute_ten_day_streaming(entries):
    total = 0.0[span_153](start_span)[span_153](end_span)
    for litres, fat, snf in entries:
        if litres > 0 and (2.0 <= fat <= 7.0) and (6.0 <= snf <= 11.0):[span_154](start_span)[span_154](end_span)
            amount = payout(litres, fat, snf)
            total = round(total + amount, 2)
        else:
            print(f"Invalid entry skipped: {(litres, fat, snf)}")[span_155](start_span)[span_155](end_span)
    return total

# Hand-trace sample verification[span_156](start_span)[span_156](end_span)
sample_entries = [(10.0, 3.5, 8.5), (8.5, 4.2, 8.7), (-2.0, 4.0, 8.5)]
print("Ten-day streaming total:", compute_ten_day_streaming(sample_entries))
      
