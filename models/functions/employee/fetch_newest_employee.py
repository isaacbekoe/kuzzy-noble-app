from models.database import db_conn_handle, db_connection_handler
from models.views.employee import EmployeesView
from models.schemas.employee import EmployeeViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record
from sqlalchemy import desc


@db_connection_handler
async def fetch_newest_employee() -> EmployeeViewSchema | None:
    """Fetch the most recent employee that has been enrolled

    Returns:
        EmployeeSchema: The employee if found else nothing
    """
    # prepare the query
    query: SelectQuery = EmployeesView.select().order_by(
        desc(EmployeesView.c.created_at)).limit(1)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if record is not found
    if not record:
        return None
    # return the record
    return EmployeeViewSchema(**record._mapping)
