SELECT * FROM `kidsfriendlyparis.Kids_friendly_data.normalized_table` LIMIT 10;

#Distribution of types across zip codes
SELECT 
  zipcode, 
  type, 
  COUNT(*) AS num_places
FROM `kidsfriendlyparis.Kids_friendly_data.normalized_table`
GROUP BY zipcode, type
ORDER BY zipcode, num_places DESC;


# Identify rows with null values
SELECT *
FROM `kidsfriendlyparis.Kids_friendly_data.normalized_table`
WHERE unique_id IS NULL
   OR name IS NULL
   OR adresse IS NULL
   OR zipcode IS NULL
   OR ville IS NULL
   OR type IS NULL;

# Places by city
SELECT 
    ville AS City,
    type AS Place_Type,
    name AS Place_Name,
    adresse AS Address,
    zipcode AS Zip_Code
FROM `kidsfriendlyparis.Kids_friendly_data.normalized_table`
ORDER BY ville, type;
