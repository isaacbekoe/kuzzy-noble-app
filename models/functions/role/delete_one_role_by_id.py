from models.database import db_conn_handle, db_connection_handler
from models.tables.role import RolesTable
from models.schemas.role import RoleSchema
from sqlalchemy.sql.expression import (
    Delete as DeleteQuery
)
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def delete_one_role_by_id(
    role_id: int,
) -> RoleSchema | None:
    """Delete one role by ID

    Args:
        role_id (int): The role ID

    Returns:
        RoleSchema: The deleted role record if found else nothing
    """
    # create the delete query
    query: DeleteQuery = RolesTable.delete().where(RolesTable.c.id == role_id).returning(RolesTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    if not record:
        return None
    # return the deleted record
    return RoleSchema(**record._mapping)
