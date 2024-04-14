import sqlalchemy as sa
from models.schemas.shared import Gender as GenderEnum


metadata = sa.MetaData()

EmployeesView = sa.Table(
    "employee_view",
    metadata,
    sa.Column("id", sa.Integer, nullable=False),
    sa.Column("employee_id", sa.String(20), nullable=False),
    sa.Column("title", sa.String(255), nullable=False),
    sa.Column("name", sa.String(255), nullable=False),
    sa.Column("gender", sa.Enum(GenderEnum), nullable=False),
    sa.Column("date_of_birth", sa.Date, nullable=False),
    sa.Column("nationality", sa.String(255), nullable=False),
    sa.Column("email_address", sa.String(255), nullable=False),
    sa.Column("phone_number", sa.String(15), nullable=False),
    sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    sa.Column("branch_id", sa.Integer, nullable=True),
    sa.Column("branch_name", sa.String(100), nullable=True),
    sa.Column("branch_address", sa.String(100), nullable=True),
    sa.Column("branch_created_at", sa.DateTime(timezone=True), nullable=True),
    sa.Column("branch_updated_at", sa.DateTime(timezone=True), nullable=True),
    sa.Column("department_id", sa.Integer, nullable=True),
    sa.Column("department_name", sa.String(100), nullable=True),
    sa.Column("department_description", sa.String(1900), nullable=True),
    sa.Column("department_created_at", sa.DateTime(timezone=True), nullable=True),
    sa.Column("department_updated_at", sa.DateTime(timezone=True), nullable=True),
    sa.Column("role_id", sa.Integer, nullable=False),
    sa.Column("role_name", sa.String(100), unique=True, nullable=False),
    sa.Column("role_description", sa.String(2000), nullable=True),
    sa.Column("role_created_at", sa.DateTime(timezone=True), nullable=False),
    sa.Column("role_updated_at", sa.DateTime(timezone=True), nullable=False),
)
