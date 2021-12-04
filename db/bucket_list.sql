DROP TABLE places_of_interest;
DROP TABLE cities;
DROP TABLE countries;

CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capital VARCHAR(255),
    population INT,
    visited BOOLEAN
);

CREATE TABLE cities(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    places_of_interest TEXT,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE places_of_interest(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    information TEXT,
    visited BOOLEAN,
    city_id INT REFERENCES cities(id) ON DELETE CASCADE
)