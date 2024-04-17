-- Inserting data into the branch table
INSERT INTO branch (name, address) VALUES
('Main Branch', '123 Main Street'),
('Downtown Branch', '456 Downtown Avenue'),
('Main Street Branch', '456 Downtown Avenue'),
('Southern Branch', '456 Downtown Avenue'),
('Uptown Branch', '789 Uptown Road');

-- Inserting data into the department table
INSERT INTO department (name, description, branch_id) VALUES
('Cardiology', 'Specializing in heart-related issues', 1),
('Radiology', 'Specializing in medical imaging', 2),
('Pathology', 'Specializing in laboratory analysis', 3),
('Pharmacy', 'Specializing in pharmaceuticals', 4),
('Orthopedia', 'Specializing in orthopedics', 5);

-- Inserting data into the role table
INSERT INTO role (name, description) VALUES
('Doctor', 'Medical practitioner'),
('Nurse', 'Healthcare professional'),
('Technician', 'Skilled worker'),
('Pharmacist', 'Professional pharmacist'),
('Surgeon', 'Professional surgeon');

-- Inserting data into the employee table
INSERT INTO employee (employee_id, title, name, gender, date_of_birth, nationality, phone_number, email_address, department_id, branch_id, role_id) VALUES
('EMP001', 'Dr.', 'John Smith', 'Male', '1980-01-15', 'American', '+123456789', 'johnsmith@example.com', 1, 1, 1),
('EMP002', 'Nurse', 'Emily Johnson', 'Female', '1985-05-20', 'Canadian', '+987654321', 'emilyjohnson@example.com', 2, 2, 2),
('EMP003', 'Technician', 'Michael Williams', 'Male', '1990-08-10', 'British', '+1122334455', 'michaelwilliams@example.com', 3, 3, 3),
('EMP004', 'Mrs.', 'Anita Boateng', 'Female', '2001-12-23', 'Ghanaian', '+233122334455', 'anitaboateng@example.com', 4, 4, 4),
('EMP005', 'Rev.', 'Cristus Pontus', 'Male', '1950-01-02', 'Spanish', '+45122334455', 'cristus@example.com', 5, 5, 5);

-- Inserting data into the institution table
INSERT INTO institution (name, address, phone_number, email_address) VALUES
('ABC Hospital', '123 Hospital Street', '+1122334455', 'info@abchospital.com'),
('XYZ Clinic', '456 Clinic Avenue', '+987654321', 'info@xyzclinic.com'),
('DEF Medical Center', '789 Medical Road', '+123456789', 'info@defmedicalcenter.com');

-- Inserting data into the doctor table
INSERT INTO doctor (title, name, phone_number, email_address, institution_id) VALUES
('Dr.', 'Sarah Johnson', '+1122334455', 'drsarah@example.com', 1),
('Dr.', 'Alex Wilson', '+987654321', 'dralex@example.com', 2),
('Dr.', 'Emma Davis', '+123456789', 'dremma@example.com', 3);

-- Inserting data into the patient table
INSERT INTO patient (patient_code, name, gender, phone_number, email_address, date_of_birth, enrolled_by, enrollment_branch_id) VALUES
('P001', 'Mark Johnson', 'Male', '+1122334455', 'markjohnson@example.com', '1988-03-25', 1, 1),
('P002', 'Alice Smith', 'Female', '+987654321', 'alicesmith@example.com', '1995-08-12', 2, 2),
('P003', 'Tom Wilson', 'Male', '+123456789', 'tomwilson@example.com', '1975-12-05', 3, 3);

-- Inserting data into the test category table
INSERT INTO test_category (name, description) VALUES
('Blood Test', 'Category for blood-related tests'),
('X-Ray', 'Category for X-ray tests'),
('MRI', 'Category for MRI tests');

-- Inserting data into the test table
INSERT INTO test (name, abbreviation, test_category_id, price, turnaround_time_in_hours, unit, consultants) VALUES
('Complete Blood Count', 'CBC', 1, 50.00, 24, 'cells/mm3', 'Hematologist'),
('X-Ray Imaging', 'XRI', 2, 100.00, 48, 'X-Ray Technician', 'Radiologist'),
('MRI Scan', 'MRI', 3, 300.00, 72, 'Tesla', 'mri@consulting.com');

-- Inserting data into the sample type table
INSERT INTO sample_type (name, description, specimens) VALUES
('Blood', 'Type for blood samples', 'Whole Blood, Serum, Plasma'),
('Urine', 'Type for urine samples', 'Urine'),
('Tissue', 'Type for tissue samples', 'Tissue');

-- Inserting data into the sample table
INSERT INTO sample (sample_code, sample_type_id, patient_id, collected_by, collected_at, initial_quantity, initial_quantity_unit, additional_information) VALUES
('S001', 1, 1, 1, '2024-04-14 08:00:00', 10.00, 'ml', 'Fasting sample'),
('S002', 2, 2, 2, '2024-04-14 09:00:00', 20.00, 'ml', 'First morning urine sample'),
('S003', 3, 3, 3, '2024-04-14 10:00:00', 5.00, 'mg', 'Biopsy from lung tissue');

-- Inserting data into the medical report table
INSERT INTO medical_report (report_code, patient_id, test_id, price, created_by, result, result_unit, comment) VALUES
('MR001', 1, 1, 50.00, 1, 12.5, 'mg/dL', 'Normal range'),
('MR002', 2, 2, 100.00, 2, 20.0, 'mg/dL', 'Above normal range'),
('MR003', 3, 3, 300.00, 3, 5.0, 'Tesla', 'Successful scan');

-- Inserting data into the payment method table
INSERT INTO payment_method (name, description) VALUES
('Credit Card', 'Payment via credit card'),
('Cash', 'Payment in cash'),
('Bank Transfer', 'Payment via bank transfer');

-- Inserting data into the payment table
INSERT INTO payment (payment_code, amount_paid, discount, payment_method_id, cash_handler_id, medical_report_id) VALUES
('PAY001', 150.00, 10.00, 1, 1, 1),
('PAY002', 200.00, 0.00, 2, 2, 2),
('PAY003', 300.00, 20.00, 3, 3, 3);
