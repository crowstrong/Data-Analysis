import psycopg2
import random
from faker import Faker
from datetime import datetime
from tqdm import tqdm
from dotenv import load_dotenv
import os


load_dotenv()
# Connection to PostgreSQL
conn_params = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

fake = Faker('uk_UA')

# Skill codes and descriptions
skills_list = [
    ("РАД", "ручная аргонодуговая сварка неплавящимся электродом"),
    ("МАДП", "механизированная аргонодуговая сварка плавящимся электродом"),
    ("МП", "механизированная сварка плавящимся электродом в среде активных газов и смесях"),
    ("ААД", "автоматическая аргонодуговая сварка неплавящимся электродом"),
    ("АПГ", "автоматическая сварка плавящимся электродом в среде активных газов и смесях"),
    ("АПГН", "автоматическая наплавка плавящимся электродом в среде активных газов и смесях"),
    ("АППГ", "автоматическая сварка порошковой проволокой в среде активных газов и смесях"),
    ("АППГН", "автоматическая наплавка порошковой проволокой в среде активных газов и смесях"),
    ("ААДП", "автоматическая аргонодуговая сварка плавящимся электродом"),
    ("ААДН", "автоматическая аргонодуговая сварка или наплавка неплавящимся электродом"),
    ("МПГ", "механизированная сварка порошковой проволокой в среде активных газов"),
    ("РАДН", "ручная аргонодуговая наплавка"),
    ("АПИ", "автоматическая сварка порошковой проволокой в среде инертных газов и смесях"),
    ("АПИН", "автоматическая наплавка порошковой проволокой в среде инертных газов и смесях"),
    ("МПН", "механизированная наплавка плавящимся электродом в среде активных газов и смесях"),
    ("МАДПН", "механизированная аргонодуговая наплавка плавящимся электродом"),
    ("МПГН", "механизированная наплавка порошковой проволокой в среде активных газов и смесях"),
    ("МПИ", "механизированная сварка порошковой проволокой в среде инертных газов и смесях"),
    ("МПИН", "механизированная наплавка порошковой проволокой в среде инертных газов и смесях")
]

qualification_skill_map = {
    1: (1, 2),
    2: (2, 3),
    3: (3, 4),
    4: (4, 6),
    5: (5, 8),
    6: (6, 12)
}

email_domains = ['@gmail.com', '@hotmail.com', '@outlook.com', '@ukr.net']
city_list = list({fake.city_name() for _ in range(200)})

def connect_db(params):
    return psycopg2.connect(**params)

def get_or_create_city(cursor, name):
    cursor.execute("SELECT id FROM cities WHERE name = %s;", (name,))
    res = cursor.fetchone()
    if res:
        return res[0]
    cursor.execute("INSERT INTO cities (name) VALUES (%s) RETURNING id;", (name,))
    return cursor.fetchone()[0]

def get_or_create_qualification(cursor, level):
    cursor.execute("SELECT id FROM qualifications WHERE level = %s;", (level,))
    res = cursor.fetchone()
    if res:
        return res[0]
    cursor.execute("INSERT INTO qualifications (level) VALUES (%s) RETURNING id;", (level,))
    return cursor.fetchone()[0]

def get_or_create_skill(cursor, code, desc):
    cursor.execute("SELECT id FROM skills WHERE code = %s;", (code,))
    res = cursor.fetchone()
    if res:
        return res[0]
    cursor.execute("INSERT INTO skills (code, description) VALUES (%s, %s) RETURNING id;", (code, desc))
    return cursor.fetchone()[0]

def insert_reference_data(cursor):
    for code, desc in skills_list:
        get_or_create_skill(cursor, code, desc)
    for level in range(1, 7):
        get_or_create_qualification(cursor, level)
    for city in city_list:
        get_or_create_city(cursor, city)

def insert_welders(cursor, count=1000):
    for _ in tqdm(range(count), desc="Inserting welders"):
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
        gender = "male"
        birth_date = fake.date_of_birth(minimum_age=20, maximum_age=60)
        city_name = random.choice(city_list)
        qualification_level = random.randint(1, 6)
        exp_years = random.randint(1, 40)
        phone = fake.phone_number()
        email = f"{first_name.lower()}.{last_name.lower()}{random.randint(1,99)}{random.choice(email_domains)}"
        is_available = random.choice([True, False])
        created_at = datetime.now()

        city_id = get_or_create_city(cursor, city_name)
        qualification_id = get_or_create_qualification(cursor, qualification_level)

        cursor.execute("""
            INSERT INTO welders (
                name, surname, gender, birth_date, city_id, qualification_id,
                experience_years, phone_number, email, is_available, created_at
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id;
        """, (
            first_name, last_name, gender, birth_date, city_id, qualification_id,
            exp_years, phone, email, is_available, created_at
        ))
        welder_id = cursor.fetchone()[0]

        skill_count = random.randint(*qualification_skill_map[qualification_level])
        selected_skills = random.sample(skills_list, skill_count)

        for code, desc in selected_skills:
            skill_id = get_or_create_skill(cursor, code, desc)
            cursor.execute("""
                INSERT INTO welder_skills (welder_id, skill_id)
                VALUES (%s, %s) ON CONFLICT DO NOTHING;
            """, (welder_id, skill_id))


if __name__ == "__main__":
    # This block is for testing the script directly
    try:
        conn = connect_db(conn_params)
        conn.autocommit = True
        cur = conn.cursor()

        insert_reference_data(cur)
        insert_welders(cur, count=100)

        cur.close()
        conn.close()
        print("Mock data inserted successfully.")
    except Exception as e:
        print("Error:", e)
