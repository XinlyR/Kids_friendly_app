CREATE DATABASE kids_friendly_db_new;
USE kids_friendly_db_new;
CREATE TABLE detailed_places (

    name VARCHAR(255),

    type VARCHAR(255),

    vicinity VARCHAR(255),

    formatted_address VARCHAR(255),

    website VARCHAR(255),

    phone_number VARCHAR(50),

    opening_hours TEXT,

    reviews TEXT,

    zipcode INT,

    unique_id VARCHAR(255),

    type_id VARCHAR(255),

    df_id VARCHAR(255),

    df_unique_id VARCHAR(255),

    PRIMARY KEY (unique_id)

);



CREATE TABLE parks_with_playground (

    unique_id VARCHAR(255) PRIMARY KEY,

    nom_espace_vert VARCHAR(255),

    typologie_espace_vert VARCHAR(255),

    categorie VARCHAR(255),

    zipcode INT,

    surface_calculee VARCHAR(50),

    superficie_totale_reelle VARCHAR(50),

    perimetre VARCHAR(50),

    ouverture_24h_24h VARCHAR(50),

    site_villes VARCHAR(255),

    geo_shape TEXT,

    url_plan VARCHAR(255),

    geo_point VARCHAR(255),

    adresse VARCHAR(255),

    type VARCHAR(255),

    type_id VARCHAR(255),

    df_id VARCHAR(255),

    df_unique_id VARCHAR(255)

);



CREATE TABLE faire (

    unique_id INT PRIMARY KEY,

    url VARCHAR(255),

    titre VARCHAR(255),

    chapeau TEXT,

    description TEXT,

    description_date TEXT,

    nom_lieu VARCHAR(255),

    adresse_lieu VARCHAR(255),

    zipcode VARCHAR(10),

    ville VARCHAR(255),

    coordonnees_geographiques VARCHAR(255),

    type_prix VARCHAR(50),

    groupe VARCHAR(50),

    locale VARCHAR(50),

    month_debut VARCHAR(50),

    year_debut INT,

    month_fin VARCHAR(50),

    year_fin INT,

    type VARCHAR(255),

    type_id VARCHAR(255),

    df_id VARCHAR(255),

    df_unique_id VARCHAR(255)

);



CREATE TABLE paris_data (

    arrondissement INT,

    name_arrondissement VARCHAR(255),

    surface_ha VARCHAR(50),

    population_2020 INT,

    density_2021_hab_km2 INT,

    zipcode VARCHAR(10),

    PRIMARY KEY (arrondissement)

);



CREATE TABLE `data` (

    name VARCHAR(255),

    vicinity VARCHAR(255),

    formatted_address VARCHAR(255),

    website VARCHAR(255),

    phone_number VARCHAR(50),

    opening_hours TEXT,

    reviews TEXT,

    latitude FLOAT,

    longitude FLOAT,

    proche_park BOOLEAN,

    kids_mentions_count INT,

    zipcode INT,

    unique_id VARCHAR(255) PRIMARY KEY,

    kids_friendly BOOLEAN,

    type VARCHAR(255),

    type_id VARCHAR(255),

    df_id VARCHAR(255),

    df_unique_id VARCHAR(255)

);





CREATE TABLE kf_places_paris (

    name VARCHAR(255),

    vicinity VARCHAR(255),

    type VARCHAR(255),

    latitude FLOAT,

    longitude FLOAT,

    zipcode VARCHAR(10),

    unique_id VARCHAR(255) PRIMARY KEY,

    type_id VARCHAR(255),

    df_id VARCHAR(255),

    df_unique_id VARCHAR(255)

);
SELECT * FROM `data`;
SELECT * FROM detailed_places;
SELECT * FROM faire;
SELECT * FROM kf_places_paris;
SELECT * FROM paris_data;
SELECT * FROM parks_with_playground;
ALTER TABLE faire DROP COLUMN url;
ALTER TABLE faire DROP COLUMN titre;
ALTER TABLE faire DROP COLUMN chapeau;
ALTER TABLE faire DROP COLUMN description_date;
ALTER TABLE faire DROP COLUMN `description`;
ALTER TABLE faire DROP COLUMN nom_lieu;
ALTER TABLE faire DROP COLUMN adresse_lieu;
ALTER TABLE faire DROP COLUMN ville;
ALTER TABLE faire DROP COLUMN coordonnees_geographiques;
ALTER TABLE faire DROP COLUMN type_prix;
ALTER TABLE faire DROP COLUMN groupe;
ALTER TABLE faire DROP COLUMN month_debut;
ALTER TABLE faire DROP COLUMN month_fin;
ALTER TABLE faire DROP COLUMN year_fin;
ALTER TABLE faire DROP COLUMN year_debut;

