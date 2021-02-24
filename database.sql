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
VALUES ('Gimli'), ('Gandalf'), ('Frodo'), ('Sam');

INSERT INTO "pets" ("pet", "breed", "color", "owner_id", "checked_in_date")
VALUES ('Bones', 'Cat', 'White', '2'), ('Chonk', 'Cat', 'Brown', '2'), ('GoodBoi', 'Doge', 'Black', '3'), ('GoodLawd', 'Snake', 'Green', '4')

UPDATE "pets" SET "checked_in" = TRUE, "checked_in_date" = '2021-02-21'
WHERE "id" = 2