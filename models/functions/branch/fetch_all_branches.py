from models.database import db_conn_handle, db_connection_handler
from models.views.branch import BranchesView
from models.schemas.branch import BranchViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record
from sqlalchemy import func


@db_connection_handler
async def fetch_all_branches(skip: int, limit: int) -> tuple[list[BranchViewSchema], int]:
    """Fetch all branches

    Args:
        skip (int): The number of records to skip
        limit (int): The number of records to select

    Returns:
        tuple[list[BranchViewSchema], int]: A list of branches and the total number of matching records
    """
    # get the total number of records
    query: SelectQuery = BranchesView.select().where().with_only_columns(*[func.count()])
    records_count: int = await db_conn_handle.execute(query=query)
    # create the select query
    query: SelectQuery = BranchesView.select().where().order_by(BranchesView.c.name).limit(limit).offset(skip)
    # execute the query, select the branches without loading then all into
    # memory at once
    selected_branches = []
    row: Record
    async for row in db_conn_handle.iterate(query=query):
        selected_branches.append(BranchViewSchema(**row._mapping))
    # return the selected branches
    return selected_branches, records_count