ALTER TABLE detailed_places MODIFY zipcode VARCHAR(10);
ALTER TABLE parks_with_playground MODIFY zipcode VARCHAR(10);
ALTER TABLE faire MODIFY zipcode VARCHAR(10);
ALTER TABLE data MODIFY zipcode VARCHAR(10);
ALTER TABLE kf_places_paris MODIFY zipcode VARCHAR(10);

ALTER TABLE paris_data 
ADD COLUMN arrondissement INT NOT NULL FIRST;
DROP TABLE paris_data;
CREATE TABLE paris_data (
    arrondissement INT NOT NULL,
    name_arrondissement VARCHAR(255),
    surface_ha VARCHAR(50),
    population_2020 INT,
    density_2021_hab_km2 INT,
    zipcode VARCHAR(10),
    PRIMARY KEY (arrondissement),
    UNIQUE (zipcode)
);

INSERT INTO paris_data (arrondissement, name_arrondissement, surface_ha, population_2020, density_2021_hab_km2, zipcode)
VALUES
(1,'Louvre','183','15919','8699','75001'),
(2,'Bourse','99',	'21119',	'21332',	'75002'),
(3,'Temple',	'117',	'32793',	'28028',	'75003'),
(4,'Hotel de ville',	'160',	'28324',	'17702',	'75004'),
(5,'Pantheon', 	'254',	'56841',	'22378',	'75005'),
(6,'Luxembourg',	'215',	'40209',	'18702',	'75006'),
(7,'Palais-Bourbon',	'409',	'47947',	'11723',	'75007'),
(8,'Elysee',	'388',	'35123',	'9052',	'75008'),
(9,'Opera',	'218',	'58951',	'27042',	'75009'),
(10,'Enclos saint laurent',	'289',	'83543',	'28908',	'75010'),
(11,'Popincourt',	'367',	'142583',	'38851',	'75011'),
(12,'Reuilly',	'637',	'142340',	'22594',	'75012'),
(13,'Gobelins',	'715',	'178350',	'24944',	'75013'),
(14,'Observatoire',	'564',	'136368',	'24179',	'75014'),
(15,'Vaugirard',	'848',	'227746',	'26857',	'75015'),
(16,'Passy',	'791',	'165487',	'20921',	'75016'),
(17,'Batignolles',	'567',	'164413',	'28997',	'75017'),
(18,'Butte-Montmartre',	'601',	'188446',	'31355',	'75018'),
(19,'Buttes-Chaumont',	'679',	'181616',	'26748',	'75019'),
(20,'Menilmontant',	'598',	'189805',	'31740',	'75020');

INSERT INTO paris_data (arrondissement, zipcode)
SELECT zipcode AS arrondissement, zipcode
FROM detailed_places
WHERE zipcode NOT IN (SELECT zipcode FROM paris_data);

ALTER TABLE detailed_places 
ADD CONSTRAINT fk_detailed_places_zipcode
FOREIGN KEY (zipcode) REFERENCES paris_data(zipcode);

ALTER TABLE kf_places_paris 
ADD CONSTRAINT fk_kf_places_zipcode
FOREIGN KEY (zipcode) REFERENCES paris_data(zipcode);

#cleaning zipcode espaces
SET SQL_SAFE_UPDATES = 0;
UPDATE faire
SET zipcode = TRIM(zipcode);
SET SQL_SAFE_UPDATES = 1;

SET SQL_SAFE_UPDATES = 0;
UPDATE faire
SET zipcode = 
    CASE 
        WHEN zipcode = '7014' THEN '75014'
        WHEN zipcode = '79019' THEN '75019'
        WHEN zipcode = '76013' THEN '75013'
        ELSE zipcode
    END
WHERE zipcode IN ('7014', '79019', '76013');
SET SQL_SAFE_UPDATES = 1;

SET SQL_SAFE_UPDATES = 0;
UPDATE faire
SET zipcode = 
    CASE 
        WHEN zipcode = '93300 Aube' THEN '93300'
        WHEN zipcode = '93 200' THEN '93200'
        WHEN zipcode = '75 004' THEN '75004'
        ELSE zipcode
    END
