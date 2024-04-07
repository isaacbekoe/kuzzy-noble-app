from models.database import db_conn_handle, db_connection_handler
from models.views.role import RolesView
from models.schemas.role import SearchRoleSchema, RoleViewSchema
from sqlalchemy.sql.expression import (
    Select as SelectQuery
)
from utils.shared import preprocess_search_params
from databases.core import Record
from sqlalchemy import func


@db_connection_handler
async def search_roles(data: SearchRoleSchema, skip: int, limit: int) -> tuple[list[RoleViewSchema], int]:
    """Search for roles

    Args:
        data (SearchRoleSchema): The search parameters
        skip (int): The number of records to skip
        limit (int): The number of records to select

    Returns:
        tuple[list[RoleViewSchema], int]: A list of roles and the total number of matching records
    """
    # extract only the fields that are not None for the search
    str_search_dict, other_types_search_dict, datetime_search_dict = preprocess_search_params(
        vars(data))
    # create the select query
    query: SelectQuery = RolesView.select().where()
    # add search terms for string fields to query
    for column_name, search_term in str_search_dict.items():
        query = query.where(
            RolesView.columns[column_name].ilike(search_term))
    # add date search items to query
    for column_name, search_term in datetime_search_dict.items():
        query = query.where(
            func.date(
                RolesView.columns[column_name]) == search_term)
    # add other search terms to query
    for column_name, search_term in other_types_search_dict.items():
        query = query.where(
            RolesView.columns[column_name] == search_term)
    # get the total number of records
    count_query: SelectQuery = query.with_only_columns(*[func.count()])
    records_count: int = await db_conn_handle.execute(query=count_query)
    # add sort by field, limit and skip contraints to query
    query = query.order_by(RolesView.c.name).limit(limit).offset(skip)
    # execute the query, select the roles without loading then all into
    # memory at once
    selected_roles = []
    row: Record
    async for row in db_conn_handle.iterate(query=query):
        selected_roles.append(RoleViewSchema(**row._mapping))
    # return the selected roles
    return selected_roles, records_count
