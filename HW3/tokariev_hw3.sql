-- CONSTRAINTS
-- salary_expectations

ALTER TABLE salary_expectations
ADD CONSTRAINT salary_check CHECK (expected_salary >= acceptable_start_salary);

-- education

ALTER TABLE education
ADD CONSTRAINT year_valid CHECK (year_completed BETWEEN 1950 AND EXTRACT(YEAR FROM CURRENT_DATE));

-- learning_meta

ALTER TABLE learning_meta
ADD COLUMN daily_load INTEGER GENERATED ALWAYS AS (
    study_hours_per_day + work_hours_per_day
) STORED;

-- student_skills, student_learning_goals

ALTER TABLE student_skills
ADD CONSTRAINT unique_student_skill UNIQUE (student_id, skill_id);

ALTER TABLE student_learning_goals
ADD CONSTRAINT unique_student_goal UNIQUE (student_id, goal_id);

-- meta_data — update

ALTER TABLE meta_data
ALTER COLUMN st_id SET NOT NULL,
ALTER COLUMN edu_id SET NOT NULL;

ALTER TABLE meta_data
ADD CONSTRAINT fk_st_id FOREIGN KEY (st_id) REFERENCES students(id) ON DELETE CASCADE,
ADD CONSTRAINT fk_edu_id FOREIGN KEY (edu_id) REFERENCES education(id) ON DELETE CASCADE;

-- Checking for acceptable salary values
ALTER TABLE salary_expectations
ADD CONSTRAINT salary_check CHECK (expected_salary >= acceptable_start_salary);

-- Checking the valid year of completion of education
ALTER TABLE education
ADD CONSTRAINT year_valid CHECK (year_completed BETWEEN 1950 AND EXTRACT(YEAR FROM CURRENT_DATE));

-- Calculation column: total daily load (study + work)
ALTER TABLE learning_meta
ADD COLUMN daily_load INTEGER GENERATED ALWAYS AS (
    study_hours_per_day + work_hours_per_day
) STORED;

-- Prohibition of duplicates in the connection student ↔ skill
ALTER TABLE student_skills
ADD CONSTRAINT unique_student_skill UNIQUE (student_id, skill_id);

-- Prohibition of duplicates in the connection student ↔ learning goal
ALTER TABLE student_learning_goals
ADD CONSTRAINT unique_student_goal UNIQUE (student_id, goal_id);

-- Mandatory relationships and restrictions in meta_data
ALTER TABLE meta_data
ALTER COLUMN st_id SET NOT NULL,
ALTER COLUMN edu_id SET NOT NULL;

ALTER TABLE meta_data
ADD CONSTRAINT fk_st_id FOREIGN KEY (st_id) REFERENCES students(id) ON DELETE CASCADE,
ADD CONSTRAINT fk_edu_id FOREIGN KEY (edu_id) REFERENCES education(id) ON DELETE CASCADE;

-- feedback table
CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id) ON DELETE CASCADE,
    survey_id INTEGER REFERENCES surveys(id) ON DELETE CASCADE,
    comment TEXT,
    rating INTEGER CHECK (rating BETWEEN 1 AND 5),
    created_at TIMESTAMPTZ DEFAULT now()
);

-- EASTER EGG var

ALTER TABLE learning_meta
ADD COLUMN is_full_time BOOLEAN GENERATED ALWAYS AS (
    work_hours_per_day >= 6
) STORED;

-- unique skill on the student's list

ALTER TABLE student_skills
ADD CONSTRAINT unique_student_skill UNIQUE (student_id, skill_id);

-- group age limit (non-negative)

ALTER TABLE students
ADD CONSTRAINT age_positive CHECK (age_group > 0);

-- limitation “many courses” and “zero hours”

ALTER TABLE learning_meta
ADD CONSTRAINT course_time_check CHECK (
    NOT (courses_last_year > 0 AND study_hours_per_day = 0)
);

-- Calculation column: is_full_time

ALTER TABLE learning_meta
ADD COLUMN is_full_time BOOLEAN GENERATED ALWAYS AS (
    (study_hours_per_day + work_hours_per_day) >= 6
) STORED;

-- Logical exchange: control of educational progress

ALTER TABLE learning_meta
ADD CONSTRAINT course_load_check CHECK (
    NOT (courses_last_year > 0 AND study_hours_per_day = 0)
);

-- Localization (normalization of countries/regions/cities)

-- countries
CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

-- states
CREATE TABLE states (
    id SERIAL PRIMARY KEY,
    country_id INTEGER REFERENCES countries(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    UNIQUE (country_id, name)
);


-- cities
CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    state_id INTEGER REFERENCES states(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    UNIQUE (state_id, name)
);

-- Audit / change log
-- track all INSERT/UPDATE/DELETE
-- understand who changed the data and when
-- useful when working with multiple users

-- change_log table
CREATE TABLE change_log (
    id SERIAL PRIMARY KEY,
    table_name TEXT NOT NULL,
    record_id INTEGER,
    action TEXT NOT NULL CHECK (action IN ('INSERT', 'UPDATE', 'DELETE')),
    changed_at TIMESTAMPTZ DEFAULT now(),
    changed_by TEXT 
);

-- log trigger

CREATE OR REPLACE FUNCTION log_meta_data_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'INSERT') THEN
        INSERT INTO change_log(table_name, record_id, action)
        VALUES (TG_TABLE_NAME, NEW.id, 'INSERT');
        RETURN NEW;
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO change_log(table_name, record_id, action)
        VALUES (TG_TABLE_NAME, NEW.id, 'UPDATE');
        RETURN NEW;
    ELSIF (TG_OP = 'DELETE') THEN
        INSERT INTO change_log(table_name, record_id, action)
        VALUES (TG_TABLE_NAME, OLD.id, 'DELETE');
        RETURN OLD;
    END IF;
END;
$$ LANGUAGE plpgsql;



CREATE TRIGGER trg_meta_data_changes
AFTER INSERT OR UPDATE OR DELETE ON meta_data
FOR EACH ROW
EXECUTE FUNCTION log_meta_data_changes();

-- created_at, updated_at

ALTER TABLE students
ADD COLUMN created_at TIMESTAMPTZ DEFAULT now(),
ADD COLUMN updated_at TIMESTAMPTZ DEFAULT now();


-- auto update updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = now();
   RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER set_timestamp
BEFORE UPDATE ON students
FOR EACH ROW
EXECUTE PROCEDURE update_updated_at_column();

-- age group check

ALTER TABLE students
ADD CONSTRAINT age_group_check CHECK (age_group BETWEEN 14 AND 100);

-- degree_levels dict

-- creating degree_levels table
CREATE TABLE degree_levels (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

-- levels names UKR
INSERT INTO degree_levels (name)
VALUES 
    ('Базова середня освіта'),          -- 5–9 класи
    ('Повна загальна середня освіта'),  -- 10–11 класи
    ('Бакалавр'),                       -- Вища освіта
    ('Магістр');                        -- Після бакалавра


-- adding NOT NULL until important fields

-- job_description д
ALTER TABLE jobs
ALTER COLUMN job_description SET NOT NULL;

-- field
ALTER TABLE education
ALTER COLUMN field SET NOT NULL;

-- meta_data
ALTER TABLE meta_data
ALTER COLUMN city_id SET NOT NULL;

-- UNIQUE

-- One student should not have the same job_description multiple times
ALTER TABLE jobs
ADD CONSTRAINT unique_student_job UNIQUE (student_id, job_description);

-- A unique student-city pair (the same student cannot be tied to the same city multiple times)
ALTER TABLE meta_data
ADD CONSTRAINT unique_student_city UNIQUE (st_id, city_id);

-- Education: A student must not have multiple identical records
ALTER TABLE education
ADD CONSTRAINT unique_education_per_student UNIQUE (student_id, field, institution, year_completed);
