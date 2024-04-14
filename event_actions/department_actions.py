from PyQt6 import QtWidgets
from models.schemas.department import (
    CreateDepartmentSchema, 
    SearchDepartmentSchema,
)
from models.functions.department import (
    add_one_department,
    delete_one_department_by_id,
    search_departments,
    fetch_all_departments,
)


def add_department(self) -> None:
    try:
        name = self.departmentNameLineEdit.text()
        description = self.departmentDescriptionLineEdit.text()
        selected_branch_idx: int = self.departmentBranchComboBox.currentIndex() - 1
        branch_id = (self.branch_selection_options[selected_branch_idx].id if selected_branch_idx >= 0 else None)
        data: CreateDepartmentSchema = CreateDepartmentSchema(
            name=name if name else None,
            description=description if description else None,
            branch_id=branch_id
        )
        self.event_loop.run_until_complete(add_one_department(data=data))
        load_all_departments(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Department added successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to add department")
    
    
def reset_department_form(self) -> None:
    self.departmentNameLineEdit.setText("")
    self.departmentDescriptionLineEdit.setText("")
    self.departmentBranchComboBox.setCurrentIndex(0)
    

def delete_department(self):
    try:
        selected_row_idx = self.departmentsTableWidget.currentRow()
        self.event_loop.run_until_complete(delete_one_department_by_id(department_id=self.departments_table_data[selected_row_idx].id))
        load_all_departments(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Department deleted successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to delete department")
    
    
def load_all_departments(self):
    self.departments_table_data, _ = self.event_loop.run_until_complete(fetch_all_departments(0, 100))
    self.department_selection_options = self.departments_table_data.copy()
    item_names: list[str] = [None]
    self.departmentsTableWidget.setRowCount(0)
    row_position = self.departmentsTableWidget.rowCount()
    for record in self.departments_table_data:
        self.departmentsTableWidget.insertRow(row_position)
        self.departmentsTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.name))
        self.departmentsTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.description))
        self.departmentsTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.departmentsTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        self.departmentsTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(record.branch_name))
        row_position += 1
        item_names.append(f"{record.name} - {record.branch_name}")
    self.employeeDepartmentComboBox.clear()
    self.employeeDepartmentComboBox.addItems(item_names)
        
        
def filter_departments(self):
    query = self.searchDepartmentLineEdit.text()
    data: SearchDepartmentSchema = SearchDepartmentSchema(name=query)
    self.departments_table_data, _ = self.event_loop.run_until_complete(search_departments(data=data, skip=0, limit=100))
    self.departmentsTableWidget.setRowCount(0)
    row_position = self.departmentsTableWidget.rowCount()
    for record in self.departments_table_data:
        self.departmentsTableWidget.insertRow(row_position)
        self.departmentsTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.name))
        self.departmentsTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.description))
        self.departmentsTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.departmentsTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        self.departmentsTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(record.branch_name))
        row_position += 1