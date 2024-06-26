import sqlalchemy as sa
from sqlalchemy.sql import func


metadata = sa.MetaData()

BranchesTable = sa.Table(
    "branch",
    metadata,
    sa.Column(
        "id",
        sa.Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
        nullable=False,
    ),
    sa.Column("name", sa.String(255), nullable=False),
    sa.Column("address", sa.String(255), nullable=True),
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
    sa.UniqueConstraint("name", name="branch_name_unique_constraint"),
)
