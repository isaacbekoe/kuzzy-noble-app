from models.database import db_conn_handle, db_connection_handler
from models.tables.employee import EmployeesTable
from models.schemas.employee import EmployeeSchema
from sqlalchemy.sql.expression import (
    Delete as DeleteQuery
)
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def delete_one_employee_by_id(
    employee_record_id: int,
) -> EmployeeSchema | None:
    """Delete one employee by ID

    Args:
        employee_record_id (int): The employee ID

    Returns:
        EmployeeSchema: The deleted employee record if found else nothing
    """
    # create the delete query
    query: DeleteQuery = EmployeesTable.delete().where(EmployeesTable.c.id == employee_record_id).returning(EmployeesTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    if not record:
        return None
    # return the deleted record
    return EmployeeSchema(**record._mapping)
