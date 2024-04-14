from PyQt6 import QtWidgets
from models.schemas.doctor import (
    CreateDoctorSchema, 
    SearchDoctorSchema,
)
from models.functions.doctor import (
    add_one_doctor,
    delete_one_doctor_by_id,
    search_doctors,
    fetch_all_doctors,
)


def add_doctor(self) -> None:
    try:
        title = self.doctorTitleComboBox.currentText()
        name = self.doctorNameLineEdit.text()
        phone_number = self.doctorPhoneNumberLineEdit.text()
        email_address = self.doctorEmailAddressLineEdit.text()
        selected_institution_idx: int = self.doctorInstitutionComboBox.currentIndex() - 1
        institution_id = (self.institution_selection_options[selected_institution_idx].id if selected_institution_idx >= 0 else None)
        data: CreateDoctorSchema = CreateDoctorSchema(
            title=title if title else None,
            name=name if name else None,
            phone_number=phone_number if phone_number else None,
            email_address=email_address if email_address else None,
            institution_id=institution_id if institution_id else None,
        )
        self.event_loop.run_until_complete(add_one_doctor(data=data))
        load_all_doctors(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Doctor added successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to add doctor")
    
    
def reset_doctor_form(self) -> None:
    self.doctorTitleComboBox.setCurrentIndex(0)
    self.doctorNameLineEdit.setText("")
    self.doctorPhoneNumberLineEdit.setText("")
    self.doctorEmailAddressLineEdit.setText("")
    self.doctorInstitutionComboBox.setCurrentIndex(0)
    

def delete_doctor(self):
    try:
        selected_row_idx = self.doctorsTableWidget.currentRow()
        self.event_loop.run_until_complete(delete_one_doctor_by_id(doctor_id=self.doctors_table_data[selected_row_idx].id))
        load_all_doctors(self)
        QtWidgets.QMessageBox.information(self, "Operation Status", "Doctor deleted successfully")
    except Exception as e:
        print(e)
        QtWidgets.QMessageBox.critical(self, "Operation Status", "Failed to delete doctor")
    
    
def load_all_doctors(self):
    self.doctors_table_data, _ = self.event_loop.run_until_complete(fetch_all_doctors(0, 100))
    self.doctor_selection_options = self.doctors_table_data.copy()
    item_names: list[str] = [None]
    self.doctorsTableWidget.setRowCount(0)
    row_position = self.doctorsTableWidget.rowCount()
    for record in self.doctors_table_data:
        self.doctorsTableWidget.insertRow(row_position)
        self.doctorsTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.title))
        self.doctorsTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.name))
        self.doctorsTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(record.phone_number))
        self.doctorsTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(record.email_address))
        self.doctorsTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.doctorsTableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        self.doctorsTableWidget.setItem(row_position, 6, QtWidgets.QTableWidgetItem(record.institution_name))
        row_position += 1
        item_names.append(f"{record.name} - {record.institution_name}")
        
        
def filter_doctors(self):
    query = self.searchDoctorLineEdit.text()
    data: SearchDoctorSchema = SearchDoctorSchema(name=query)
    self.doctors_table_data, _ = self.event_loop.run_until_complete(search_doctors(data=data, skip=0, limit=100))
    self.doctorsTableWidget.setRowCount(0)
    row_position = self.doctorsTableWidget.rowCount()
    for record in self.doctors_table_data:
        self.doctorsTableWidget.insertRow(row_position)
        self.doctorsTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(record.title))
        self.doctorsTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(record.name))
        self.doctorsTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(record.phone_number))
        self.doctorsTableWidget.setItem(row_position, 3, QtWidgets.QTableWidgetItem(record.email_address))
        self.doctorsTableWidget.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(record.created_at)))
        self.doctorsTableWidget.setItem(row_position, 5, QtWidgets.QTableWidgetItem(str(record.updated_at)))
        self.doctorsTableWidget.setItem(row_position, 6, QtWidgets.QTableWidgetItem(record.institution_name))
        row_position += 1