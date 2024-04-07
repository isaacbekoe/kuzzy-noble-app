from models.database import db_conn_handle, db_connection_handler
from models.tables.department import DepartmentsTable
from models.schemas.department import UpdateDepartmentSchema, DepartmentSchema, DepartmentViewSchema
from models.functions import department as department_functions
from sqlalchemy.sql.expression import (
    Update as UpdateQuery
)
from datetime import datetime, timezone
from databases.core import Record


@db_connection_handler
@db_conn_handle.transaction()
async def update_one_department_by_id(
    department_id: int,
    data: UpdateDepartmentSchema,
) -> DepartmentSchema | None:
    """Update one department by ID

    Args:
        department_id (int): The department ID
        data (UpdateDepartmentSchema): The input data
        revision_actor_user_id (uuid.UUID): The ID of the user submitting the record

    Returns:
        DepartmentSchema: The updated department record if found else nothing
    """
    # get the current record
    current_record: DepartmentViewSchema | None = await department_functions.fetch_one_department_by_id(
        department_id=department_id
    )
    if not current_record:
        return None
    # get the current date and time
    now = datetime.now(tz=timezone.utc)
    # create the update query
    query: UpdateQuery = DepartmentsTable.update().where(
        DepartmentsTable.c.id == department_id
    ).values(
        **vars(data),
        updated_at=now
    ).returning(DepartmentsTable)
    # execute the query
    record: Record | None = await db_conn_handle.fetch_one(query=query)
    # return nothing if the record was not found
    if not record:
        return None
    # return the updated record
    return DepartmentSchema(**record._mapping)
