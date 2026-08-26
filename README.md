# Background

SQL sublanguage: DDL (Data Definition Language)

A primary key is a constraint that labels a column as the unique identifier for a record in the table. Primary
keys are UNIQUE and NOT NULL implicitly.

CREATE TABLE site_user (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username varchar(100),
password varchar(100)
);

The `id` column above will autogenerate a unique number for us, and is marked as the primary key.

## Problem 1

Create a table in `problem1.sql` called `song` with 3 columns: `id`, `title`, and `artist`. The `id` column
should be the primary key.

| id  | title            | artist       |
| --- | ---------------- | ------------ |
| 1   | Let it be        | Beatles      |
| 2   | Hotel California | Eagles       |
| 3   | Kashmir          | Led Zeppelin |
