create database pet_pie_hotel

CREATE TABLE owners (
    "id" SERIAL PRIMARY KEY,
    "name" VARCHAR(80) NOT NULL 
);

CREATE TABLE pets (
    "id" SERIAL PRIMARY KEY,
    "pet" VARCHAR(80) NOT NULL,
    "breed" VARCHAR(80) NOT NULL,
    "color" VARCHAR(80) NOT NULL,
    "checked_in" BOOLEAN default FALSE,
    "checked_in_date" DATE,
    "owner_id" INT references "owners"
);

INSERT INTO "owners" ("name")
VALUES ('testUser');