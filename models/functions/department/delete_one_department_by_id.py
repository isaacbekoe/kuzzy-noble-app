from models.database import db_conn_handle, db_connection_handler
from models.tables.department import DepartmentsTable
from models.schemas.department import DepartmentSchema
from sqlalchemy.sql.expression import (
    Delete as DeleteQuery
)
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def delete_one_department_by_id(
    department_id: int,
) -> DepartmentSchema | None:
    """Delete one department by ID

    Args:
        department_id (int): The department ID

    Returns:
        DepartmentSchema: The deleted department record if found else nothing
    """
    # create the delete query
    query: DeleteQuery = DepartmentsTable.delete().where(DepartmentsTable.c.id == department_id).returning(DepartmentsTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    if not record:
        return None
    # return the deleted record
    return DepartmentSchema(**record._mapping)
