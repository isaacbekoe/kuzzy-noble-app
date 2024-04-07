from models.database import db_conn_handle, db_connection_handler
from models.views.role import RolesView
from models.schemas.role import RoleViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record
from sqlalchemy import func


@db_connection_handler
async def fetch_all_roles(skip: int, limit: int) -> tuple[list[RoleViewSchema], int]:
    """Fetch all roles

    Args:
        skip (int): The number of records to skip
        limit (int): The number of records to select

    Returns:
        tuple[list[RoleViewSchema], int]: A list of roles and the total number of matching records
    """
    # get the total number of records
    query: SelectQuery = RolesView.select().where().with_only_columns(*[func.count()])
    records_count: int = await db_conn_handle.execute(query=query)
    # create the select query
    query: SelectQuery = RolesView.select().where().order_by(RolesView.c.name).limit(limit).offset(skip)
    # execute the query, select the roles without loading then all into
    # memory at once
    selected_roles = []
    row: Record
    async for row in db_conn_handle.iterate(query=query):
        selected_roles.append(RoleViewSchema(**row._mapping))
    # return the selected roles
    return selected_roles, records_count
