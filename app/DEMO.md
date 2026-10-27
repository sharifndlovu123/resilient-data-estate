# Demo: restore integrity check

**Framework:** none, plain Python. **Moving parts locally:** none.

`check(expected, restored)` compares row count and a checksum. The weekly restore test runs it after restoring a backup into a throwaway environment.

## Run it

```bash
cd app
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
```

```bash
pytest                    # 3 tests
python -c "from restore_check import check; print(check([(1,'a')], [(1,'x')]))"
# {'rows_match': True, 'checksum_match': False}
```

## What is missing locally (added in the cloud work)

- The Step Functions workflow and the Fargate Spot job that does the restore.
- Reading real rows from the restored database.
- Writing the measured recovery time to a dashboard.

Rows are sorted before hashing, so order does not matter, only content.
