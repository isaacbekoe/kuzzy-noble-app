from models.database import db_conn_handle, db_connection_handler
from models.views.branch import BranchesView
from models.schemas.branch import BranchViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record


@db_connection_handler
async def fetch_one_branch_by_id(branch_id: int) -> BranchViewSchema | None:
    """Fetch one branch by ID

    Args:
        branch_id (int): The branch ID

    Returns:
        BranchViewSchema: The branch if found else nothing
    """
    # prepare the query
    query: SelectQuery = BranchesView.select().where(BranchesView.c.id == branch_id)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if record is not found
    if not record:
        return None
    # return the record
    return BranchViewSchema(**record._mapping)
