from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime, timezone, date


class EmployeeBaseSchema(BaseModel):
    employee_id: str = Field(
        ...,
        title="Employee ID",
        description="The ID of the employee"
    )
    title: str = Field(
        ...,
        title="Employee Title",
        description="The title of the employee. Eg. Mr., Mrs., etc"
    )
    name: str = Field(
        ...,
        title="Name",
        description="The name of the employee"
    )
    gender: str = Field(
        ...,
        title="Gender",
        description="The employee's gender"
    )
    date_of_birth: date = Field(
        ...,
        title="Date of Birth",
        description="The employee's date of birth"
    )
    nationality: str = Field(
        ...,
        title="Nationality",
        description="The employee's nationality"
    )
    email_address: EmailStr = Field(
        ...,
        title="Email Address",
        description="The employee's email address"
    )
    phone_number: str = Field(
        ...,
        title="Phone Number",
        description="The employee's phone number"
    )
    department_id: int | None = Field(
        default=None,
        title="Department ID",
        description="The ID of the department the employee belongs to"
    )
    branch_id: int | None = Field(
        default=None,
        title="Branch ID",
        description="The ID of the branch the employee belongs to"
    )
    role_id: int = Field(
        ...,
        title="Role ID",
        description="The ID of the employee's role"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class CreateEmployeeSchema(EmployeeBaseSchema):
    model_config = ConfigDict(
        populate_by_name=True,
    )


class UpdateEmployeeSchema(EmployeeBaseSchema):
    model_config = ConfigDict(
        populate_by_name=True,
    )


class SearchEmployeeSchema(BaseModel):
    id: int | None = Field(
        default=None,
        title="Employee ID",
        description="The ID of the employee"
    )
    employee_id: str | None = Field(
        default=None,
        title="Employee ID",
        description="The ID of the employee"
    )
    title: str | None = Field(
        default=None,
        title="Employee Title",
        description="The title of the employee. Eg. Mr., Mrs., etc",
    )
    name: str | None = Field(
        default=None,
        title="Employee Name",
        description="The name of the employee",
    )
    gender: str | None = Field(
        default=None,
        title="Gender",
        description="The employee's gender"
    )
    date_of_birth: date | None = Field(
        default=None,
        title="Date of Birth",
        description="The employee's date of birth"
    )
    nationality: str | None = Field(
        default=None,
        title="Nationality",
        description="The employee's nationality"
    )
    email_address: str | None = Field(
        default=None,
        title="Email Address",
        description="The employee's email address"
    )
    phone_number: str | None = Field(
        default=None,
        title="Phone Number",
        description="The employee's phone number"
    )
    created_at: date | None = Field(
        default=None,
        title="Created At",
        description="The date the employee was created"
    )
    updated_at: date | None = Field(
        default=None,
        title="Updated At",
        description="The date the employee was updated"
    )
    branch_id: int | None = Field(
        default=None,
        title="Branch ID",
        description="The ID of the branch the employee belongs to"
    )
    branch_name: str | None = Field(
        default=None,
        title="Branch Name",
        description="The name of the branch",
    )
    branch_address: str | None = Field(
        default=None,
        title="Branch Address",
        description="The address of the branch"
    )
    branch_created_at: date | None = Field(
        default=None,
        title="Branch Created At",
        description="The date the branch was created"
    )
    branch_updated_at: date | None = Field(
        default=None,
        title="Branch Updated At",
        description="The date the branch was updated"
    )
    department_id: int | None = Field(
        default=None,
        title="Department ID",
        description="The ID of the department the employee belongs to"
    )
    department_name: str | None = Field(
        default=None,
        title="Department Name",
        description="The name of the department",
    )
    department_description: str | None = Field(
        default=None,
        title="Department Description",
        description="The description of the department"
    )
    department_created_at: date | None = Field(
        default=None,
        title="Department Created At",
        description="The date the department was created"
    )
    department_updated_at: date | None = Field(
        default=None,
        title="Department Updated At",
        description="The date the department was updated"
    )
    role_id: int | None = Field(
        default=None,
        title="Role ID",
        description="The ID of the employee's role"
    )
    role_name: str | None = Field(
        default=None,
        title="Role Name",
        description="The name of the role",
    )
    role_description: str | None = Field(
        default=None,
        title="Role Description",
        description="The description of the role"
    )
    role_created_at: date | None = Field(
        default=None,
        title="Role Created At",
        description="The date the role was created"
    )
    role_updated_at: date | None = Field(
        default=None,
        title="Role Updated At",
        description="The date the role was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class EmployeeSchema(BaseModel):
    id: int = Field(
        ...,
        title="Employee ID",
        description="The ID of the employee"
    )
    employee_id: str = Field(
        ...,
        title="Employee ID",
        description="The ID of the employee"
    )
    title: str = Field(
        ...,
        title="Employee Title",
        description="The title of the employee. Eg. Mr., Mrs., etc",
    )
    name: str = Field(
        ...,
        title="Employee Name",
        description="The name of the employee",
    )
    gender: str = Field(
        ...,
        title="Gender",
        description="The employee's gender"
    )
    date_of_birth: date = Field(
        ...,
        title="Date of Birth",
        description="The employee's date of birth"
    )
    nationality: str = Field(
        ...,
        title="Nationality",
        description="The employee's nationality"
    )
    email_address: EmailStr = Field(
        ...,
        title="Email Address",
        description="The employee's email address"
    )
    phone_number: str = Field(
        ...,
        title="Phone Number",
        description="The employee's phone number"
    )
    department_id: int | None = Field(
        default=None,
        title="Department ID",
        description="The ID of the department the employee belongs to"
    )
    branch_id: int | None = Field(
        default=None,
        title="Branch ID",
        description="The ID of the branch the employee belongs to"
    )
    role_id: int = Field(
        ...,
        title="Role ID",
        description="The ID of the employee's role"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the employee was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the employee was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class EmployeeViewSchema(BaseModel):
    id: int = Field(
        ...,
        title="Employee ID",
        description="The ID of the employee"
    )
    employee_id: str = Field(
        ...,
        title="Employee ID",
        description="The ID of the employee"
    )
    title: str = Field(
        ...,
        title="Employee Title",
        description="The title of the employee. Eg. Mr., Mrs., etc",
    )
    name: str = Field(
        ...,
        title="Employee Name",
        description="The name of the employee",
    )
    gender: str = Field(
        ...,
        title="Gender",
        description="The employee's gender"
    )
    date_of_birth: date = Field(
        ...,
        title="Date of Birth",
        description="The employee's date of birth"
    )
    nationality: str = Field(
        ...,
        title="Nationality",
        description="The employee's nationality"
    )
    email_address: EmailStr = Field(
        ...,
        title="Email Address",
        description="The employee's email address"
    )
    phone_number: str = Field(
        ...,
        title="Phone Number",
        description="The employee's phone number"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the employee was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the employee was updated"
    )
    branch_id: int | None = Field(
        default=None,
        title="Branch ID",
        description="The ID of the associated branch"
    )
    branch_name: str | None = Field(
        default=None,
        title="Branch Name",
        description="The name of the branch",
    )
    branch_address: str | None = Field(
        default=None,
        title="Branch Address",
        description="The address of the branch"
    )
    branch_created_at: datetime | None = Field(
        default=None,
        title="Branch Created At",
        description="The date and time the branch was created"
    )
    branch_updated_at: datetime | None = Field(
        default=None,
        title="Branch Updated At",
        description="The date and time the branch was updated"
    )
    department_id: int | None = Field(
        default=None,
        title="Department ID",
        description="The ID of the department the employee belongs to"
    )
    department_name: str | None = Field(
        default=None,
        title="Department Name",
        description="The name of the department",
    )
    department_description: str | None = Field(
        default=None,
        title="Department Description",
        description="The description of the department"
    )
    department_created_at: datetime | None = Field(
        default=None,
        title="Department Created At",
        description="The date and time the department was created"
    )
    department_updated_at: datetime | None = Field(
        default=None,
        title="Department Updated At",
        description="The date and time the department was updated"
    )
    role_id: int = Field(
        ...,
        title="Role ID",
        description="The ID of the employee's role"
    )
    role_name: str = Field(
        ...,
        title="Role Name",
        description="The name of the role",
    )
    role_description: str | None = Field(
        default=None,
        title="Role Description",
        description="The description of the role"
    )
    role_created_at: datetime = Field(
        ...,
        title="Role Created At",
        description="The date and time the role was created"
    )
    role_updated_at: datetime = Field(
        ...,
        title="Role Updated At",
        description="The date and time the role was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )
