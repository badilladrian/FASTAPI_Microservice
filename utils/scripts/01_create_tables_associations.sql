DROP DATABASE IF EXISTS farmly;

CREATE DATABASE farmly WITH OWNER = root ENCODING = "UTF8" TABLESPACE = pg_default CONNECTION LIMIT = - 1;

\c farmly
-- SEQUENCE: public.addresses_id_seq
CREATE SEQUENCE IF NOT EXISTS public.addresses_id_seq
INCREMENT 1 START 1
MINVALUE 1
MAXVALUE 2147483647
CACHE 1;

-- Table: public.addresses
CREATE TABLE IF NOT EXISTS public.addresses (
    id integer NOT NULL DEFAULT nextval('addresses_id_seq'::regclass),
    country text COLLATE pg_catalog."default" NOT NULL,
    state text COLLATE pg_catalog."default",
    city text COLLATE pg_catalog."default",
    address1 text COLLATE pg_catalog."default",
    address2 text COLLATE pg_catalog."default",
    zipcode integer,
    CONSTRAINT addresses_pkey PRIMARY KEY (id)
);

-- SEQUENCE: public.users_id_seq

CREATE SEQUENCE IF NOT EXISTS public.users_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- Table: public.users
CREATE TABLE IF NOT EXISTS public.users (
    id integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    email text COLLATE pg_catalog."default" NOT NULL,
    username text COLLATE pg_catalog."default" NOT NULL,
    first_name text COLLATE pg_catalog."default" NOT NULL,
    last_name text COLLATE pg_catalog."default" NOT NULL,
    password text COLLATE pg_catalog."default" NOT NULL,
    phone text COLLATE pg_catalog."default",
    sharing text COLLATE pg_catalog."default" NOT NULL,
    what_share text COLLATE pg_catalog."default" NOT NULL,
    active boolean,
    created_date date,
    address1 text COLLATE pg_catalog."default",
    address2 text COLLATE pg_catalog."default",
    city text COLLATE pg_catalog."default",
    state text COLLATE pg_catalog."default",
    country text COLLATE pg_catalog."default",
    zipcode integer,
    CONSTRAINT pk_id PRIMARY KEY (id),
    CONSTRAINT unique_email UNIQUE (email),
    CONSTRAINT unique_username UNIQUE (username),
    CONSTRAINT chk_sharing CHECK (sharing = ANY (ARRAY['EO'::text, 'OC'::text, 'NO'::text])),
    CONSTRAINT chk_what_share CHECK (what_share = ANY (ARRAY['ET'::text, 'SC'::text, 'AA'::text]))
    );

