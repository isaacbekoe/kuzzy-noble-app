from models.database import db_conn_handle, db_connection_handler
from models.tables.institution import InstitutionsTable
from models.schemas.institution import UpdateInstitutionSchema, InstitutionSchema
from sqlalchemy.sql.expression import (
    Update as UpdateQuery
)
from datetime import datetime, timezone
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def update_one_institution_by_id(
    institution_id: int,
    data: UpdateInstitutionSchema,
) -> InstitutionSchema | None:
    """Update one institution by ID

    Args:
        institution_id (int): The institution ID
        data (UpdateInstitutionSchema): The input data

    Returns:
        InstitutionSchema: The updated institution record if found else nothing
    """
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the update query
    query: UpdateQuery = InstitutionsTable.update().where(
        InstitutionsTable.c.id == institution_id
    ).values(
        **vars(data),
        updated_at=now
    ).returning(InstitutionsTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if the record was not found
    if not record:
        return None
    # return the updated record
    return InstitutionSchema(**record._mapping)
