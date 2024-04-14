from models.database import db_conn_handle, db_connection_handler
from models.tables.doctor import DoctorsTable
from models.schemas.doctor import DoctorSchema
from sqlalchemy.sql.expression import (
    Delete as DeleteQuery
)
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def delete_one_doctor_by_id(
    doctor_id: int,
) -> DoctorSchema | None:
    """Delete one doctor by ID

    Args:
        doctor_id (int): The doctor ID

    Returns:
        DoctorSchema: The deleted doctor record if found else nothing
    """
    # create the delete query
    query: DeleteQuery = DoctorsTable.delete().where(
        DoctorsTable.c.id == doctor_id
    ).returning(DoctorsTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    if not record:
        return None
    # return the deleted record
    return DoctorSchema(**record._mapping)
