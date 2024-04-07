import sqlalchemy as sa


metadata = sa.MetaData()

BranchesView = sa.Table(
    "branch_view",
    metadata,
    sa.Column(
        "id",
        sa.Integer,
        nullable=False),
    sa.Column("name", sa.String(255), nullable=False),
    sa.Column("address", sa.String(255), nullable=True),
    sa.Column(
        "created_at",
        sa.DateTime(timezone=True),
        nullable=False),
    sa.Column(
        "updated_at",
        sa.DateTime(timezone=True),
        nullable=False),
)
