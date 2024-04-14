from models.database import db_conn_handle, db_connection_handler
from models.tables.institution import InstitutionsTable
from models.schemas.institution import InstitutionSchema
from sqlalchemy.sql.expression import (
    Delete as DeleteQuery
)
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def delete_one_institution_by_id(
    institution_id: int,
) -> InstitutionSchema | None:
    """Delete one institution by ID

    Args:
        institution_id (int): The institution ID

    Returns:
        InstitutionSchema: The deleted institution record if found else nothing
    """
    # create the delete query
    query: DeleteQuery = InstitutionsTable.delete().where(
        InstitutionsTable.c.id == institution_id,
    ).returning(InstitutionsTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    if not record:
        return None
    # return the deleted record
    return InstitutionSchema(**record._mapping)
