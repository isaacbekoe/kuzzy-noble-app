from pydantic import BaseModel, Field, EmailStr, ConfigDict
from datetime import datetime, date


class DoctorBaseSchema(BaseModel):
    title: str = Field(
        ...,
        title="Title",
        description="The title of the doctor"
    )
    name: str = Field(
        ...,
        title="Name",
        description="The name of the doctor"
    )
    phone_number: str | None = Field(
        default=None,
        title="Phone Number",
        description="The doctor's phone number"
    )
    email_address: EmailStr | None = Field(
        default=None,
        title="Email Address",
        description="The doctor's email address"
    )
    institution_id: int | None = Field(
        default=None,
        title="Institution ID",
        description="The ID of the associated institution"
    )

    model_config = ConfigDict(
        populate_by_name=True
    )


class CreateDoctorSchema(DoctorBaseSchema):
    model_config = ConfigDict(
        populate_by_name=True
    )


class UpdateDoctorSchema(DoctorBaseSchema):
    model_config = ConfigDict(
        populate_by_name=True
    )


class SearchDoctorSchema(BaseModel):
    id: int | None = Field(
        default=None,
        title="Doctor ID",
        description="The ID of the doctor"
    )
    title: str | None = Field(
        default=None,
        title="Title",
        description="The title of the doctor"
    )
    name: str | None = Field(
        default=None,
        title="Name",
        description="The name of the doctor"
    )
    phone_number: str | None = Field(
        default=None,
        title="Phone Number",
        description="The doctor's phone number"
    )
    email_address: str | None = Field(
        default=None,
        title="Email Address",
        description="The doctor's email address"
    )
    created_at: date | None = Field(
        default=None,
        title="Created At",
        description="The date the doctor was created"
    )
    updated_at: date | None = Field(
        default=None,
        title="Updated At",
        description="The date the doctor was updated"
    )
    institution_id: int | None = Field(
        default=None,
        title="Institution ID",
        description="The ID of the institution"
    )
    institution_name: str | None = Field(
        default=None,
        title="Institution Name",
        description="The name of the institution",
    )
    institution_address: str | None = Field(
        default=None,
        title="Institution Address",
        description="The address of the institution"
    )
    institution_phone_number: str | None = Field(
        default=None,
        title="Phone Number",
        description="The institution's phone number"
    )
    institution_email_address: str | None = Field(
        default=None,
        title="Email Address",
        description="The institution's email address"
    )
    institution_created_at: date | None = Field(
        default=None,
        title="Institution Created At",
        description="The date the institution was created"
    )
    institution_updated_at: date | None = Field(
        default=None,
        title="Institution Updated At",
        description="The date the institution was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True
    )


class DoctorSchema(BaseModel):
    id: int = Field(
        ...,
        title="Doctor ID",
        description="The ID of the doctor"
    )
    title: str = Field(
        ...,
        title="Title",
        description="The title of the doctor"
    )
    name: str = Field(
        ...,
        title="Name",
        description="The name of the doctor"
    )
    phone_number: str | None = Field(
        default=None,
        title="Phone Number",
        description="The doctor's phone number"
    )
    email_address: EmailStr | None = Field(
        default=None,
        title="Email Address",
        description="The doctor's email address"
    )
    institution_id: int | None = Field(
        default=None,
        title="Institution ID",
        description="The ID of the associated institution"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the doctor was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the doctor was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True
    )


class DoctorViewSchema(BaseModel):
    id: int = Field(
        ...,
        title="Doctor ID",
        description="The ID of the doctor"
    )
    title: str = Field(
        ...,
        title="Title",
        description="The title of the doctor"
    )
    name: str = Field(
        ...,
        title="Name",
        description="The name of the doctor"
    )
    phone_number: str | None = Field(
        default=None,
        title="Phone Number",
        description="The doctor's phone number"
    )
    email_address: EmailStr | None = Field(
        default=None,
        title="Email Address",
        description="The doctor's email address"
    )
    created_at: datetime = Field(
        ...,
        title="Created At",
        description="The date and time the doctor was created"
    )
    updated_at: datetime = Field(
        ...,
        title="Updated At",
        description="The date and time the doctor was updated"
    )
    institution_id: int | None = Field(
        default=None,
        title="Institution ID",
        description="The ID of the institution"
    )
    institution_name: str | None = Field(
        default=None,
        title="Institution Name",
        description="The name of the institution",
    )
    institution_address: str | None = Field(
        default=None,
        title="Institution Address",
        description="The address of the institution"
    )
    institution_phone_number: str | None = Field(
        default=None,
        title="Institution Phone Number",
        description="The institution's phone number"
    )
    institution_email_address: EmailStr | None = Field(
        default=None,
        title="Institution Email Address",
        description="The institution's email address"
    )
    institution_created_at: datetime | None = Field(
        default=None,
        title="Institution Created At",
        description="The date and time the institution was created"
    )
    institution_updated_at: datetime | None = Field(
        default=None,
        title="Institution Updated At",
        description="The date and time the institution was updated"
    )

    model_config = ConfigDict(
        populate_by_name=True
    )