WHERE zipcode IN ('93300 Aube', '93 200', '75 004');
SET SQL_SAFE_UPDATES = 1;

INSERT INTO paris_data (zipcode, arrondissement, name_arrondissement)
SELECT DISTINCT zipcode, zipcode AS arrondissement, 'Unknown' AS name_arrondissement
FROM faire
WHERE zipcode NOT IN (SELECT zipcode FROM paris_data);

ALTER TABLE faire 
ADD CONSTRAINT fk_faire_zipcode
FOREIGN KEY (zipcode) REFERENCES paris_data(zipcode);

INSERT INTO paris_data (zipcode, arrondissement, name_arrondissement)
SELECT DISTINCT zipcode, zipcode AS arrondissement, 'Unknown' AS name_arrondissement
FROM `data`
WHERE zipcode NOT IN (SELECT zipcode FROM paris_data);

ALTER TABLE `data` 
ADD CONSTRAINT fk_data_zipcode
FOREIGN KEY (zipcode) REFERENCES paris_data(zipcode);

ALTER TABLE parks_with_playground 
ADD CONSTRAINT fk_parks_zipcode
FOREIGN KEY (zipcode) REFERENCES paris_data(zipcode);

CREATE TABLE faire_events (
    unique_id INT PRIMARY KEY,
    url VARCHAR(255),
    titre TEXT,
    `description` TEXT,
    nom_lieu TEXT,
    adresse_lieu VARCHAR(255),
    zipcode VARCHAR(10),
    ville VARCHAR(255),
    coordonnees_geographiques VARCHAR(255),
    type_prix VARCHAR(50),
    type_acces VARCHAR(50),
    audience VARCHAR(50),
    locale VARCHAR(50),
    month_debut VARCHAR(50),
    year_debut INT,
    month_fin VARCHAR(50),
    year_fin INT,
    `type` VARCHAR(50),
    type_id VARCHAR(50),
    df_id VARCHAR(50),
    df_unique_id VARCHAR(50),
    CONSTRAINT fk_faire_events_zipcode FOREIGN KEY (zipcode) REFERENCES paris_data(zipcode)
);
ALTER TABLE faire_events MODIFY audience VARCHAR(255);
DROP TABLE faire;

CREATE TABLE `type` (
    type_id VARCHAR(255) PRIMARY KEY,
    `type` VARCHAR(255) NOT NULL,
    zipcode VARCHAR(10),
    CONSTRAINT fk_type_zipcode FOREIGN KEY (zipcode) REFERENCES paris_data(zipcode)
);

CREATE TABLE parks (
    unique_id VARCHAR(255) PRIMARY KEY,
    name_park VARCHAR(255),
    typologie_espace_vert VARCHAR(255),
    categorie VARCHAR(255),
    zipcode VARCHAR(10),
    ouverture_24h_24h VARCHAR(50),
    url_plan VARCHAR(255),
    geo_point VARCHAR(255),
    adresse VARCHAR(255),
    `type` VARCHAR(255),
    type_id VARCHAR(255),
    df_id VARCHAR(255),
    df_unique_id VARCHAR(255),
    CONSTRAINT fk_parks_zipcode_new FOREIGN KEY (zipcode) REFERENCES paris_data(zipcode),
    CONSTRAINT fk_parks_type_id FOREIGN KEY (type_id) REFERENCES `type`(type_id));
    
INSERT INTO `type` (type_id, `type`, zipcode)
SELECT DISTINCT type_id, 'Unknown' AS `type`, NULL AS zipcode
FROM detailed_places
WHERE type_id NOT IN (SELECT type_id FROM `type`);

INSERT INTO `type` (type_id, `type`, zipcode)
SELECT DISTINCT type_id, `type`, NULL AS zipcode
FROM `data`
WHERE type_id NOT IN (SELECT type_id FROM `type`);

INSERT INTO `type` (type_id, `type`, zipcode)
SELECT DISTINCT type_id, 'Unknown' AS `type`, NULL AS zipcode
FROM faire_events
WHERE type_id NOT IN (SELECT type_id FROM `type`);

INSERT INTO `type` (type_id, `type`, zipcode)
SELECT DISTINCT type_id, 'Unknown' AS `type`, zipcode
FROM parks
WHERE type_id NOT IN (SELECT type_id FROM `type`);

