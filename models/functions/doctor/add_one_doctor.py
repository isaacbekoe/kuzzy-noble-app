from models.database import db_conn_handle, db_connection_handler
from models.tables.doctor import DoctorsTable
from models.schemas.doctor import CreateDoctorSchema, DoctorSchema
from sqlalchemy.sql.expression import (
    Insert as InsertQuery
)
from datetime import datetime, timezone


@db_connection_handler
@db_conn_handle.transaction()
async def add_one_doctor(data: CreateDoctorSchema) -> DoctorSchema:
    """Add one doctor

    Args:
        data (CreateDoctorSchema): The input data

    Returns:
        DoctorSchema: The new doctor record
    """
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the insert query
    query: InsertQuery = DoctorsTable.insert().values(
        **vars(data),
        created_at=now,
        updated_at=now
    )
    # execute the query
    last_record_id: int = await db_conn_handle.execute(query=query)
    # return the new record
    return DoctorSchema(
        id=last_record_id,
        **vars(data),
        created_at=now,
        updated_at=now
    )
