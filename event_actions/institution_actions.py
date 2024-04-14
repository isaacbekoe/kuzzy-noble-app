from PyQt6 import QtWidgets
from models.schemas.institution import (
    CreateInstitutionSchema, 
    SearchInstitutionSchema,
)
from models.functions.institution import (
    add_one_institution,
    delete_one_institution_by_id,
    search_institutions,
    fetch_all_institutions,
)


def add_institution(self) -> None:
    try:
        name = self.institutionNameLineEdit.text()
        address = self.institutionAddressLineEdit.text()
        phone_number = self.institutionPhoneNumberLineEdit.text()
        email_address = self.institutionEmailAddressLineEdit.text()
        data: CreateInstitutionSchema = CreateInstitutionSchema(
            name=name if name else None,
            address=address if address else None,
            phone_number=phone_number if phone_number else None,
            email_address=email_address if email_address else None,
        )
        self.event_loop.run_until_complete(add_one_institution(data=data))
        load_all_institutions(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Institution added successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to add institution")
    
    
def reset_institution_form(self) -> None:
    self.institutionNameLineEdit.setText("")
    self.institutionAddressLineEdit.setText("")
    self.institutionPhoneNumberLineEdit.setText("")
    self.institutionEmailAddressLineEdit.setText("")
    

def delete_institution(self):
    try:
        selected_row_idx = self.institutionsTableWidget.currentRow()
        self.event_loop.run_until_complete(delete_one_institution_by_id(institution_id=self.institutions_table_data[selected_row_idx].id))
        load_all_institutions(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Institution deleted successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to delete institution")
    
    
def load_all_institutions(self):
    self.institutions_table_data, _ = self.event_loop.run_until_complete(fetch_all_institutions(0, 100))
    self.institution_selection_options = self.institutions_table_data.copy()
    item_names: list[str] = [None]
    self.institutionsTableWidget.setRowCount(0)
    row_position = self.institutionsTableWidget.rowCount()
    for record in self.institutions_table_data:
        self.institutionsTableWidget.insertRow(row_position)
        self.institutionsTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.name))
        self.institutionsTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.address))
        self.institutionsTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(record.phone_number))
        self.institutionsTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(record.email_address))
        self.institutionsTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.institutionsTableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        row_position += 1
        item_names.append(record.name)
    self.doctorInstitutionComboBox.clear()
    self.doctorInstitutionComboBox.addItems(item_names)
    
        
def filter_institutions(self):
    query = self.searchInstitutionLineEdit.text()
    data: SearchInstitutionSchema = SearchInstitutionSchema(name=query)
    self.institutions_table_data, _ = self.event_loop.run_until_complete(search_institutions(data=data, skip=0, limit=100))
    self.institutionsTableWidget.setRowCount(0)
    row_position = self.institutionsTableWidget.rowCount()
    for record in self.institutions_table_data:
        self.institutionsTableWidget.insertRow(row_position)
        self.institutionsTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.name))
        self.institutionsTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.address))
        self.institutionsTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(record.phone_number))
        self.institutionsTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(record.email_address))
        self.institutionsTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.institutionsTableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        row_position += 1