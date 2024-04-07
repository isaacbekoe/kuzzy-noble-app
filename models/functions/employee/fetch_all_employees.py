from models.database import db_conn_handle, db_connection_handler
from models.views.employee import EmployeesView
from models.schemas.employee import EmployeeViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from databases.core import Record
from sqlalchemy import func


@db_connection_handler
async def fetch_all_employees(skip: int, limit: int) -> tuple[list[EmployeeViewSchema], int]:
    """Fetch all employees

    Args:
        skip (int): The number of records to skip
        limit (int): The number of records to select

    Returns:
        tuple[list[EmployeeViewSchema], int]: A list of employees and the total number of matching records
    """
    # get the total number of records
    query: SelectQuery = EmployeesView.select().where().with_only_columns(*[func.count()])
    records_count: int = await db_conn_handle.execute(query=query)
    # create the select query
    query: SelectQuery = EmployeesView.select().where().order_by(EmployeesView.c.name).limit(limit).offset(skip)
    # execute the query, select the employees without loading then all into
    # memory at once
    selected_employees = []
    row: Record
    async for row in db_conn_handle.iterate(query=query):
        selected_employees.append(EmployeeViewSchema(**row._mapping))
    # return the selected employees
    return selected_employees, records_count
