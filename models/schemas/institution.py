from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime, date


class InstitutionBaseSchema(BaseModel):
    name: str = Field(
        ...,
        title="Institution Name",
        description="The name of the institution"
    )
    address: str | None = Field(
        default=None,
        title="Institution Address",
        description="The address of the institution"
    )
    phone_number: str | None = Field(
        default=None,
        title="Phone Number",
        description="The institution's phone number"
    )
    email_address: EmailStr | None = Field(
        default=None,
        title="Email Address",
        description="The institution's email address"
    )

    model_config = ConfigDict(
        populate_by_name=True
    )


class CreateInstitutionSchema(InstitutionBaseSchema):
    model_config = ConfigDict(
        populate_by_name=True
    )


class UpdateInstitutionSchema(InstitutionBaseSchema):
    model_config = ConfigDict(
        populate_by_name=True
    )


class SearchInstitutionSchema(BaseModel):
    id: int | None = Field(
        default=None,
        title="Institution ID",
        description="The ID of the institution"
    )
    name: str | None = Field(
        default=None,
        title="Institution Name",
        description="The name of the institution",
    )
    address: str | None = Field(
        default=None,
        title="Institution Address",
        description="The address of the institution"
    )
    phone_number: str | None = Field(
        default=None,
        title="Phone Number",
        description="The institution's phone number"
    )
    email_address: str | None = Field(
        default=None,
        title="Email Address",
        description="The institution's email address"
    )
    created_at: date | None = Field(
        default=None,
        title="Created At",
        description="The date the institution was created"
    )
    updated_at: date | None = Field(
        default=None,
        title="Updated At",
        description="The date the institution was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True
    )


class InstitutionSchema(BaseModel):
    id: int = Field(
        ...,
        title="Institution ID",
        description="The ID of the institution"
    )
    name: str = Field(
        ...,
        title="Institution Name",
        description="The name of the institution",
    )
    address: str | None = Field(
        default=None,
        title="Institution Address",
        description="The address of the institution"
    )
    phone_number: str | None = Field(
        default=None,
        title="Phone Number",
        description="The institution's phone number"
    )
    email_address: EmailStr | None = Field(
        default=None,
        title="Email Address",
        description="The institution's email address"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the institution was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the institution was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True
    )


class InstitutionViewSchema(BaseModel):
    id: int = Field(
        ...,
        title="Institution ID",
        description="The ID of the institution"
    )
    name: str = Field(
        ...,
        title="Institution Name",
        description="The name of the institution",
    )
    address: str | None = Field(
        default=None,
        title="Institution Address",
        description="The address of the institution"
    )
    phone_number: str | None = Field(
        default=None,
        title="Phone Number",
        description="The institution's phone number"
    )
    email_address: EmailStr | None = Field(
        default=None,
        title="Email Address",
        description="The institution's email address"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the institution was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the institution was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True
    )
