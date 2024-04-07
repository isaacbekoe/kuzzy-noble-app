from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, timezone, date


class BranchBaseSchema(BaseModel):
    name: str = Field(
        ...,
        title="Branch Name",
        description="The name of the branch",
    )
    address: str | None = Field(
        default=None,
        title="Branch Address",
        description="The address of the branch"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class CreateBranchSchema(BranchBaseSchema):
    model_config = ConfigDict(
        populate_by_name=True,
    )


class UpdateBranchSchema(BranchBaseSchema):
    model_config = ConfigDict(
        populate_by_name=True,
    )


class SearchBranchSchema(BaseModel):
    id: int | None = Field(
        default=None,
        title="Branch ID",
        description="The ID of the branch"
    )
    name: str | None = Field(
        default=None,
        title="Branch Name",
        description="The name of the branch",
    )
    address: str | None = Field(
        default=None,
        title="Branch Address",
        description="The address of the branch"
    )
    created_at: date | None = Field(
        default=None,
        title="Created At",
        description="The date the branch was created"
    )
    updated_at: date | None = Field(
        default=None,
        title="Updated At",
        description="The date the branch was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class BranchSchema(BaseModel):
    id: int = Field(
        ...,
        title="Branch ID",
        description="The ID of the branch"
    )
    name: str = Field(
        ...,
        title="Branch Name",
        description="The name of the branch",
    )
    address: str | None = Field(
        default=None,
        title="Branch Address",
        description="The address of the branch"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the branch was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the branch was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )


class BranchViewSchema(BaseModel):
    id: int = Field(
        ...,
        title="Branch ID",
        description="The ID of the branch"
    )
    name: str = Field(
        ...,
        title="Branch Name",
        description="The name of the branch",
    )
    address: str | None = Field(
        default=None,
        title="Branch Address",
        description="The address of the branch"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the branch was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the branch was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True,
    )
