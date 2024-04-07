import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import uic
from models.schemas.branch import BranchViewSchema
from models.schemas.role import RoleViewSchema
from event_actions.branch_actions import (
    add_branch,
    reset_branch_form,
    load_all_branches,
    delete_branch,
    filter_branches,
)
from event_actions.role_actions import (
    add_role,
    reset_role_form,
    load_all_roles,
    delete_role,
    filter_roles,
)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # load the user interface
        uic.loadUi("./ui/mainwindow.ui", self)
        
        # NOTE: FOR BRANCHES
        # initialize table data
        self.branches_table_data: list[BranchViewSchema] = []
        # add button actions
        self.addBranchButton.pressed.connect(lambda: add_branch(self))
        self.resetBranchFormButton.pressed.connect(lambda: reset_branch_form(self))
        self.loadBranchesButton.pressed.connect(lambda: load_all_branches(self))
        self.deleteBranchButton.pressed.connect(lambda: delete_branch(self))
        self.searchBranchButton.pressed.connect(lambda: filter_branches(self))
        load_all_branches(self)
        
        # NOTE: FOR DEPARTMENTS
        
        # NOTE: FOR ROLES
        # initialize table data
        self.roles_table_data: list[RoleViewSchema] = []
        # add button actions
        self.addRoleButton.pressed.connect(lambda: add_role(self))
        self.resetRoleFormButton.pressed.connect(lambda: reset_role_form(self))
        self.loadRolesButton.pressed.connect(lambda: load_all_roles(self))
        self.deleteRoleButton.pressed.connect(lambda: delete_role(self))
        self.searchRoleButton.pressed.connect(lambda: filter_roles(self))
        load_all_roles(self)
        
        # NOTE: FOR EMPLOYEES
    
          
if __name__ == "__main__":
    # run application
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()