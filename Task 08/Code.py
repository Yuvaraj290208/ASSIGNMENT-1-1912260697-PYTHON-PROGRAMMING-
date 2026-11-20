ALGORITHM TenDayFarmerPayment
START
    SET total TO 0.0
    SET valid_count TO 0
    INPUT entries
    FOR each entry IN entries
        EXTRACT litres, fat, snf FROM entry
        IF litres > 0 AND fat >= 2.0 AND fat <= 7.0 AND snf >= 6.0 AND snf <= 11.0 THEN
            SET fat_steps TO ROUND((fat - 3.5) / 0.1)
            SET snf_steps TO ROUND((snf - 8.5) / 0.1)
            SET rate TO ROUND(30.00 + (fat_steps * 0.40) + (snf_steps * 0.30), 2)
            SET amount TO ROUND(litres * rate, 2)
            SET total TO ROUND(total + amount, 2)
            SET valid_count TO valid_count + 1
            OUTPUT amount
        ELSE
            OUTPUT "Invalid entry"
        ENDIF
    ENDFOR
    OUTPUT total
END