SET SQL_SAFE_UPDATES = 0;
UPDATE `type`
SET `type` = CASE
    WHEN type_id LIKE 'Ev-%' THEN 'Event'
    WHEN type_id LIKE 'Re-%' THEN 'Restaurant'
    WHEN type_id LIKE 'Fo-%' THEN 'Food Market'
    ELSE `type`  -- Garder la valeur existante pour les autres
END
WHERE `type` = 'Unknown';
SET SQL_SAFE_UPDATES = 1;

SET SQL_SAFE_UPDATES = 0;
UPDATE `type`
SET zipcode = RIGHT(type_id, 5)
WHERE zipcode IS NULL AND RIGHT(type_id, 5) REGEXP '^[0-9]{5}$';
SET SQL_SAFE_UPDATES = 1;

ALTER TABLE detailed_places 
ADD CONSTRAINT fk_detailed_places_type_id
FOREIGN KEY (type_id) REFERENCES `type`(type_id);

ALTER TABLE `data` 
ADD CONSTRAINT fk_data_type_id
FOREIGN KEY (type_id) REFERENCES `type`(type_id);

ALTER TABLE faire_events 
ADD CONSTRAINT fk_faire_events_type_id
FOREIGN KEY (type_id) REFERENCES `type`(type_id);
DROP TABLE parks_with_playground;

#Create new table to centralized the all tables on type
CREATE TABLE centralized_types (
    unique_id VARCHAR(255) PRIMARY KEY,
    type_id VARCHAR(255),
    `type` VARCHAR(255),
    `name` VARCHAR(255),
    arrondissement VARCHAR(255),
    zipcode VARCHAR(10)
);

INSERT INTO centralized_types (unique_id, type_id, `type`, `name`, arrondissement, zipcode)
SELECT 
    d.unique_id,
    d.type_id,
    d.`type`,
    d.name,
    pd.name_arrondissement,
    d.zipcode
FROM `data` d
LEFT JOIN paris_data pd ON d.zipcode = pd.zipcode;

#2 detailed places

INSERT INTO centralized_types (unique_id, type_id, `type`, `name`, arrondissement, zipcode)
SELECT 
    dp.unique_id,
    dp.type_id,
    dp.`type`,
    dp.name,
    pd.name_arrondissement,
    dp.zipcode
FROM detailed_places dp
LEFT JOIN paris_data pd ON dp.zipcode = pd.zipcode
ON DUPLICATE KEY UPDATE
    type_id = dp.type_id,
    `type` = dp.`type`,
    `name` = dp.name,
    arrondissement = pd.name_arrondissement,
    zipcode = dp.zipcode;


#3 kf_places_paris
INSERT INTO centralized_types (unique_id, type_id, `type`, `name`, arrondissement, zipcode)
SELECT 
    kp.unique_id,
    kp.type_id,
    kp.`type`,
    kp.name,
    pd.name_arrondissement,
    kp.zipcode
FROM kf_places_paris kp
LEFT JOIN paris_data pd ON kp.zipcode = pd.zipcode;

#4faire_events
INSERT INTO centralized_types (unique_id, type_id, `type`, `name`, arrondissement, zipcode)
SELECT 
    fe.unique_id,
    fe.type_id,
    fe.`type`,
    fe.titre AS name,
    pd.name_arrondissement,
    fe.zipcode
FROM faire_events fe
LEFT JOIN paris_data pd ON fe.zipcode = pd.zipcode;

#5 parks non
INSERT INTO centralized_types (unique_id, type_id, `type`, `name`, arrondissement, zipcode)
SELECT 
    p.unique_id,
    p.type_id,
    p.`type`,
    p.name_park AS name,
    pd.name_arrondissement,
    p.zipcode
FROM parks p
LEFT JOIN paris_data pd ON p.zipcode = pd.zipcode
ON DUPLICATE KEY UPDATE
    type_id = p.type_id,
    `type` = p.`type`,
    `name` = p.name_park,
    arrondissement = pd.name_arrondissement,
    zipcode = p.zipcode;

#To get relations in centralized_types    
INSERT INTO `type` (type_id, `type`, zipcode)
SELECT DISTINCT type_id, 'Playground', NULL
FROM centralized_types
WHERE type_id NOT IN (SELECT type_id FROM `type`);

