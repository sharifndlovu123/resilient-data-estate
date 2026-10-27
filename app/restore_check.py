"""After a restore, compare what came back with what was expected."""
import hashlib


def checksum(rows: list) -> str:
    return hashlib.sha256("\n".join(sorted(map(str, rows))).encode()).hexdigest()


def check(expected: list, restored: list) -> dict:
    return {
        "rows_match": len(expected) == len(restored),
        "checksum_match": checksum(expected) == checksum(restored),
    }
