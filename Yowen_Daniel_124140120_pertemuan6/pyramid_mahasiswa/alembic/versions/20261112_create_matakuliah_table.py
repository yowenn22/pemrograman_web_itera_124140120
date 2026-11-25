"""create matakuliah table

Revision ID: 202611120002
Revises: 202611120001
Create Date: 2026-11-12 10:05:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = "202611120002"
down_revision = "202611120001"
branch_labels = None
depends_on = None


def upgrade():
    """Membuat tabel matakuliah."""
    op.create_table(
        "matakuliah",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("kode_mk", sa.Text(), nullable=False),
        sa.Column("nama_mk", sa.Text(), nullable=False),
        sa.Column("sks", sa.Integer(), nullable=False),
        sa.Column("semester", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("kode_mk"),
    )


def downgrade():
    """Menghapus tabel matakuliah."""
    op.drop_table("matakuliah")
