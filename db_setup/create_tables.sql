CREATE DATABASE kuzzy_noble_db;

USE kuzzy_noble_db;

-- Creating the Branch table
CREATE TABLE branch (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Department table
CREATE TABLE department (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    branch_id INT,
    FOREIGN KEY (branch_id) REFERENCES branch(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Role table
CREATE TABLE role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Employee table
CREATE TABLE employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id VARCHAR(255),
    title VARCHAR(255),
    name VARCHAR(255) NOT NULL,
    gender ENUM('Male', 'Female', 'Other'),
    date_of_birth DATE,
    nationality VARCHAR(255),
    phone_number VARCHAR(15),
    email_address VARCHAR(255),
    department_id INT,
    branch_id INT,
    role_id INT,
    FOREIGN KEY (department_id) REFERENCES department(id),
    FOREIGN KEY (branch_id) REFERENCES branch(id),
    FOREIGN KEY (role_id) REFERENCES role(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Institution table
CREATE TABLE institution (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    phone_number VARCHAR(15),
    email_address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Doctor table
CREATE TABLE doctor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15),
    email_address VARCHAR(255),
    institution_id INT,
    FOREIGN KEY (institution_id) REFERENCES institution(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Patient's table
CREATE TABLE patient (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_code VARCHAR(255),
    name VARCHAR(255) NOT NULL,
    gender ENUM('Male', 'Female', 'Other'),
    phone_number VARCHAR(15),
    email_address VARCHAR(255),
    date_of_birth DATE,
    enrolled_by INT,
    enrollment_branch_id INT,
    FOREIGN KEY (enrolled_by) REFERENCES employee(id),
    FOREIGN KEY (enrollment_branch_id) REFERENCES branch(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Test Category table
CREATE TABLE test_category (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Test table
CREATE TABLE test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    abbreviation VARCHAR(255),
    test_category_id INT,
    price DECIMAL(10, 2),
    turnaround_time_in_hours INT,
    unit VARCHAR(255),
    consultants VARCHAR(255),
    FOREIGN KEY (test_category_id) REFERENCES test_category(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Sample Type table
CREATE TABLE sample_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    specimens VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Sample table
CREATE TABLE sample (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sample_code VARCHAR(255),
    sample_type_id INT,
    patient_id INT,
    collected_by INT,
    collected_at TIMESTAMP,
    initial_quantity DECIMAL(10, 2),
    initial_quantity_unit VARCHAR(255),
    additional_information TEXT,
    FOREIGN KEY (sample_type_id) REFERENCES sample_type(id),
    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (collected_by) REFERENCES employee(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Medical Report table
CREATE TABLE medical_report (
    id INT AUTO_INCREMENT PRIMARY KEY,
    report_code VARCHAR(255),
    patient_id INT,
    sample_id INT,
    test_id INT,
    specimen VARCHAR(255),
    price DECIMAL(10, 2),
    created_by INT,
    result DECIMAL(10, 2),
    result_unit VARCHAR(255),
    comment TEXT,
    is_done BOOLEAN,
    is_quality_checked BOOLEAN,
    is_signed BOOLEAN,
    signed_by INT,
    FOREIGN KEY (patient_id) REFERENCES patient(id),
    FOREIGN KEY (sample_id) REFERENCES sample(id),
    FOREIGN KEY (test_id) REFERENCES test(id),
    FOREIGN KEY (created_by) REFERENCES employee(id),
    FOREIGN KEY (signed_by) REFERENCES employee(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Creating the Payment Method table
CREATE TABLE payment_method (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create Payment table
CREATE TABLE payment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    payment_code VARCHAR(255),
    amount_paid DECIMAL(10, 2),
    discount DECIMAL(10, 2),
    is_receivable BOOLEAN,
    payment_method_id INT,
    cash_handler_id INT,
    medical_report_id INT,
    FOREIGN KEY (payment_method_id) REFERENCES payment_method(id),
    FOREIGN KEY (cash_handler_id) REFERENCES employee(id),
    FOREIGN KEY (medical_report_id) REFERENCES medical_report(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create Branch view
CREATE VIEW branch_view AS (
    SELECT * FROM branch
);

-- Create Department view
CREATE VIEW department_view AS (
    SELECT 
    department.id,
    department.name,
    department.description,
    department.created_at,
    department.updated_at,
    branch.id AS branch_id,
    branch.name AS branch_name,
    branch.created_at AS branch_created_at,
    branch.updated_at AS branch_updated
    FROM department LEFT JOIN branch ON department.id=branch.id
);

-- Create Role view
CREATE VIEW role_view AS (
    SELECT * FROM role
);

-- Create Employee view
CREATE VIEW employee_view AS (
    SELECT
    employee_plus_department_branch.id,
    employee_plus_department_branch.employee_id,
    employee_plus_department_branch.title,
    employee_plus_department_branch.name,
    employee_plus_department_branch.gender,
    employee_plus_department_branch.date_of_birth,
    employee_plus_department_branch.nationality,
    employee_plus_department_branch.phone_number,
    employee_plus_department_branch.email_address,
    employee_plus_department_branch.created_at,
    employee_plus_department_branch.updated_at,
    employee_plus_department_branch.department_id,
    employee_plus_department_branch.department_name,
    employee_plus_department_branch.department_description,
    employee_plus_department_branch.department_created_at,
    employee_plus_department_branch.department_updated_at,
    employee_plus_department_branch.branch_id,
    employee_plus_department_branch.branch_name,
    employee_plus_department_branch.branch_address,
    employee_plus_department_branch.branch_created_at,
    employee_plus_department_branch.branch_updated,
    role.id AS role_id,
    role.name AS role_name,
    role.description AS role_description,
    role.created_at AS role_created_at,
    role.updated_at AS role_updated
    FROM
    (
        SELECT
        employee_plus_department.id,
        employee_plus_department.employee_id,
        employee_plus_department.title,
        employee_plus_department.name,
        employee_plus_department.gender,
        employee_plus_department.date_of_birth,
        employee_plus_department.nationality,
        employee_plus_department.phone_number,
        employee_plus_department.email_address,
        employee_plus_department.role_id,
        employee_plus_department.created_at,
        employee_plus_department.updated_at,
        employee_plus_department.department_id,
        employee_plus_department.department_name,
        employee_plus_department.department_description,
        employee_plus_department.department_created_at,
        employee_plus_department.department_updated_at,
        branch.id AS branch_id,
        branch.name AS branch_name,
        branch.address AS branch_address,
        branch.created_at AS branch_created_at,
        branch.updated_at AS branch_updated
        FROM
        (
            SELECT 
            employee.id,
            employee.employee_id,
            employee.title,
            employee.name,
            employee.gender,
            employee.date_of_birth,
            employee.nationality,
            employee.phone_number,
            employee.email_address,
            employee.branch_id,
            employee.role_id,
            employee.created_at,
            employee.updated_at,
            department.id AS department_id,
            department.name AS department_name,
            department.description AS department_description,
            department.created_at AS department_created_at,
            department.updated_at AS department_updated_at
            FROM employee LEFT JOIN department ON employee.id=department.id
        ) AS employee_plus_department
        LEFT JOIN branch ON employee_plus_department.branch_id=branch.id
    ) AS employee_plus_department_branch
    LEFT JOIN role ON employee_plus_department_branch.role_id=role.id
);