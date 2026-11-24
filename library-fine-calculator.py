from datetime import date

FINE_PER_DAY = 2  # rupees per late day


def days_late(due, ret):
    return max((ret - due).days, 0)


def is_overdue(due, ret):
    return ret > due


def fine(days):
    if days < 0:
        raise ValueError("days cannot be negative")
    return days * FINE_PER_DAY


def main():
    due = date(2026, 11, 10)
    ret = date(2026, 11, 15)
    late = days_late(due, ret)
    if is_overdue(due, ret):
        print(f"Overdue by {late} day(s). Fine = Rs. {fine(late)}")
    else:
        print("Returned on time. No fine.")


if __name__ == "__main__":
    main()