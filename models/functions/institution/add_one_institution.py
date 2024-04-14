from models.database import db_conn_handle, db_connection_handler
from models.tables.institution import InstitutionsTable
from models.schemas.institution import CreateInstitutionSchema, InstitutionSchema
from sqlalchemy.sql.expression import (
    Insert as InsertQuery
)
from datetime import datetime, timezone


@db_connection_handler
@db_conn_handle.transaction()
async def add_one_institution(data: CreateInstitutionSchema) -> InstitutionSchema:
    """Add one institution

    Args:
        data (CreateInstitutionSchema): The input data

    Returns:
        InstitutionSchema: The new institution record
    """
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the insert query
    query: InsertQuery = InstitutionsTable.insert().values(
        **vars(data),
        created_at=now,
        updated_at=now
    )
    # execute the query
    last_record_id: int = await db_conn_handle.execute(query=query)
    # return the new record
    return InstitutionSchema(
        id=last_record_id,
        **vars(data),
        created_at=now,
        updated_at=now
    )
