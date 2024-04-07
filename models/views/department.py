import sqlalchemy as sa


metadata = sa.MetaData()

DepartmentsView = sa.Table(
    "department_view",
    metadata,
    sa.Column(
        "id",
        sa.Integer,
        nullable=False),
    sa.Column("name", sa.String(255), nullable=False),
    sa.Column("description", sa.String(2000), nullable=True),
    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        nullable=False),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        nullable=False),
    sa.Column(
        "branch_id",
        sa.Integer,
        nullable=False),
    sa.Column("branch_name", sa.String(255), nullable=False),
    sa.Column("branch_address", sa.String(255), nullable=True),
    sa.Column(
        "branch_created_at",
        sa.DateTime(timezone=True),
        nullable=False),
    sa.Column(
        "branch_updated_at",
        sa.DateTime(timezone=True),
        nullable=False),
)
