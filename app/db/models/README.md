# To add new models

Precheck: Ensure alembic is installed, initiated, and `alembic/env.py` is configured

1. Create a new `table.py` and define the table there
2. Import that model into this directory's `__init__.py`
3. `cd` into where `alembic.ini` exists and run `alembic revision --autogenerate -m "create <YOUR_TABLE_NAME> table"`
4. Run `alembic upgrade head`
