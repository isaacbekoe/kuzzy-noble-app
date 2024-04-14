from models.database import db_conn_handle, db_connection_handler
from models.views.institution import InstitutionsView
from models.schemas.institution import InstitutionViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record
from sqlalchemy import func


@db_connection_handler
async def fetch_all_institutions(skip: int, limit: int) -> tuple[list[InstitutionViewSchema], int]:
    """Fetch all institutions

    Args:
        skip (int): The number of records to skip
        limit (int): The number of records to select

    Returns:
        tuple[list[InstitutionViewSchema], int]: A list of institutions and the total number of matching records
    """
    # get the total number of records
    query: SelectQuery = InstitutionsView.select().where().with_only_columns(*[func.count()])
    records_count: int = await db_conn_handle.execute(query=query)
    # create the select query
    query: SelectQuery = InstitutionsView.select().where().order_by(InstitutionsView.c.name).limit(limit).offset(skip)
    # execute the query, select the institutions without loading then all into
    # memory at once
    selected_institutions = []
    row: Record
    async for row in db_conn_handle.iterate(query=query):
        selected_institutions.append(InstitutionViewSchema(**row._mapping))
    # return the selected institutions
    return selected_institutions, records_count
