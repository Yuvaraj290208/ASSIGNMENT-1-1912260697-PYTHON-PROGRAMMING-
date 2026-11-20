from decimal import Decimal, ROUND_HALF_UP

# Seasonal rate cards[span_228](start_span)[span_228](end_span)[span_229](start_span)[span_229](end_span)
SUMMER_MONTHS = {4, 5, 6}  # April to June[span_230](start_span)[span_230](end_span)[span_231](start_span)[span_231](end_span)

SEASONAL_RATES = {
    "summer": {
        "base_rate": Decimal("32.00"),[span_232](start_span)[span_232](end_span)[span_233](start_span)[span_233](end_span)
        "fat_step_value": Decimal("0.45"),[span_234](start_span)[span_234](end_span)[span_235](start_span)[span_235](end_span)
        "snf_step_value": Decimal("0.30"),[span_236](start_span)[span_236](end_span)[span_237](start_span)[span_237](end_span)
    },
    "regular": {
        "base_rate": Decimal("30.00"),[span_238](start_span)[span_238](end_span)[span_239](start_span)[span_239](end_span)
        "fat_step_value": Decimal("0.40"),[span_240](start_span)[span_240](end_span)[span_241](start_span)[span_241](end_span)
        "snf_step_value": Decimal("0.30"),[span_242](start_span)[span_242](end_span)[span_243](start_span)[span_243](end_span)
    },
}

BONUS_THRESHOLD_LITRES = Decimal("500")[span_244](start_span)[span_244](end_span)[span_245](start_span)[span_245](end_span)
BONUS_RATE_PER_LITRE = Decimal("0.50")[span_246](start_span)[span_246](end_span)[span_247](start_span)[span_247](end_span)

def get_rate_card(month: int) -> dict[str, Decimal]:[span_248](start_span)[span_248](end_span)[span_249](start_span)[span_249](end_span)
    """Selects seasonal rate card based on calendar month (4-6 = April-June).""[span_250](start_span)[span_251](start_span)"[span_250](end_span)[span_251](end_span)
    return SEASONAL_RATES["summer"] if month in SUMMER_MONTHS else SEASONAL_RATES["regular"][span_252](start_span)[span_252](end_span)[span_253](start_span)[span_253](end_span)

def rate_per_litre_v2(fat: Decimal, snf: Decimal, month: int) -> Decimal:
    """
    Computes rate per litre for 2-decimal automatic milk analyser readings (e.g., 4.25%, 8.63%).
    Uses exact proportional 0.1% steps (e.g., +0.75% fat = 7.5 steps) to preserve analyser precision.
    ""[span_254](start_span)[span_255](start_span)"[span_254](end_span)[span_255](end_span)
    if not (Decimal("2.00") <= fat <= Decimal("7.00")):
        raise ValueError(f"Fat {fat}% out of valid range [2.00, 7.00].")
    if not (Decimal("6.00") <= snf <= Decimal("11.00")):
        raise ValueError(f"SNF {snf}% out of valid range [6.00, 11.00].")

    card = get_rate_card(month)[span_256](start_span)[span_256](end_span)[span_257](start_span)[span_257](end_span)
    fat_steps = (fat - Decimal("3.50")) / Decimal("0.1")[span_258](start_span)[span_258](end_span)[span_259](start_span)[span_259](end_span)
    snf_steps = (snf - Decimal("8.50")) / Decimal("0.1")[span_260](start_span)[span_260](end_span)[span_261](start_span)[span_261](end_span)

    raw_rate = card["base_rate"] + (fat_steps * card["fat_step_value"]) + (snf_steps * card["snf_step_value"])[span_262](start_span)[span_262](end_span)[span_263](start_span)[span_263](end_span)
    return raw_rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def calculate_volume_bonus(total_litres: Decimal) -> Decimal:[span_264](start_span)[span_264](end_span)[span_265](start_span)[span_265](end_span)
    """
    Pays Rs 0.50/litre on ALL litres if total ten-day volume strictly exceeds 500 L.
    Exactly 500 L receives Rs 0.00 bonus.
    ""[span_266](start_span)[span_267](start_span)"[span_266](end_span)[span_267](end_span)
    if total_litres > BONUS_THRESHOLD_LITRES:[span_268](start_span)[span_268](end_span)[span_269](start_span)[span_269](end_span)
        return (total_litres * BONUS_RATE_PER_LITRE).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)[span_270](start_span)[span_270](end_span)[span_271](start_span)[span_271](end_span)
    return Decimal("0.00")[span_272](start_span)[span_272](end_span)[span_273](start_span)[span_273](end_span)

def farmer_ten_day_settlement(entries: list[tuple[Decimal, Decimal, Decimal]], month: int) -> dict[str, Decimal]:[span_274](start_span)[span_274](end_span)[span_275](start_span)[span_275](end_span)
    """Computes base payout, volume bonus, and grand total for a farmer's 10-day cycle.""[span_276](start_span)[span_277](start_span)"[span_276](end_span)[span_277](end_span)
    total_litres = Decimal("0.00")
    base_payout = Decimal("0.00")

    for litres, fat, snf in entries:
        if litres <= 0:
            raise ValueError("Litres must be positive.")
        rate = rate_per_litre_v2(fat, snf, month)
        entry_pay = (litres * rate).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        total_litres += litres
        base_payout += entry_pay

    bonus = calculate_volume_bonus(total_litres)
    return {
        "total_litres": total_litres,
        "base_payout": base_payout,
        "bonus": bonus,
        "final_payout": base_payout + bonus,
    }

if __name__ == "__main__":
    # Worked test cases for 2-decimal readings, both seasons, and bonus boundary (500L vs >500L)[span_278](start_span)[span_278](end_span)[span_279](start_span)[span_279](end_span)
    print("Regular (Oct) 4.25% fat, 8.63% SNF rate:", rate_per_litre_v2(Decimal("4.25"), Decimal("8.63"), month=10))[span_280](start_span)[span_280](end_span)[span_281](start_span)[span_281](end_span)
    print("Summer  (May) 4.25% fat, 8.63% SNF rate:", rate_per_litre_v2(Decimal("4.25"), Decimal("8.63"), month=5))[span_282](start_span)[span_282](end_span)[span_283](start_span)[span_283](end_span)

    # Boundary check: Exactly 500 L -> No bonus[span_284](start_span)[span_284](end_span)[span_285](start_span)[span_285](end_span)
    exact_500 = [(Decimal("250"), Decimal("3.50"), Decimal("8.50")), (Decimal("250"), Decimal("3.50"), Decimal("8.50"))]
    print("Exactly 500L (May):", farmer_ten_day_settlement(exact_500, month=5))[span_286](start_span)[span_286](end_span)[span_287](start_span)[span_287](end_span)

    # Above boundary: 500.5 L -> Rs 0.50 * 500.5 = Rs 250.25 bonus[span_288](start_span)[span_288](end_span)[span_289](start_span)[span_289](end_span)
    over_500 = [(Decimal("250"), Decimal("4.25"), Decimal("8.63")), (Decimal("250.5"), Decimal("4.25"), Decimal("8.63"))]
    print("500.5L (May)      :", farmer_ten_day_settlement(over_500, month=5))[span_290](start_span)[span_290](end_span)[span_291](start_span)[span_291](end_span)
