import sqlalchemy as sa
from sqlalchemy.sql import func


metadata = sa.MetaData()

DepartmentsTable = sa.Table(
    "department",
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
    sa.Column("description", sa.String(2000), nullable=True),
    sa.Column("branch_id", sa.Integer, sa.ForeignKey("branch.id"), nullable=False),
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
    sa.UniqueConstraint(
        "name", "branch_id", name="department_name_branch_id_unique_constraint"
    ),
)
