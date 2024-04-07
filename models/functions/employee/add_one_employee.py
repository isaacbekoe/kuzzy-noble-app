from models.database import db_conn_handle, db_connection_handler
from models.tables.employee import EmployeesTable
from models.schemas.employee import CreateEmployeeSchema, EmployeeSchema
from sqlalchemy.sql.expression import (
    Insert as InsertQuery
)
from datetime import datetime, timezone


@db_connection_handler
@db_conn_handle.transaction()
async def add_one_employee(
    data: CreateEmployeeSchema,
) -> EmployeeSchema:
    """Add one employee

    Args:
        data (CreateEmployeeSchema): The input data

    Returns:
        EmployeeSchema: The new employee record
    """
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the insert query
    query: InsertQuery = EmployeesTable.insert().values(
        **vars(data),
        created_at=now,
        updated_at=now
    )
    # execute the query
    last_record_id: int = await db_conn_handle.execute(query=query)
    # return the new record
    return EmployeeSchema(
        id=last_record_id,
        **vars(data),
        created_at=now,
        updated_at=now
    )