-- SEQUENCE: public.yards_id_seq
CREATE SEQUENCE IF NOT EXISTS public.yards_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- Table: public.yards
CREATE TABLE IF NOT EXISTS public.yards (
    id integer NOT NULL DEFAULT nextval('yards_id_seq'::regclass),
    user_id integer NOT NULL,
    address_id integer NOT NULL,
    CONSTRAINT yards_pkey PRIMARY KEY (id),
    CONSTRAINT fk_address_id FOREIGN KEY (address_id) REFERENCES public.addresses (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES public.users (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION
);

-- SEQUENCE: public.beds_id_seq
CREATE SEQUENCE IF NOT EXISTS public.beds_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;


-- Table: public.beds
CREATE TABLE IF NOT EXISTS public.beds (
    id integer NOT NULL DEFAULT nextval('beds_id_seq'::regclass),
    yard_id integer NOT NULL,
    CONSTRAINT beds_pkey PRIMARY KEY (id),
    CONSTRAINT fk_yard_id FOREIGN KEY (yard_id) REFERENCES public.yards (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION
);


-- SEQUENCE: public.botanical_categories_id_seq
CREATE SEQUENCE IF NOT EXISTS public.botanical_categories_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;


-- Table: public.botanical_categories
CREATE TABLE IF NOT EXISTS public.botanical_categories (
    id integer NOT NULL DEFAULT nextval('botanical_categories_id_seq'::regclass),
    botanical_category text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT botanical_categories_pkey PRIMARY KEY (id));


-- SEQUENCE: public.plant_families_id_seq
CREATE SEQUENCE IF NOT EXISTS public.plant_families_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- Table: public.plant_families
CREATE TABLE IF NOT EXISTS public.plant_families (
    id integer NOT NULL DEFAULT nextval('plant_families_id_seq'::regclass),
    plant_family text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT plant_families_pkey PRIMARY KEY (id));

-- SEQUENCE: public.plants_id_seq
CREATE SEQUENCE IF NOT EXISTS public.plants_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- Table: public.plants
CREATE TABLE IF NOT EXISTS public.plants (
    id integer NOT NULL DEFAULT nextval('plants_id_seq'::regclass),
    plant text COLLATE pg_catalog."default" NOT NULL,
    plant_family_id integer,
    botanical_category_id integer,
    CONSTRAINT plants_pkey PRIMARY KEY (id),
    CONSTRAINT fk_botanical_category_id FOREIGN KEY (botanical_category_id) REFERENCES public.botanical_categories (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT fk_plant_family_id FOREIGN KEY (plant_family_id) REFERENCES public.plant_families (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION);


-- SEQUENCE: public.cultivars_id_seq
CREATE SEQUENCE IF NOT EXISTS public.cultivars_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- Table: public.cultivars
CREATE TABLE IF NOT EXISTS public.cultivars (
    id integer NOT NULL DEFAULT nextval('cultivars_id_seq'::regclass),
    cultivar text COLLATE pg_catalog."default" NOT NULL,
    look text COLLATE pg_catalog."default",
    flavor text COLLATE pg_catalog."default",
    ripe_color text COLLATE pg_catalog."default",
    shape text COLLATE pg_catalog."default",
    size text COLLATE pg_catalog."default",
    unripe_color text COLLATE pg_catalog."default",
    climate text COLLATE pg_catalog."default",
    planting_season text COLLATE pg_catalog."default",
    harvest_season text COLLATE pg_catalog."default",
    number_harvest_year integer,
    plant_id integer NOT NULL,
    category text COLLATE pg_catalog."default",
    display_name text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT cultivars_pkey PRIMARY KEY (id),
    CONSTRAINT fk_plant_id FOREIGN KEY (plant_id) REFERENCES public.plants (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION);

-- SEQUENCE: public.entry_groups_id_seq
CREATE SEQUENCE IF NOT EXISTS public.entry_groups_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- Table: public.entry_groups
CREATE TABLE IF NOT EXISTS public.entry_groups (
    id integer NOT NULL DEFAULT nextval('entry_groups_id_seq'::regclass),
    "group" text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT entry_groups_pkey PRIMARY KEY (id));


-- SEQUENCE: public.entry_types_id_seq
CREATE SEQUENCE IF NOT EXISTS public.entry_types_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- Table: public.entry_types
CREATE TABLE IF NOT EXISTS public.entry_types (
    id integer NOT NULL DEFAULT nextval('entry_types_id_seq'::regclass),
    type text COLLATE pg_catalog."default" NOT NULL,
    entry_group_id integer,
    CONSTRAINT entry_types_pkey PRIMARY KEY (id),
    CONSTRAINT fk_entry_group_id FOREIGN KEY (entry_group_id) REFERENCES public.entry_groups (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION);
-- SEQUENCE: public.journals_id_seq

-- SEQUENCE: public.plantings_id_seq
CREATE SEQUENCE IF NOT EXISTS public.plantings_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- Table: public.plantings
CREATE TABLE IF NOT EXISTS public.plantings (
    id integer NOT NULL DEFAULT nextval('plantings_id_seq'::regclass),
    cultivar_id integer NOT NULL,
    bed_id integer NOT NULL,
    description text COLLATE pg_catalog."default",
    planted_date date NOT NULL,
    CONSTRAINT plantings_pkey PRIMARY KEY (id),
    CONSTRAINT fk_bed_id FOREIGN KEY (bed_id) REFERENCES public.beds (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT fk_cultivar_id FOREIGN KEY (cultivar_id) REFERENCES public.cultivars (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION);

CREATE SEQUENCE IF NOT EXISTS public.journals_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- Table: public.journals
CREATE TABLE IF NOT EXISTS public.journals (
    id integer NOT NULL DEFAULT nextval('journals_id_seq'::regclass),
    planting_id integer NOT NULL,
    CONSTRAINT journals_pkey PRIMARY KEY (id),
    CONSTRAINT fk_planting_id FOREIGN KEY (planting_id) REFERENCES public.plantings (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION);


-- SEQUENCE: public.entries_id_seq
CREATE SEQUENCE IF NOT EXISTS public.entries_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

-- Table: public.entries
CREATE TABLE IF NOT EXISTS public.entries (
    id integer NOT NULL DEFAULT nextval('entries_id_seq'::regclass),
    entry_type_id integer NOT NULL,
    journal_id integer NOT NULL,
    datetime timestamp with time zone NOT NULL,
    description json NOT NULL,
    CONSTRAINT entries_pkey PRIMARY KEY (id),
    CONSTRAINT fk_entry_type_id FOREIGN KEY (entry_type_id) REFERENCES public.entry_types (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT fk_journal_id FOREIGN KEY (journal_id) REFERENCES public.journals (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION);


-- SEQUENCE: public.entries_id_seq
CREATE SEQUENCE IF NOT EXISTS public.entry_pictures_id_seq
    INCREMENT 1 START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;


-- Table: public.entry_pictures
CREATE TABLE IF NOT EXISTS public.entry_pictures (
    id integer NOT NULL DEFAULT nextval('entry_pictures_id_seq'::regclass),
    entry_id integer NOT NULL,
    picture bytea NOT NULL,
    CONSTRAINT entry_pictures_pkey PRIMARY KEY (id),
    CONSTRAINT fk_entry_id FOREIGN KEY (entry_id) REFERENCES public.entries (id) MATCH SIMPLE ON UPDATE NO ACTION ON DELETE NO ACTION);

  GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO farmly_user;
