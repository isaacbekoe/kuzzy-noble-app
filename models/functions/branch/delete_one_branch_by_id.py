from models.database import db_conn_handle, db_connection_handler
from models.tables.branch import BranchesTable
from models.schemas.branch import BranchSchema
from sqlalchemy.sql.expression import (
    Delete as DeleteQuery
)
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def delete_one_branch_by_id(
    branch_id: int,
) -> BranchSchema | None:
    """Delete one branch by ID

    Args:
        branch_id (int): The branch ID

    Returns:
        BranchSchema: The deleted branch record if found else nothing
    """
    # create the delete query
    query: DeleteQuery = BranchesTable.delete().where(BranchesTable.c.id == branch_id).returning(BranchesTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    if not record:
        return None
    # return the deleted record
    return BranchSchema(**record._mapping)
