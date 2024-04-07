from models.database import db_conn_handle, db_connection_handler
from models.views.employee import EmployeesView
from models.schemas.employee import EmployeeViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record


@db_connection_handler
async def fetch_one_employee_by_id(employee_record_id: int) -> EmployeeViewSchema | None:
    """Fetch one employee by ID

    Args:
        employee_record_id (int): The employee ID

    Returns:
        EmployeeSchema: The employee if found else nothing
    """
    # prepare the query
    query: SelectQuery = EmployeesView.select().where(EmployeesView.c.id == employee_record_id)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if record is not found
    if not record:
        return None
    # return the record
    return EmployeeViewSchema(**record._mapping)
