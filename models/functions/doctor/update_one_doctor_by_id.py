from models.database import db_conn_handle, db_connection_handler
from models.tables.doctor import DoctorsTable
from models.schemas.doctor import UpdateDoctorSchema, DoctorSchema
from sqlalchemy.sql.expression import (
    Update as UpdateQuery
)
from datetime import datetime, timezone
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def update_one_doctor_by_id(
    doctor_id: int,
    data: UpdateDoctorSchema,
) -> DoctorSchema | None:
    """Update one doctor by ID

    Args:
        doctor_id (int): The doctor ID
        data (UpdateDoctorSchema): The input data

    Returns:
        DoctorSchema: The updated doctor record if found else nothing
    """
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the update query
    query: UpdateQuery = DoctorsTable.update().where(
        DoctorsTable.c.id == doctor_id
    ).values(
        **vars(data),
        updated_at=now
    ).returning(DoctorsTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if the record was not found
    if not record:
        return None
    # return the updated record
    return DoctorSchema(**record._mapping)
