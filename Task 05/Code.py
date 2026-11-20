def is_valid_number(text: str) -> bool:
    """Checks if a stripped string represents a valid positive/negative decimal number using str methods."""
    cleaned = text.strip()
    if cleaned.startswith(("+", "-")):
        cleaned = cleaned[1:]
    if not cleaned or cleaned.count(".") > 1:
        return False
    return cleaned.replace(".", "", 1).isdigit()

def read_float_string_check(prompt: str) -> float:
    """Reads and validates float input using string inspection before conversion.""[span_88](start_span)"[span_88](end_span)
    while True:
        raw = input(prompt)
        if is_valid_number(raw):
            return float(raw.strip())
        print(f"Invalid numeric input: {raw!r}. Please try again.")

def read_float_try_except(prompt: str) -> float:
    """Alternative EAFP approach using try/except ValueError.""[span_89](start_span)"[span_89](end_span)
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print(f"Invalid numeric input: {raw!r}. Please try again.")

# Formatted table output using f-string width and precision[span_90](start_span)[span_90](end_span)
if __name__ == "__main__":
    sample_records = [
        ("F001", 10.0, 3.5, 8.5, 30.00, 300.00),
        ("F002", 8.5, 4.2, 8.7, 33.40, 283.90),
    ]
    print(f"{'ID':<6} {'Litres':>8} {'Fat%':>6} {'SNF%':>6} {'Rate':>8} {'Amount':>10}")
    for fid, lit, fat, snf, rate, amt in sample_records:
        print(f"{fid:<6} {lit:8.2f} {fat:6.1f} {snf:6.1f} {rate:8.2f} {amt:10.2f}")
        
