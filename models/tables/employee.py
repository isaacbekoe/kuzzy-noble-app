import sqlalchemy as sa
from sqlalchemy.sql import func
from models.schemas.shared import Gender as GenderEnum


metadata = sa.MetaData()

EmployeesTable = sa.Table(
    "employee",
    metadata,
    sa.Column(
        "id",
        sa.Integer,
        primary_key=True,
        autoincrement=True,
        index=True,
        nullable=False,
    ),
    sa.Column("employee_id", sa.String(20), index=True, nullable=False),
    sa.Column("title", sa.String(255), nullable=False),
    sa.Column("name", sa.String(255), nullable=False),
    sa.Column("gender", sa.Enum(GenderEnum), nullable=False),
    sa.Column("date_of_birth", sa.Date, nullable=False),
    sa.Column("nationality", sa.String(255), nullable=False),
    sa.Column(
        "department_id", sa.Integer, sa.ForeignKey("department.id"), nullable=True
    ),
    sa.Column("branch_id", sa.Integer, sa.ForeignKey("branche.id"), nullable=True),
    sa.Column("role_id", sa.Integer, sa.ForeignKey("role.id"), nullable=False),
    sa.Column("email_address", sa.String(255), nullable=False),
    sa.Column("phone_number", sa.String(15), nullable=False),
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
    sa.UniqueConstraint("employee_id", name="employees_employee_id_unique_constraint"),
    sa.UniqueConstraint(
        "email_address", name="employees_email_address_unique_constraint"
    ),
    sa.UniqueConstraint(
        "phone_number", name="employees_phone_number_unique_constraint"
    ),
)
