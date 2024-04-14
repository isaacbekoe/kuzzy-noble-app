from models.database import db_conn_handle, db_connection_handler
from models.tables.employee import EmployeesTable
from models.schemas.employee import UpdateEmployeeSchema, EmployeeSchema
from sqlalchemy.sql.expression import (
    Update as UpdateQuery
)
from datetime import datetime, timezone
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def update_one_employee_by_id(
    employee_record_id: int,
    data: UpdateEmployeeSchema,
) -> EmployeeSchema | None:
    """Update one employee by ID

    Args:
        employee_record_id (int): The employee record ID
        data (UpdateEmployeeSchema): The input data

    Returns:
        EmployeeSchema: The updated employee record if found else nothing
    """
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the update query
    query: UpdateQuery = EmployeesTable.update().where(
        EmployeesTable.c.id == employee_record_id
    ).values(
        **vars(data),
        updated_at=now
    ).returning(EmployeesTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if the record was not found
    if not record:
        return None
    # return the updated record
    return EmployeeSchema(**record._mapping)
