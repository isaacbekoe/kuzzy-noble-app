from models.database import db_conn_handle, db_connection_handler
from models.tables.branch import BranchesTable
from models.schemas.branch import UpdateBranchSchema, BranchSchema, BranchViewSchema
from models.functions import branch as branch_functions
from sqlalchemy.sql.expression import (
    Update as UpdateQuery
)
from datetime import datetime, timezone
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def update_one_branch_by_id(
    branch_id: int,
    data: UpdateBranchSchema,
) -> BranchSchema | None:
    """Update one branch by ID

    Args:
        branch_id (int): The branch ID
        data (UpdateBranchSchema): The input data

    Returns:
        BranchSchema: The updated branch record if found else nothing
    """
    # get the current record
    current_record: BranchViewSchema | None = await branch_functions.fetch_one_branch_by_id(
        branch_id=branch_id
    )
    if not current_record:
        return None
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the update query
    query: UpdateQuery = BranchesTable.update().where(
        BranchesTable.c.id == branch_id
    ).values(
        **vars(data),
        updated_at=now
    ).returning(BranchesTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if the record was not found
    if not record:
        return None
    # return the updated record
    return BranchSchema(**record._mapping)
