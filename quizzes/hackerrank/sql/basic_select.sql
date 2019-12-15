---- Revising the Select Query I
-- Query all columns for all American cities in CITY with populations larger than 100000.
-- The CountryCode for America is USA. 
select * from CITY where COUNTRYCODE = 'USA' and POPULATION > 100000;

---- Revising the Select Query II
-- Query the names of all American cities in CITY with populations larger than 120000.
-- The CountryCode for America is USA.
select NAME from CITY where COUNTRYCODE = 'USA' and POPULATION > 120000;

---- Select All
-- Query all columns (attributes) for every row in the CITY table.
select * from CITY;

---- Select By ID
-- Query all columns for a city in CITY with the ID 1661.
select * from CITY where ID=1661;

---- Japanese Cities' Attributes
-- Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
select * from CITY where COUNTRYCODE='JPN';

---- Japanese Cities' Names
-- Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT NAME FROM CITY WHERE COUNTRYCODE='JPN';
