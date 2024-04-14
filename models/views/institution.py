import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


metadata = sa.MetaData()

InstitutionsView = sa.Table(
    "institution_view",
    metadata,
    sa.Column("id", sa.Integer, nullable=False),
    sa.Column("name", sa.String(100), nullable=False),
    sa.Column("address", sa.String(100), nullable=True),
    sa.Column("phone_number", sa.String(20), nullable=True),
    sa.Column("email_address", sa.String(100), nullable=True),
    sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
)
