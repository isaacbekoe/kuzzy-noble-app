from models.database import db_conn_handle, db_connection_handler
from models.tables.role import RolesTable
from models.schemas.role import CreateRoleSchema, RoleSchema
from sqlalchemy.sql.expression import (
    Insert as InsertQuery
)
from datetime import datetime, timezone


@db_connection_handler
@db_conn_handle.transaction()
async def add_one_role(data: CreateRoleSchema) -> RoleSchema:
    """Add one role

    Args:
        data (CreateRoleSchema): The input data

    Returns:
        RoleSchema: The new role record
    """
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the insert query
    query: InsertQuery = RolesTable.insert().values(
        **vars(data),
        created_at=now,
        updated_at=now
    )
    # execute the query
    last_record_id: int = await db_conn_handle.execute(query=query)
    # return the new record
    return RoleSchema(
        id=last_record_id,
        **vars(data),
        created_at=now,
        updated_at=now
    )
