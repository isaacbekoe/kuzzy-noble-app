# KUZZY NOBLE APP

This is a simple application for manipulating the Kuzzy Noble App project presented for the course IE6700.

## HOW TO RUN ON LOCAL MACHINE

1. Install and setup a MySQL database server. Two options include [XAMPP](https://www.apachefriends.org/download.html) or [MySQL Workbench](https://dev.mysql.com/downloads/workbench/).

2. As a root user on the MySQL database server application, run the SQL script in the file `db_setup/create_tables.sql` to setup the database.

3. Now, in the root directory of the project, create a `.env` file file by running the command:

   ```bash
   cp .env.example .env
   ```

   This will create a starter `.env` file.

4. Replace the value of the `DATABASE_URL` parameter with the appropriate connection string to the database created above. The format of the connection string is `mysql+aiomysql://<username>:@<host address>:<port>/kuzzy_noble_db`. An example of the default connection details in XAMPP is

   ```bash
   DATABASE_URL="mysql+aiomysql://root:@127.0.0.1:3306/kuzzy_noble_db"
   ```

5. Now, install [Python 3](https://www.python.org/downloads/) if not already installed.

6. In the root directory of the project, create a virtual environment using the command:

   ```bash
   python3 -m venv venv
   ```

7. Active the virtual environment with the command:

   On Linux or in bash shell

   ```bash
   . venv/bin/activate
   ```

   On Windows or in powershell

   ```bash
   ./venv/Scripts/activate.ps1
   ```

8. Install the project dependencies by running the command:

   ```bash
   pip install -r requirements.txt
   ```

9. Run the application with the command:

   ```bash
   python3 mainwindow.py
   ```

   