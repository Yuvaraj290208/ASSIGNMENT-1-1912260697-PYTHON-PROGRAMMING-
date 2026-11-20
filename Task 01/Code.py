# Demonstration of data representation and validation rules for Task 1

# Named Constants
BASE_RATE = 30.00
BASE_FAT = 3.5
BASE_SNF = 8.5
FAT_STEP = 0.1
SNF_STEP = 0.1
FAT_STEP_RATE = 0.40
SNF_STEP_RATE = 0.30

MIN_FAT, MAX_FAT = 2.0, 7.0
MIN_SNF, MAX_SNF = 6.0, 11.0
VALID_SHIFTS = ("AM", "PM")

def validate_entry(farmer_id: str, litres: float, fat: float, snf: float, shift: str) -> bool:
    """Validates a single milk collection entry against domain rules."""
    if not farmer_id or not isinstance(farmer_id, str):
        return False
    if litres <= 0:
        return False
    if not (MIN_FAT <= fat <= MAX_FAT):
        return False
    if not (MIN_SNF <= snf <= MAX_SNF):
        return False
    if shift.upper() not in VALID_SHIFTS:
        return False
    return True

# Scalable tuple-per-entry structure instead of separate scalar variables
entries = [
    ("F001", 10.0, 3.5, 8.5, "AM"),
    ("F002", 8.5, 4.2, 8.7, "PM"),
    ("F003", -5.0, 3.5, 8.5, "AM"),  # Invalid entry
]

for entry in entries:
    print(f"Entry {entry} valid? -> {validate_entry(*entry)}")
  
