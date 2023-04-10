CREATE DATABASE dbcreditcard;

\c dbcreditcard;

-- Table User
CREATE TABLE IF NOT EXISTS users (
    id_user varchar(50) PRIMARY KEY,
    username varchar(60) UNIQUE NOT NULL,
    password varchar(300) NOT NULL,
    is_staff boolean NOT NULL
);

-- Table Card
CREATE TABLE IF NOT EXISTS card (
    id_card varchar(50) PRIMARY KEY,
    exp_date date NOT NULL,
    holder varchar(50) NOT NULL,
    number varchar(500) NOT NULL,
    cvv int,
    brand varchar(50)
);
