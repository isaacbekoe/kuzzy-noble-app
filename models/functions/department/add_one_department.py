from models.database import db_conn_handle, db_connection_handler
from models.tables.department import DepartmentsTable
from models.schemas.department import CreateDepartmentSchema, DepartmentSchema
from sqlalchemy.sql.expression import (
    Insert as InsertQuery
)
from datetime import datetime, timezone


@db_connection_handler
@db_conn_handle.transaction()
async def add_one_department(
    data: CreateDepartmentSchema,
) -> DepartmentSchema:
    """Add one department

    Args:
        data (CreateDepartmentSchema): The input data

    Returns:
        DepartmentSchema: The new department record
    """
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the insert query
    query: InsertQuery = DepartmentsTable.insert().values(
        **vars(data),
        created_at=now,
        updated_at=now
    )
    # execute the query
    last_record_id: int = await db_conn_handle.execute(query=query)
    # return the new record
    return DepartmentSchema(
        id=last_record_id,
        **vars(data),
        created_at=now,
        updated_at=now
    )
