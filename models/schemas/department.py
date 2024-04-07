from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, timezone, date


class DepartmentBaseSchema(BaseModel):
    name: str = Field(
        ...,
        title="Department Name",
        description="The name of the department",
    )
    description: str | None = Field(
        default=None,
        title="Department Location",
        description="The location of the department"
    )
    branch_id: int = Field(
        ...,
        title="Branch ID",
        description="The ID of the associated branch"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class CreateDepartmentSchema(DepartmentBaseSchema):
    model_config = ConfigDict(
        populate_by_name=True,
    )


class UpdateDepartmentSchema(DepartmentBaseSchema):
    model_config = ConfigDict(
        populate_by_name=True,
    )


class SearchDepartmentSchema(BaseModel):
    id: int | None = Field(
        default=None,
        title="Department ID",
        description="The ID of the department"
    )
    name: str | None = Field(
        default=None,
        title="Department Name",
        description="The name of the department",
    )
    description: str | None = Field(
        default=None,
        title="Department Description",
        description="The description of the department"
    )
    created_at: date | None = Field(
        default=None,
        title="Created At",
        description="The date the department was created"
    )
    updated_at: date | None = Field(
        default=None,
        title="Updated At",
        description="The date the department was updated"
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

    model_config = ConfigDict(
        populate_by_name=True,
    )


class DepartmentSchema(BaseModel):
    id: int = Field(
        ...,
        title="Department ID",
        description="The ID of the department"
    )
    name: str = Field(
        ...,
        title="Department Name",
        description="The name of the department",
    )
    description: str | None = Field(
        default=None,
        title="Department Description",
        description="The description of the department"
    )
    branch_id: int = Field(
        ...,
        title="Branch ID",
        description="The ID of the associated branch"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the department was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the department was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class DepartmentViewSchema(BaseModel):
    id: int = Field(
        ...,
        title="Department ID",
        description="The ID of the department"
    )
    name: str = Field(
        ...,
        title="Department Name",
        description="The name of the department",
    )
    description: str | None = Field(
        default=None,
        title="Department Description",
        description="The description of the department"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the department was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the department was updated"
    )
    branch_id: int = Field(
        ...,
        title="Branch ID",
        description="The ID of the associated branch"
    )
    branch_name: str = Field(
        ...,
        title="Branch Name",
        description="The name of the branch",
    )
    branch_address: str | None = Field(
        default=None,
        title="Branch Address",
        description="The address of the branch"
    )
    branch_created_at: datetime = Field(
        ...,
        title="Branch Created At",
        description="The date and time the branch was created"
    )
    branch_updated_at: datetime = Field(
        ...,
        title="Branch Updated At",
        description="The date and time the branch was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )
