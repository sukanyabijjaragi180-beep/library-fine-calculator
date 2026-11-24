from datetime import date
import pytest
from library_fine import days_late, is_overdue, fine, capped_fine


def test_days_late_on_time():
    assert days_late(date(2026, 11, 10), date(2026, 11, 8)) == 0


def test_days_late_three_days():
    assert days_late(date(2026, 11, 10), date(2026, 11, 13)) == 3


def test_is_overdue_true():
    assert is_overdue(date(2026, 11, 10), date(2026, 11, 12)) is True


def test_is_overdue_false_same_day():
    assert is_overdue(date(2026, 11, 10), date(2026, 11, 10)) is False


def test_fine_five_days():
    assert fine(5) == 10


def test_fine_zero_days():
    assert fine(0) == 0


def test_fine_negative_raises():
    with pytest.raises(ValueError):
        fine(-1)


def test_capped_fine_limit():
    assert capped_fine(1000) == 500