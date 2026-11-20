import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

# External JSON configuration so rate revisions require zero code edits[span_206](start_span)[span_206](end_span)
DEFAULT_CONFIG = {
    "base_rate": "30.00",[span_207](start_span)[span_207](end_span)[span_208](start_span)[span_208](end_span)
    "base_fat": "3.5",[span_209](start_span)[span_209](end_span)[span_210](start_span)[span_210](end_span)
    "base_snf": "8.5",[span_211](start_span)[span_211](end_span)[span_212](start_span)[span_212](end_span)
    "fat_step_size": "0.1",[span_213](start_span)[span_213](end_span)[span_214](start_span)[span_214](end_span)
    "snf_step_size": "0.1",[span_215](start_span)[span_215](end_span)[span_216](start_span)[span_216](end_span)
    "fat_step_value": "0.40",[span_217](start_span)[span_217](end_span)[span_218](start_span)[span_218](end_span)
    "snf_step_value": "0.30",[span_219](start_span)[span_219](end_span)[span_220](start_span)[span_220](end_span)
    "min_fat": "2.0",[span_221](start_span)[span_221](end_span)
    "max_fat": "7.0",[span_222](start_span)[span_222](end_span)
    "min_snf": "6.0",[span_223](start_span)[span_223](end_span)
    "max_snf": "11.0",[span_224](start_span)[span_224](end_span)
}

def load_rate_card(filepath: str = "rate_card.json") -> dict[str, Decimal]:[span_225](start_span)[span_225](end_span)
    path = Path(filepath)
    if not path.exists():
        path.write_text(json.dumps(DEFAULT_CONFIG, indent=2))
    raw = json.loads(path.read_text())
    return {k: Decimal(v) for k, v in raw.items()}

class CooperativeCalculator:
    """Production-ready calculator using Decimal arithmetic and externalized rate cards."""
    def __init__(self, card: dict[str, Decimal]):
        self.card = card

    def rate_per_litre(self, fat: Decimal, snf: Decimal) -> Decimal:
        if not (self.card["min_fat"] <= fat <= self.card["max_fat"]):
            raise ValueError(f"Fat {fat}% out of allowed range.")
        if not (self.card["min_snf"] <= snf <= self.card["max_snf"]):
            raise ValueError(f"SNF {snf}% out of allowed range.")

        fat_steps = ((fat - self.card["base_fat"]) / self.card["fat_step_size"]).to_integral_value(rounding=ROUND_HALF_UP)
        snf_steps = ((snf - self.card["base_snf"]) / self.card["snf_step_size"]).to_integral_value(rounding=ROUND_HALF_UP)

        rate = (
            self.card["base_rate"]
            + fat_steps * self.card["fat_step_value"]
            + snf_steps * self.card["snf_step_value"]
        )
        return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    def payout(self, litres: Decimal, fat: Decimal, snf: Decimal) -> Decimal:
        if litres <= 0:
            raise ValueError("Litres must be positive.")
        return (litres * self.rate_per_litre(fat, snf)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    calc = CooperativeCalculator(load_rate_card())
    print("District-scale ready payout (10L, 3.5%, 8.5%):", calc.payout(Decimal("10"), Decimal("3.5"), Decimal("8.5")))