SET SQL_SAFE_UPDATES = 0;
UPDATE `type`
SET zipcode = RIGHT(type_id, 5)
WHERE zipcode IS NULL AND RIGHT(type_id, 5) REGEXP '^[0-9]{5}$';
SET SQL_SAFE_UPDATES = 1;

ALTER TABLE centralized_types
ADD CONSTRAINT fk_centralized_type_id
FOREIGN KEY (type_id) REFERENCES type(type_id);

ALTER TABLE centralized_types
ADD CONSTRAINT fk_centralized_zipcode
FOREIGN KEY (zipcode) REFERENCES paris_data(zipcode);  



#Querys for the analysis :

#How many restaurants , events and parcs by name_arrondissement :

SELECT pd.name_arrondissement,
       COUNT(DISTINCT dp.unique_id) AS restaurant_count,
       COUNT(DISTINCT f.unique_id) AS event_count,
       COUNT(DISTINCT p.unique_id) AS park_count
FROM paris_data pd
LEFT JOIN detailed_places dp ON pd.zipcode = dp.zipcode
LEFT JOIN faire_events f ON pd.zipcode = f.zipcode
LEFT JOIN parks p ON pd.zipcode = p.zipcode
WHERE pd.zipcode BETWEEN '75001' AND '75020'
GROUP BY pd.name_arrondissement;

#Name and number actvities by name_arrondissement
SELECT 
    pd.name_arrondissement AS Arrondissement,
    t.`type` AS Type,
    COUNT(DISTINCT dp.unique_id) AS Total
FROM detailed_places dp
JOIN `type` t ON dp.type_id = t.type_id
JOIN paris_data pd ON dp.zipcode = pd.zipcode
GROUP BY pd.name_arrondissement, t.`type`
ORDER BY pd.name_arrondissement, Total DESC;

#Top 5 restaurants by number of reviews
SELECT 
    dp.name AS Restaurant,
    dp.formatted_address AS Adresse,
    dp.reviews AS Avis,
    dp.zipcode AS Zipcode,
    COUNT(reviews) AS Nombre_Avis
FROM detailed_places dp
JOIN `type` t ON dp.type_id = t.type_id
WHERE t.`type` = 'Restaurant'
GROUP BY dp.name, dp.formatted_address, dp.reviews, dp.zipcode
ORDER BY Nombre_Avis DESC
LIMIT 5;

#TOP 10 EVENEMENTS BY ARRONDISSEMENT
SELECT 
    fe.titre AS Event,
    fe.adresse_lieu AS Adresse,
    fe.ville AS Ville,
    fe.month_debut AS Mois_Debut,
    fe.year_debut AS Annee_Debut,
    fe.month_fin AS Mois_Fin,
    fe.year_fin AS Annee_Fin
FROM faire_events fe
JOIN paris_data pd ON fe.zipcode = pd.zipcode
WHERE fe.year_debut >= 2023
ORDER BY fe.year_debut DESC, fe.month_debut DESC
LIMIT 10;

SELECT 
    pd.name_arrondissement AS Arrondissement,
    pd.density_2021_hab_km2 AS Densite_Hab,
    COUNT(DISTINCT dp.unique_id) + COUNT(DISTINCT fe.unique_id) + COUNT(DISTINCT p.unique_id) AS Total_Entites
FROM paris_data pd
LEFT JOIN detailed_places dp ON pd.zipcode = dp.zipcode
LEFT JOIN faire_events fe ON pd.zipcode = fe.zipcode
LEFT JOIN parks p ON pd.zipcode = p.zipcode
GROUP BY pd.name_arrondissement, pd.density_2021_hab_km2
ORDER BY Total_Entites DESC;

#Top 5 of numbers of parks and restaurants by arrondissement
SELECT 
    pd.name_arrondissement AS Arrondissement,
    COUNT(DISTINCT p.unique_id) AS Nombre_Parcs,
    COUNT(DISTINCT dp.unique_id) AS Nombre_Restaurants
FROM paris_data pd
LEFT JOIN parks p ON pd.zipcode = p.zipcode
LEFT JOIN detailed_places dp ON pd.zipcode = dp.zipcode
JOIN `type` t ON dp.type_id = t.type_id AND t.`type` = 'Restaurant'
GROUP BY pd.name_arrondissement
ORDER BY (Nombre_Parcs + Nombre_Restaurants) DESC
LIMIT 5;

