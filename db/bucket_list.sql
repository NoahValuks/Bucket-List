DROP TABLE countries;
DROP TABLE cities;

CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capital VARCHAR(255),
    popular INT,
    visited BOOLEAN
);

CREATE TABLE cities(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    visited BOOLEAN,
    places_of_interest TEXT,
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);