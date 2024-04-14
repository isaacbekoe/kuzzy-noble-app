import sqlalchemy as sa


metadata = sa.MetaData()

DoctorsView = sa.Table(
    "doctor_view",
    metadata,
    sa.Column("id", sa.Integer, nullable=False),
    sa.Column("title", sa.String(10), nullable=False),
    sa.Column("name", sa.String(100), nullable=False),
    sa.Column("phone_number", sa.String(20), nullable=True),
    sa.Column("email_address", sa.String(100), nullable=True),
    sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    sa.Column("institution_id", sa.Integer, nullable=False),
    sa.Column("institution_name", sa.String(100), nullable=False),
    sa.Column("institution_address", sa.String(100), nullable=True),
    sa.Column("institution_phone_number", sa.String(20), nullable=True),
    sa.Column("institution_email_address", sa.String(100), nullable=True),
    sa.Column("institution_created_at", sa.DateTime(timezone=True), nullable=False),
    sa.Column("institution_updated_at", sa.DateTime(timezone=True), nullable=False),
)