#Events by acces type and price
SELECT 
    fe.type_acces AS Type_Acces,
    fe.type_prix AS Type_Prix,
    COUNT(fe.unique_id) AS Total_Events
FROM faire_events fe
GROUP BY fe.type_acces, fe.type_prix
ORDER BY Total_Events DESC;

#Numbers of Events and Parks by most tourist arrondissement
SELECT 
    pd.name_arrondissement AS Arrondissement,
    COUNT(DISTINCT p.unique_id) AS Total_Parcs,
    COUNT(DISTINCT fe.unique_id) AS Total_Events
FROM paris_data pd
LEFT JOIN parks p ON pd.zipcode = p.zipcode
LEFT JOIN faire_events fe ON pd.zipcode = fe.zipcode
WHERE pd.zipcode IN ('75001', '75004', '75008', '75016', '75018')
GROUP BY pd.name_arrondissement
ORDER BY Total_Events DESC, Total_Parcs DESC;

#Numbers of Events and Parks by most populous arrondissement
SELECT 
    pd.name_arrondissement AS Arrondissement,
    COUNT(DISTINCT p.unique_id) AS Total_Parcs,
    COUNT(DISTINCT fe.unique_id) AS Total_Events
FROM paris_data pd
LEFT JOIN parks p ON pd.zipcode = p.zipcode
LEFT JOIN faire_events fe ON pd.zipcode = fe.zipcode
WHERE pd.zipcode IN ('75013', '75014', '75015', '75016', '75017','75018','75019','75020')
GROUP BY pd.name_arrondissement
ORDER BY Total_Events DESC, Total_Parcs DESC;

#Number of restaurants labeled "kidsfriendly" by arrondissement
SELECT 
    pd.zipcode AS Arrondissement,
    COUNT(dp.unique_id) AS Nombre_Restaurants
FROM detailed_places dp
JOIN `type` t ON dp.type_id = t.type_id
JOIN paris_data pd ON dp.zipcode = pd.zipcode
WHERE t.`type` = 'Restaurant'
GROUP BY pd.zipcode
ORDER BY Nombre_Restaurants DESC;

#Type of place by arrondissement
SELECT 
    pd.zipcode AS Arrondissement,
    t.`type` AS Type,
    COUNT(dp.unique_id) AS Nombre_Entites
FROM detailed_places dp
JOIN `type` t ON dp.type_id = t.type_id
JOIN paris_data pd ON dp.zipcode = pd.zipcode
GROUP BY pd.zipcode, t.`type`
ORDER BY pd.zipcode, Nombre_Entites DESC;

#Number of differents activities by arrondissement
SELECT 
    pd.zipcode AS Arrondissement,
    pd.population_2020 AS Number_Habitants,
    COUNT(CASE WHEN ct.`type` = 'Restaurant' THEN ct.unique_id END) AS Number_Restaurants,
    COUNT(CASE WHEN ct.`type` = 'Event' THEN ct.unique_id END) AS Number_Events,
    COUNT(CASE WHEN ct.`type` = 'Park' THEN ct.unique_id END) AS Number_Parks,
    COUNT(CASE WHEN ct.`type` = 'Museum' THEN ct.unique_id END) AS Number_Museums,
    COUNT(CASE WHEN ct.`type` = 'Zoo' THEN ct.unique_id END) AS Number_Zoos,
    COUNT(ct.unique_id) AS Nombre_Total_Activites
FROM paris_data pd
LEFT JOIN centralized_types ct ON pd.zipcode = ct.zipcode
GROUP BY pd.zipcode, pd.population_2020
ORDER BY Number_Habitants DESC;

#Relations tables
SELECT 
    table_name, 
    column_name, 
    constraint_name, 
    referenced_table_name, 
    referenced_column_name
FROM information_schema.KEY_COLUMN_USAGE
WHERE referenced_table_name IS NOT NULL
AND table_schema = 'kids_friendly_db_new';

#Export tables
SHOW VARIABLES LIKE 'secure_file_priv';
SELECT * FROM centralized_types
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/centralized_types.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM `data`
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/data.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM detailed_places
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/detailed_places.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM faire_events
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/faire_events.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM kf_places_paris
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/kf_places_paris.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM paris_data
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/paris_data.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM parks
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/parks.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

SELECT * FROM `type`
INTO OUTFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/type.csv'
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n';


