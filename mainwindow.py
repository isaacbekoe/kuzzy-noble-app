import sys
import asyncio
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from models.schemas.branch import BranchViewSchema
from models.schemas.role import RoleViewSchema
from models.schemas.department import DepartmentViewSchema
from models.schemas.employee import EmployeeViewSchema
from event_actions.branch_actions import (
    add_branch,
    reset_branch_form,
    load_all_branches,
    delete_branch,
    filter_branches,
)
from event_actions.department_actions import (
    add_department,
    reset_department_form,
    load_all_departments,
    delete_department,
    filter_departments,
)
from event_actions.role_actions import (
    add_role,
    reset_role_form,
    load_all_roles,
    delete_role,
    filter_roles,
)
from event_actions.employee_actions import (
    add_employee,
    reset_employee_form,
    load_all_employees,
    delete_employee,
    filter_employees,
)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # load the user interface
        uic.loadUi("./ui/mainwindow.ui", self)
        
        # create a single event loop for the application
        self.event_loop = asyncio.get_event_loop()
        
        # NOTE: FOR BRANCHES
        # initialize table data
        self.branches_table_data: list[BranchViewSchema] = []
        self.branch_select_options: list[BranchViewSchema] = []
        # add button actions
        self.addBranchButton.pressed.connect(lambda: add_branch(self))
        self.resetBranchFormButton.pressed.connect(lambda: reset_branch_form(self))
        self.loadBranchesButton.pressed.connect(lambda: load_all_branches(self))
        self.deleteBranchButton.pressed.connect(lambda: delete_branch(self))
        self.searchBranchButton.pressed.connect(lambda: filter_branches(self))
        load_all_branches(self)
        
        # NOTE: FOR DEPARTMENTS
        # initialize table data
        self.departments_table_data: list[DepartmentViewSchema] = []
        self.department_selection_options: list[DepartmentViewSchema] = []
        # add button actions
        self.addDepartmentButton.pressed.connect(lambda: add_department(self))
        self.resetDepartmentFormButton.pressed.connect(lambda: reset_department_form(self))
        self.loadDepartmentsButton.pressed.connect(lambda: load_all_departments(self))
        self.deleteDepartmentButton.pressed.connect(lambda: delete_department(self))
        self.searchDepartmentButton.pressed.connect(lambda: filter_departments(self))
        load_all_departments(self)
        
        # NOTE: FOR ROLES
        # initialize table data
        self.roles_table_data: list[RoleViewSchema] = []
        self.role_selection_options: list[RoleViewSchema] = []
        # add button actions
        self.addRoleButton.pressed.connect(lambda: add_role(self))
        self.resetRoleFormButton.pressed.connect(lambda: reset_role_form(self))
        self.loadRolesButton.pressed.connect(lambda: load_all_roles(self))
        self.deleteRoleButton.pressed.connect(lambda: delete_role(self))
        self.searchRoleButton.pressed.connect(lambda: filter_roles(self))
        load_all_roles(self)
        
        # NOTE: FOR EMPLOYEES
        # initialize table data
        self.employees_table_data: list[EmployeeViewSchema] = []
        self.employee_selection_options: list[EmployeeViewSchema] = []
        # add button actions
        self.addEmployeeButton.pressed.connect(lambda: add_employee(self))
        self.resetEmployeeFormButton.pressed.connect(lambda: reset_employee_form(self))
        self.loadEmployeesButton.pressed.connect(lambda: load_all_employees(self))
        self.deleteEmployeeButton.pressed.connect(lambda: delete_employee(self))
        self.searchEmployeeButton.pressed.connect(lambda: filter_employees(self))
        load_all_employees(self)
    
          
if __name__ == "__main__":
    # run application
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()