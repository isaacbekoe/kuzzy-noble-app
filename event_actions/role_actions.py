import asyncio
from PyQt6 import QtWidgets
from models.schemas.role import (
    CreateRoleSchema, 
    SearchRoleSchema,
)
from models.functions.role import (
    add_one_role,
    delete_one_role_by_id,
    search_roles,
    fetch_all_roles,
)


def add_role(self) -> None:
    try:
        name = self.roleNameLineEdit.text()
        description = self.roleDescriptionLineEdit.text()
        data: CreateRoleSchema = CreateRoleSchema(
            name=name,
            description=description
        )
        self.event_loop.run_until_complete(add_one_role(data=data))
        load_all_roles(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Role added successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to add role")
    
    
def reset_role_form(self) -> None:
    self.roleNameLineEdit.setText("")
    self.roleDescriptionLineEdit.setText("")
    

def delete_role(self):
    try:
        selected_row_idx = self.rolesTableWidget.currentRow()
        self.event_loop.run_until_complete(delete_one_role_by_id(role_id=self.roles_table_data[selected_row_idx].id))
        load_all_roles(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Role deleted successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to delete role")
    
    
def load_all_roles(self):
    self.roles_table_data, _ = self.event_loop.run_until_complete(fetch_all_roles(0, 100))
    self.role_selection_options = self.roles_table_data.copy()
    item_names: list[str] = [None]
    self.rolesTableWidget.setRowCount(0)
    row_position = self.rolesTableWidget.rowCount()
    for record in self.roles_table_data:
        self.rolesTableWidget.insertRow(row_position)
        self.rolesTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.name))
        self.rolesTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.description))
        self.rolesTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.rolesTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        row_position += 1
        item_names.append(record.name)
    self.employeeRoleComboBox.clear()
    self.employeeRoleComboBox.addItems(item_names)
        
        
def filter_roles(self):
    query = self.searchRoleLineEdit.text()
    data: SearchRoleSchema = SearchRoleSchema(name=query)
    self.roles_table_data, _ = self.event_loop.run_until_complete(search_roles(data=data, skip=0, limit=100))
    self.rolesTableWidget.setRowCount(0)
    row_position = self.rolesTableWidget.rowCount()
    for record in self.roles_table_data:
        self.rolesTableWidget.insertRow(row_position)
        self.rolesTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.name))
        self.rolesTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.description))
        self.rolesTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.rolesTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        row_position += 1