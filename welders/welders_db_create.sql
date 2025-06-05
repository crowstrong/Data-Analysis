-- 1. Cities
CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

-- 2. Qualifications
CREATE TABLE qualifications (
    id SERIAL PRIMARY KEY,
    level INTEGER UNIQUE NOT NULL CHECK (level BETWEEN 1 AND 6)
);

-- 3. Skills
CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    code TEXT UNIQUE NOT NULL,         
    description TEXT NOT NULL          
);

-- 4. Welders
CREATE TABLE welders (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    gender TEXT,
    birth_date DATE NOT NULL,
    city_id INTEGER REFERENCES cities(id),
    qualification_id INTEGER REFERENCES qualifications(id),
    experience_years INTEGER,
    phone_number TEXT UNIQUE,
    email TEXT UNIQUE,
    is_available BOOLEAN,
    created_at TIMESTAMP DEFAULT now()
);

-- 5. welder_skills (many-to-many link)
CREATE TABLE welder_skills (
    welder_id INTEGER REFERENCES welders(id) ON DELETE CASCADE,
    skill_id INTEGER REFERENCES skills(id) ON DELETE CASCADE,
    PRIMARY KEY (welder_id, skill_id)
);
