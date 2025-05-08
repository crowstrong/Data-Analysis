-- === 1. Main reference tables ===

-- Students
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    gender TEXT CHECK (gender IN ('male', 'female','Чоловік','Жінка', 'other'))
);

-- Surveys
CREATE TABLE surveys (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Education (degree level)
CREATE TABLE degree_levels (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Majors / Professions / Skills / Learning Goals, etc.
CREATE TABLE majors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE learning_goals (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE jobs (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- === 2. Main metadata table (unified survey responses) ===

CREATE TABLE meta_data (
    student_id INTEGER REFERENCES students(id) ON DELETE CASCADE,
    survey_id INTEGER REFERENCES surveys(id) ON DELETE CASCADE,
    response_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    age INTEGER,
    city TEXT,
    country TEXT,
    degree_level_id INTEGER REFERENCES degree_levels(id),
    major_id INTEGER REFERENCES majors(id),
    current_salary NUMERIC,
    expected_salary NUMERIC,
    courses_last_year INTEGER,
    study_hours_per_day INTEGER,
    work_hours_per_day INTEGER,
    motivation TEXT,
    is_full_time BOOLEAN,
    PRIMARY KEY (student_id, survey_id)
);

-- === 3. Multiple-choice relationships (skills, goals, jobs, etc.) ===

CREATE TABLE student_skills (
    student_id INTEGER,
    survey_id INTEGER,
    skill_id INTEGER REFERENCES skills(id),
    PRIMARY KEY (student_id, survey_id, skill_id),
    FOREIGN KEY (student_id, survey_id) REFERENCES meta_data(student_id, survey_id) ON DELETE CASCADE
);

CREATE TABLE student_learning_goals (
    student_id INTEGER,
    survey_id INTEGER,
    goal_id INTEGER REFERENCES learning_goals(id),
    PRIMARY KEY (student_id, survey_id, goal_id),
    FOREIGN KEY (student_id, survey_id) REFERENCES meta_data(student_id, survey_id) ON DELETE CASCADE
);

CREATE TABLE student_jobs (
    student_id INTEGER,
    survey_id INTEGER,
    job_id INTEGER REFERENCES jobs(id),
    PRIMARY KEY (student_id, survey_id, job_id),
    FOREIGN KEY (student_id, survey_id) REFERENCES meta_data(student_id, survey_id) ON DELETE CASCADE
);

-- === 4. Education details (separate if multiple degrees are needed) ===
CREATE TABLE student_education (
    id SERIAL PRIMARY KEY,
    student_id INTEGER,
    survey_id INTEGER,
    degree_level_id INTEGER REFERENCES degree_levels(id),
    field TEXT,
    FOREIGN KEY (student_id, survey_id) REFERENCES meta_data(student_id, survey_id) ON DELETE CASCADE
);