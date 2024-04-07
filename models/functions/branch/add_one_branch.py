from models.database import db_conn_handle, db_connection_handler
from models.tables.branch import BranchesTable
from models.schemas.branch import CreateBranchSchema, BranchSchema
from sqlalchemy.sql.expression import (
    Insert as InsertQuery
)
from datetime import datetime, timezone


@db_connection_handler
@db_conn_handle.transaction()
async def add_one_branch(data: CreateBranchSchema) -> BranchSchema:
    """Add one branch

    Args:
        data (CreateBranchSchema): The input data

    Returns:
        BranchSchema: The new branch record
    """
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the insert query
    query: InsertQuery = BranchesTable.insert().values(
        **vars(data),
        created_at=now,
        updated_at=now
    )
    # execute the query
    last_record_id: int = await db_conn_handle.execute(query=query)
    # return the new record
    return BranchSchema(
        id=last_record_id,
        **vars(data),
        created_at=now,
        updated_at=now
    )
