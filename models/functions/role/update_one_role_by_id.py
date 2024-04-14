from models.database import db_conn_handle, db_connection_handler
from models.tables.role import RolesTable
from models.schemas.role import UpdateRoleSchema, RoleSchema
from sqlalchemy.sql.expression import (
    Update as UpdateQuery
)
from datetime import datetime, timezone
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def update_one_role_by_id(
    role_id: int,
    data: UpdateRoleSchema,
) -> RoleSchema | None:
    """Update one role by ID

    Args:
        role_id (int): The role ID
        data (UpdateRoleSchema): The input data

    Returns:
        RoleSchema: The updated role record if found else nothing
    """
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the update query
    query: UpdateQuery = RolesTable.update().where(
        RolesTable.c.id == role_id
    ).values(
        **vars(data),
        updated_at=now
    ).returning(RolesTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if the record was not found
    if not record:
        return None
    # return the updated record
    return RoleSchema(**record._mapping)
