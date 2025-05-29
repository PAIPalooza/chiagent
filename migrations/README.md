# Database Migrations

This directory contains database migrations for the ChiAgent application.

## Applying Migrations

1. Make sure you have the required dependencies installed:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application, which will automatically apply any pending migrations:
   ```bash
   uvicorn app.main:app --reload
   ```

## Creating New Migrations

1. Create a new migration file in the `versions` directory with the following naming convention:
   `YYYYMMDDHHMMSS_short_description.py`

2. Use the following template for new migrations:
   ```python
   """Short description of the migration

   Revision ID: YYYYMMDDHHMMSS
   Revises: 
   Create Date: YYYY-MM-DD HH:MM:SS.000000

   """
   from alembic import op
   import sqlalchemy as sa
   from sqlalchemy.dialects import postgresql

   # revision identifiers, used by Alembic.
   revision = 'YYYYMMDDHHMMSS'
   down_revision = None
   branch_labels = None
   depends_on = None

   def upgrade():
       # Migration code here
       pass

   def downgrade():
       # Rollback code here
       pass
   ```

## Migration Naming Convention

- Use lowercase with underscores for file names
- Prefix with timestamp (YYYYMMDDHHMMSS)
- Use descriptive names for the migration
- Example: `20250529212141_add_address_updates_table.py`
