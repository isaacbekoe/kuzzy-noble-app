from models.database import db_conn_handle, db_connection_handler
from models.views.institution import InstitutionsView
from models.schemas.institution import InstitutionViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record


@db_connection_handler
async def fetch_one_institution_by_id(institution_id: int) -> InstitutionViewSchema | None:
    """Fetch one institution by ID

    Args:
        institution_id (int): The institution ID

    Returns:
        InstitutionViewSchema: The institution if found else nothing
    """
    # prepare the query
    query: SelectQuery = InstitutionsView.select().where(
        InstitutionsView.c.id == institution_id
    )
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if record is not found
    if not record:
        return None
    # return the record
    return InstitutionViewSchema(**record._mapping)
