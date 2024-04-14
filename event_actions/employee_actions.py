from datetime import datetime, timezone, date
from PyQt6 import QtWidgets, QtCore
from models.schemas.employee import (
    CreateEmployeeSchema, 
    SearchEmployeeSchema,
)
from models.functions.employee import (
    add_one_employee,
    delete_one_employee_by_id,
    search_employees,
    fetch_all_employees,
)


def add_employee(self) -> None:
    try:
        employee_id = self.employeeIdLineEdit.text()
        title = self.employeeTitleComboBox.currentText()
        name = self.employeeNameLineEdit.text()
        gender = self.employeeGenderComboBox.currentText()
        qdate_value = self.employeeDateOfBirthDateEdit.date()
        date_of_birth = date(qdate_value.year(), qdate_value.month(), qdate_value.day())
        nationality = self.employeeNationalityLineEdit.text()
        email_address = self.employeeEmailAddressLineEdit.text()
        phone_number = self.employeePhoneNumberLineEdit.text()
        selected_branch_idx: int = self.employeeBranchComboBox.currentIndex() - 1
        branch_id = (self.branch_selection_options[selected_branch_idx].id if selected_branch_idx >= 0 else None)
        selected_department_idx: int = self.employeeDepartmentComboBox.currentIndex() - 1
        department_id = (self.department_selection_options[selected_department_idx].id if selected_department_idx >= 0 else None)
        selected_role_idx: int = self.employeeRoleComboBox.currentIndex() - 1
        role_id = (self.role_selection_options[selected_role_idx].id if selected_role_idx >= 0 else None)
        data: CreateEmployeeSchema = CreateEmployeeSchema(
            employee_id=employee_id,
            title=title,
            name=name,
            gender=gender,
            date_of_birth=date_of_birth,
            nationality=nationality,
            email_address=email_address,
            phone_number=phone_number,
            department_id=department_id if department_id else None,
            branch_id=branch_id if branch_id else None,
            role_id=role_id
        )
        self.event_loop.run_until_complete(add_one_employee(data=data))
        load_all_employees(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Employee added successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to add employee")
    
    
def reset_employee_form(self) -> None:
    self.employeeIdLineEdit.setText("")
    self.employeeTitleComboBox.setCurrentIndex(0)
    self.employeeNameLineEdit.setText("")
    self.employeeGenderComboBox.setCurrentIndex(0)
    date_now = datetime.now(tz=timezone.utc)
    self.employeeDateOfBirthDateEdit.setDate(QtCore.QDate(date_now.year, date_now.month, date_now.day))
    self.employeeNationalityLineEdit.setText("")
    self.employeePhoneNumberLineEdit.setText("")
    self.employeeEmailAddressLineEdit.setText("")
    self.employeeBranchComboBox.setCurrentIndex(0)
    self.employeeDepartmentComboBox.setCurrentIndex(0)
    self.employeeRoleComboBox.setCurrentIndex(0)
    

def delete_employee(self):
    try:
        selected_row_idx = self.employeesTableWidget.currentRow()
        self.event_loop.run_until_complete(delete_one_employee_by_id(employee_record_id=self.employees_table_data[selected_row_idx].id))
        load_all_employees(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Employee deleted successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to delete employee")
    
    
def load_all_employees(self):
    self.employees_table_data, _ = self.event_loop.run_until_complete(fetch_all_employees(0, 100))
    self.employee_selection_options = self.employees_table_data.copy()
    item_names: list[str] = [None]
    self.employeesTableWidget.setRowCount(0)
    row_position = self.employeesTableWidget.rowCount()
    for record in self.employees_table_data:
        self.employeesTableWidget.insertRow(row_position)
        self.employeesTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.employee_id))
        self.employeesTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.title))
        self.employeesTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(record.name))
        self.employeesTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(record.gender))
        self.employeesTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(record.date_of_birth)))
        self.employeesTableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(record.nationality))
        self.employeesTableWidget.setItem(row_position, 7, QtWidgets.QTableWidgetItem(record.email_address))
        self.employeesTableWidget.setItem(row_position, 6, QtWidgets.QTableWidgetItem(record.phone_number))
        self.employeesTableWidget.setItem(row_position, 8, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.employeesTableWidget.setItem(row_position, 9, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        self.employeesTableWidget.setItem(row_position, 10, QtWidgets.QTableWidgetItem(record.branch_name))
        self.employeesTableWidget.setItem(row_position, 11, QtWidgets.QTableWidgetItem(record.department_name))
        row_position += 1
        item_names.append(record.name)
        
        
def filter_employees(self):
    query = self.searchEmployeeLineEdit.text()
    data: SearchEmployeeSchema = SearchEmployeeSchema(name=query)
    self.employees_table_data, _ = self.event_loop.run_until_complete(search_employees(data=data, skip=0, limit=100))
    self.employeesTableWidget.setRowCount(0)
    row_position = self.employeesTableWidget.rowCount()
    for record in self.employees_table_data:
        self.employeesTableWidget.insertRow(row_position)
        self.employeesTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.employee_id))
        self.employeesTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.title))
        self.employeesTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(record.name))
        self.employeesTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(record.gender))
        self.employeesTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(record.date_of_birth)))
        self.employeesTableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(record.nationality))
        self.employeesTableWidget.setItem(row_position, 6, QtWidgets.QTableWidgetItem(record.phone_number))
        self.employeesTableWidget.setItem(row_position, 7, QtWidgets.QTableWidgetItem(record.email_address))
        self.employeesTableWidget.setItem(row_position, 8, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.employeesTableWidget.setItem(row_position, 9, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        self.employeesTableWidget.setItem(row_position, 10, QtWidgets.QTableWidgetItem(record.branch_name))
        self.employeesTableWidget.setItem(row_position, 11, QtWidgets.QTableWidgetItem(record.department_name))
        row_position += 1