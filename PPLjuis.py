# ==========================================
# KUIS PENGUJIAN PERANGKAT LUNAK
# Sistem Peminjaman Ruang Diskusi
# ==========================================

# Nama : Nabiel Tatra Edy Firdaus
# NIM  : 235150207111059

print("===================================")
print("KUIS PENGUJIAN PERANGKAT LUNAK")
print("Nama : Nabiel Tatra Edy Firdaus (235150207111059)")


# ======================================================
# 1. EP & BVA TESTING
# ======================================================

print("\nEP & BVA TESTING")

# Fungsi validasi durasi
def validate_duration(duration):
    return 1 <= duration <= 4

# Data test EP & BVA
duration_tests = [0, 1, 2, 3, 4, 5]

for duration in duration_tests:
    result = validate_duration(duration)
    print(f"Duration {duration} jam => {result}")


# ======================================================
# 2. DECISION TABLE TESTING
# ======================================================

print("\nDECISION TABLE TESTING")

# Fungsi booking
def booking(registered, no_violation, room_available):

    # semua syarat harus TRUE
    if registered and no_violation and room_available:
        return "BOOKING BERHASIL"

    return "DITOLAK"

# Test case decision table
decision_tests = [
    (True, True, True),
    (False, True, True),
    (True, False, True),
    (True, True, False)
]

for test in decision_tests:
    result = booking(*test)
    print(f"{test} => {result}")


# ======================================================
# 3. STATE TRANSITION TESTING
# ======================================================

print("\nSTATE TRANSITION TESTING")

# Daftar transisi valid
transitions = {
    ("AVAILABLE", "book"): "BOOKED",
    ("BOOKED", "start"): "IN_USE",
    ("IN_USE", "finish"): "FINISHED",
    ("BOOKED", "cancel"): "AVAILABLE"
}

# Fungsi transition
def transition(current_state, event):

    # cek transisi valid
    if (current_state, event) in transitions:
        return transitions[(current_state, event)]

    # jika tidak valid
    return "INVALID TRANSITION"

# Valid transition
valid_tests = [
    ("AVAILABLE", "book"),
    ("BOOKED", "start"),
    ("IN_USE", "finish"),
    ("BOOKED", "cancel")
]

print("\nValid Transition:")

for state, event in valid_tests:
    result = transition(state, event)
    print(f"{state} + {event}() => {result}")

# Invalid transition
invalid_tests = [
    ("AVAILABLE", "finish"),
    ("AVAILABLE", "start"),
    ("IN_USE", "book"),
    ("FINISHED", "start")
]

print("\nInvalid Transition:")

for state, event in invalid_tests:
    result = transition(state, event)
    print(f"{state} + {event}() => {result}")