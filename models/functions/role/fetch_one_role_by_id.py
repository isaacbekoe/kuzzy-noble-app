from models.database import db_conn_handle, db_connection_handler
from models.views.role import RolesView
from models.schemas.role import RoleViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record


@db_connection_handler
async def fetch_one_role_by_id(role_id: int) -> RoleViewSchema | None:
    """Fetch one role by ID

    Args:
        role_id (int): The role ID

    Returns:
        RoleViewSchema: The role if found else nothing
    """
    # prepare the query
    query: SelectQuery = RolesView.select().where(RolesView.c.id == role_id)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if record is not found
    if not record:
        return None
    # return the record
    return RoleViewSchema(**record._mapping)
