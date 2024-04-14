import sqlalchemy as sa
from sqlalchemy.sql import func


metadata = sa.MetaData()

DoctorsTable = sa.Table(
    "doctor",
    metadata,
    sa.Column(
        "id",
        sa.Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
        nullable=False,
    ),
    sa.Column("title", sa.String(10), nullable=False),
    sa.Column("name", sa.String(100), nullable=False),
    sa.Column("phone_number", sa.String(20), nullable=True),
    sa.Column("email_address", sa.String(100), nullable=True),
    sa.Column(
        "institution_id", sa.Integer, sa.ForeignKey("institution.id"), nullable=True
    ),
    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    ),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        server_default=func.now(),
        server_onupdate=sa.text("NOW()"),
        nullable=False,
    ),
)
