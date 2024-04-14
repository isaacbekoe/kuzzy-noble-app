from PyQt6 import QtWidgets
from models.schemas.branch import (
    CreateBranchSchema, 
    SearchBranchSchema,
)
from models.functions.branch import (
    add_one_branch,
    delete_one_branch_by_id,
    search_branches,
    fetch_all_branches,
)


def add_branch(self) -> None:
    try:
        name = self.branchNameLineEdit.text()
        address = self.branchAddressLineEdit.text()
        data: CreateBranchSchema = CreateBranchSchema(
            name=name if name else None,
            address=address if address else None
        )
        self.event_loop.run_until_complete(add_one_branch(data=data))
        load_all_branches(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Branch added successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to add branch")
    
    
def reset_branch_form(self) -> None:
    self.branchNameLineEdit.setText("")
    self.branchAddressLineEdit.setText("")
    

def delete_branch(self):
    try:
        selected_row_idx = self.branchesTableWidget.currentRow()
        self.event_loop.run_until_complete(delete_one_branch_by_id(branch_id=self.branches_table_data[selected_row_idx].id))
        load_all_branches(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Branch deleted successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to delete branch")
    
    
def load_all_branches(self):
    self.branches_table_data, _ = self.event_loop.run_until_complete(fetch_all_branches(0, 100))
    self.branch_selection_options = self.branches_table_data.copy()
    item_names: list[str] = [None]
    self.branchesTableWidget.setRowCount(0)
    row_position = self.branchesTableWidget.rowCount()
    for record in self.branches_table_data:
        self.branchesTableWidget.insertRow(row_position)
        self.branchesTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.name))
        self.branchesTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.address))
        self.branchesTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.branchesTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        row_position += 1
        item_names.append(record.name)
    self.departmentBranchComboBox.clear()
    self.employeeBranchComboBox.clear()
    self.departmentBranchComboBox.addItems(item_names)
    self.employeeBranchComboBox.addItems(item_names)
    
        
def filter_branches(self):
    query = self.searchBranchLineEdit.text()
    data: SearchBranchSchema = SearchBranchSchema(name=query)
    self.branches_table_data, _ = self.event_loop.run_until_complete(search_branches(data=data, skip=0, limit=100))
    self.branchesTableWidget.setRowCount(0)
    row_position = self.branchesTableWidget.rowCount()
    for record in self.branches_table_data:
        self.branchesTableWidget.insertRow(row_position)
        self.branchesTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.name))
        self.branchesTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.address))
        self.branchesTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.branchesTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        row_position += 1