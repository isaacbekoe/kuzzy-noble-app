-- select the first 5 employees
SELECT * FROM employee LIMIT 5;


-- select all employees who were born in the 21st century
SELECT * FROM employee WHERE date_of_birth >= DATE('2000-01-01');


-- select the total amount of money gained from running lab tests
SELECT SUM(price) FROM medical_report;


-- select the income obtained per month
SELECT 
CONCAT(YEAR(created_at), '-', LPAD(MONTH(created_at), 2, '0')) AS year_and_month, 
SUM(price) AS income
FROM medical_report
GROUP BY YEAR(created_at), MONTH(created_at);


-- select the number of employees in each department for each branch
SELECT
department_employee_counts_with_branch.department_name,
department_employee_counts_with_branch.employee_count,
branch.name AS branch_name
FROM
(
    SELECT 
    department.name AS department_name,
    department_employee_counts.employee_count,
    department.branch_id
    FROM
    (
        SELECT 
        department_id, 
        COUNT(department_id) AS employee_count
        FROM employee 
        GROUP BY department_id
    ) AS department_employee_counts
    INNER JOIN department
    ON department_employee_counts.department_id = department.id
) AS department_employee_counts_with_branch
LEFT JOIN branch
ON department_employee_counts_with_branch.branch_id = branch.id;


-- select the number of employees in each branch
SELECT 
branch.name AS branch_name,
branch_employee_counts.employee_count
FROM
(
    SELECT 
    branch_id, 
    COUNT(branch_id) AS employee_count
    FROM employee 
    GROUP BY branch_id
) AS branch_employee_counts
INNER JOIN branch
ON branch_employee_counts.branch_id = branch.id;


-- join departments to branches using left outer join
SELECT 
department.id,
department.name,
department.description,
department.created_at,
department.updated_at,
branch.id AS branch_id,
branch.name AS branch_name,
branch.address AS branch_address,
branch.created_at AS branch_created_at,
branch.updated_at AS branch_updated_at
FROM department LEFT JOIN branch ON department.branch_id=branch.id;


-- join the employees table to their corresponding roles, departments and branches using 
-- nested selected queries and left outer joins
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
employee_plus_department_branch.branch_updated_at,
role.id AS role_id,
role.name AS role_name,
role.description AS role_description,
role.created_at AS role_created_at,
role.updated_at AS role_updated_at
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
    branch.updated_at AS branch_updated_at
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
        FROM employee LEFT JOIN department ON employee.department_id=department.id
    ) AS employee_plus_department
    LEFT JOIN branch ON employee_plus_department.branch_id=branch.id
) AS employee_plus_department_branch
LEFT JOIN role ON employee_plus_department_branch.role_id=role.id;