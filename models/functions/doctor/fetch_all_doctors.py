from models.database import db_conn_handle, db_connection_handler
from models.views.doctor import DoctorsView
from models.schemas.doctor import DoctorViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record
from sqlalchemy import func


@db_connection_handler
async def fetch_all_doctors(skip: int, limit: int) -> tuple[list[DoctorViewSchema], int]:
    """Fetch all doctors

    Args:
        skip (int): The number of records to skip
        limit (int): The number of records to select

    Returns:
        tuple[list[DoctorViewSchema], int]: A list of doctors and the total number of matching records
    """
    # get the total number of records
    query: SelectQuery = DoctorsView.select().where().with_only_columns(*[func.count()])
    records_count: int = await db_conn_handle.execute(query=query)
    # create the select query
    query: SelectQuery = DoctorsView.select().where().order_by(DoctorsView.c.name).limit(limit).offset(skip)
    # execute the query, select the doctors without loading then all into
    # memory at once
    selected_doctors = []
    row: Record
    async for row in db_conn_handle.iterate(query=query):
        selected_doctors.append(DoctorViewSchema(**row._mapping))
    # return the selected doctors
    return selected_doctors, records_count
