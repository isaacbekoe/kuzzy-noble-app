import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


metadata = sa.MetaData()

InstitutionsTable = sa.Table(
    "institution",
    metadata,
    sa.Column(
        "id",
        sa.Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
        nullable=False,
    ),
    sa.Column("name", sa.String(100), nullable=False),
    sa.Column("address", sa.String(100), nullable=True),
    sa.Column("phone_number", sa.String(20), nullable=True),
    sa.Column("email_address", sa.String(100), nullable=True),
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
    sa.UniqueConstraint("name", name="institutions_name_unique_constraint"),
)
