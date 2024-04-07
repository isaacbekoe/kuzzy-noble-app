from models.database import db_conn_handle, db_connection_handler
from models.views.department import DepartmentsView
from models.schemas.department import DepartmentViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record


@db_connection_handler
async def fetch_one_department_by_id(department_id: int) -> DepartmentViewSchema | None:
    """Fetch one department by ID

    Args:
        department_id (int): The department ID

    Returns:
        DepartmentSchema: The department if found else nothing
    """
    # prepare the query
    query: SelectQuery = DepartmentsView.select().where(DepartmentsView.c.id == department_id)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if record is not found
    if not record:
        return None
    # return the record
    return DepartmentViewSchema(**record._mapping)
