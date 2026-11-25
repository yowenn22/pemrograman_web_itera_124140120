"""create mahasiswa table

Revision ID: 202611120001
Revises:
Create Date: 2026-11-12 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = "202611120001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Membuat tabel mahasiswa."""
    op.create_table(
        "mahasiswa",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nim", sa.Text(), nullable=False),
        sa.Column("nama", sa.Text(), nullable=False),
        sa.Column("jurusan", sa.Text(), nullable=False),
        sa.Column("tanggal_lahir", sa.Date(), nullable=True),
        sa.Column("alamat", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("nim"),
    )


def downgrade():
    """Menghapus tabel mahasiswa."""
    op.drop_table("mahasiswa")
