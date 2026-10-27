from restore_check import check


def test_identical_data_passes():
    assert check([(1, "a"), (2, "b")], [(2, "b"), (1, "a")]) == {"rows_match": True, "checksum_match": True}


def test_missing_row_fails_both():
    assert check([(1, "a"), (2, "b")], [(1, "a")]) == {"rows_match": False, "checksum_match": False}


def test_changed_value_fails_checksum_only():
    assert check([(1, "a")], [(1, "x")]) == {"rows_match": True, "checksum_match": False}
