from models.database import db_conn_handle, db_connection_handler
from models.views.department import DepartmentsView
from models.schemas.department import DepartmentViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record
from sqlalchemy import func


@db_connection_handler
async def fetch_all_departments(skip: int, limit: int) -> tuple[list[DepartmentViewSchema], int]:
    """Fetch all departments

    Args:
        skip (int): The number of records to skip
        limit (int): The number of records to select

    Returns:
        tuple[list[DepartmentViewSchema], int]: A list of departments and the total number of matching records
    """
    # get the total number of records
    query: SelectQuery = DepartmentsView.select().where().with_only_columns(*[func.count()])
    records_count: int = await db_conn_handle.execute(query=query)
    # create the select query
    query: SelectQuery = DepartmentsView.select().where().order_by(DepartmentsView.c.name).limit(limit).offset(skip)
    # execute the query, select the departments without loading then all into
    # memory at once
    selected_departments = []
    row: Record
    async for row in db_conn_handle.iterate(query=query):
        selected_departments.append(DepartmentViewSchema(**row._mapping))
    # return the selected departments
    return selected_departments, records_count
