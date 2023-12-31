"""
This script provides functions to interact with an SQLite database and insert sample data into the 'cv_data' table.

Author: Your Name
"""

import sqlite3

def insert_data_and_get_variables():
    """
    Inserts sample data into the 'cv_data' table and returns the inserted data as a dictionary.

    Returns:
    dict: A dictionary containing the inserted data.
    """
    conn = sqlite3.connect('cv_database.db')
    c = conn.cursor()

    # Create 'cv_data' table if it does not exist
    c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='cv_data'")
    if not c.fetchone():
        c.execute('''
            CREATE TABLE cv_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT,
                address TEXT,
                education TEXT,
                skills TEXT,
                experience TEXT,
                projects TEXT
            )
        ''')

    # Sample data
    name = "Gregory Claassen"
    email = "ggwiese@gmail.com"
    phone = "+27734644578"
    address = "Cape Town, South Africa"
    education = """NDiploma in Marketing Management - University of South Africa (UNISA) (2009),
    National Certificate N4-N6 in Marketing Management from Northlink College (2006 - 2008),
    Basic Computer Literacy Certificate from Office Administration (2009),
    ICDL (International Computer Driver’s License) Certificate from Northlink College (2009)
    """
    skills = """HTML5, CSS3, Python, Streamlit, Flask, PostgreSQL"""
    experience = """
    Administration Specialist - Old Mutual Claims and Underwriting (2010 - Current)

    Key Responsibilities:
    - Managed and tracked various daily administrative tasks across departments, including:
        - Medical coding
        - Customer reassurance
        - Medical investigations
        - Auditing
    - Maintained accurate and up-to-date spreadsheets (MIS) for efficient data management.
    - Handled web recall activities, ensuring compliance with enquiry categories and acceptance of terms.
    - Provided coaching and training for staff on Greenlight / OMP product and process knowledge, empowering them to work independently and deliver excellent service.
    - Offered empathetic and efficient inbound phone line support for intermediaries via telephonic contact model, exceeding customer satisfaction expectations.
    """
    projects = "https://github.com/Gaiatuven"

    try:
        # Insert data into the 'cv_data' table
        c.execute("INSERT INTO cv_data (name, email, phone, address, education, skills, experience, projects) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                  (name, email, phone, address, education, skills, experience, projects))
        conn.commit()
        print("Data inserted successfully!")
    except sqlite3.Error as e:
        print("Error inserting data:", e)

    conn.close()

    # Return the inserted data as a dictionary
    return {
        'name': name,
        'email': email,
        'phone': phone,
        'address': address,
        'education': education,
        'skills': skills,
        'experience': experience,
        'projects': projects
    }
