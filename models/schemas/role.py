from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, timezone, date


class RoleBaseSchema(BaseModel):
    name: str = Field(
        ...,
        title="Role Name",
        description="The name of the role",
    )
    description: str | None = Field(
        default=None,
        title="Role Location",
        description="The location of the role"
    )


class CreateRoleSchema(RoleBaseSchema):
    pass


class UpdateRoleSchema(RoleBaseSchema):
    pass


class SearchRoleSchema(BaseModel):
    id: int | None = Field(
        default=None,
        title="Role ID",
        description="The ID of the role"
    )
    name: str | None = Field(
        default=None,
        title="Role Name",
        description="The name of the role",
    )
    description: str | None = Field(
        default=None,
        title="Role Description",
        description="The description of the role"
    )
    created_at: date | None = Field(
        default=None,
        title="Created At",
        description="The date the role was created"
    )
    updated_at: date | None = Field(
        default=None,
        title="Updated At",
        description="The date the role was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class RoleSchema(BaseModel):
    id: int = Field(
        ...,
        title="Role ID",
        description="The ID of the role"
    )
    name: str = Field(
        ...,
        title="Role Name",
        description="The name of the role",
    )
    description: str | None = Field(
        default=None,
        title="Role Description",
        description="The description of the role"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the role was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the role was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class RoleViewSchema(BaseModel):
    id: int = Field(
        ...,
        title="Role ID",
        description="The ID of the role"
    )
    name: str = Field(
        ...,
        title="Role Name",
        description="The name of the role",
    )
    description: str | None = Field(
        default=None,
        title="Role Description",
        description="The description of the role"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the role was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the role was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )
