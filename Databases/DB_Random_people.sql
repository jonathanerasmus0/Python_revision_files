-- Create the database
CREATE DATABASE RandomPeopleDB;

-- Connect to the newly created database
\c RandomPeopleDB;

-- Create table for men
CREATE TABLE men (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

-- Create table for women
CREATE TABLE women (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    city VARCHAR(50)
);

-- Insert random data for men
INSERT INTO men (name, age, city)
SELECT 
    'Male' || generate_series,
    floor(random() * 70) + 18,  -- Generate random age between 18 and 87
    'City' || floor(random() * 10) + 1 -- Generate random city number between 1 and 10
FROM generate_series(1, 12);

-- Insert random data for women
INSERT INTO women (name, age, city)
SELECT 
    'Female' || generate_series,
    floor(random() * 70) + 18,  -- Generate random age between 18 and 87
    'City' || floor(random() * 10) + 1 -- Generate random city number between 1 and 10
FROM generate_series(1, 12);
