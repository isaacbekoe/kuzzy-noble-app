from models.database import db_conn_handle, db_connection_handler
from models.views.doctor import DoctorsView
from models.schemas.doctor import DoctorViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record


@db_connection_handler
async def fetch_one_doctor_by_id(doctor_id: int) -> DoctorViewSchema | None:
    """Fetch one doctor by ID

    Args:
        doctor_id (int): The doctor ID

    Returns:
        DoctorViewSchema: The doctor if found else nothing
    """
    # prepare the query
    query: SelectQuery = DoctorsView.select().where(
        DoctorsView.c.id == doctor_id
    )
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if record is not found
    if not record:
        return None
    # return the record
    return DoctorViewSchema(**record._mapping)
