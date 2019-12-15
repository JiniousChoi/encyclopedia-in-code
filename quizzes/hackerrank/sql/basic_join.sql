------------------------------------
-- author: jinchoiseoul@gmail.com --
------------------------------------


---- Asian Population
-- Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.
-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
-----------------------------------------------------------------------------------------------------------------------
-- [city]        [country]
-----------------------------------------------------------------------------------------------------------------------
-- id            code 
-- name          name
-- countrycode   continent
-- district      region
-- population    surfacearea 
--               indepyear 
--               population 
--               lifeexpectancy 
--               gnp 
--               gnpold 
--               localname 
--               governmentform 
--               headofstate 
--               capital 
--               code2 
-----------------------------------------------------------------------------------------------------------------------
SELECT SUM(CITY.POPULATION) FROM CITY JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE WHERE COUNTRY.CONTINENT = 'Asia';


---- African Cities
-- Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
-----------------------------------------------------------------------------------------------------------------------
-- [city]        [country]
-----------------------------------------------------------------------------------------------------------------------
-- id            code 
-- name          name
-- countrycode   continent
-- district      region
-- population    surfacearea 
--               indepyear 
--               population 
--               lifeexpectancy 
--               gnp 
--               gnpold 
--               localname 
--               governmentform 
--               headofstate 
--               capital 
--               code2 
-----------------------------------------------------------------------------------------------------------------------
SELECT CITY.NAME FROM CITY JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE WHERE COUNTRY.CONTINENT = 'Africa';


---- Average Population of Each Continent
-- Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent)
-- and their respective average city populations (CITY.Population) rounded down to the nearest integer.
-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
-- Do not include continents without cities in your output.
-----------------------------------------------------------------------------------------------------------------------
-- [city]        [country]
-----------------------------------------------------------------------------------------------------------------------
-- id            code 
-- name          name
-- countrycode   continent
-- district      region
-- population    surfacearea 
--               indepyear 
--               population 
--               lifeexpectancy 
--               gnp 
--               gnpold 
--               localname 
--               governmentform 
--               headofstate 
--               capital 
--               code2 
-----------------------------------------------------------------------------------------------------------------------
SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION))
FROM CITY JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
GROUP BY Country.CONTINENT;


---- The Report
-- Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark.
-- Ketty doesn't want the NAMES of those students who received a grade lower than 8.
-- The report must be in descending order by grade -- i.e. higher grades are entered first.
-- If there is more than one student with the same grade (8-10) assigned to them,
-- order those particular students by their name alphabetically.
-- Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order.
-- If there is more than one student with the same grade (1-7) assigned to them,
-- order those particular students by their marks in ascending order.
-- Sample Output:
   -- Maria 10 99
   -- Jane 9 81
   -- Julia 9 88 
   -- Scarlet 8 78
   -- NULL 7 63
   -- NULL 7 68
-------------------------------------------------------
-- [grades]      [students]
-------------------------------------------------------
-- Grade         ID 
-- Min_Mark      Name 
-- Max_Mark      Marks 
-------------------------------------------------------
SELECT if(GRADES.GRADE > 7, STUDENTS.NAME, NULL), GRADES.GRADE, STUDENTS.MARKS
FROM STUDENTS join GRADES
ON STUDENTS.MARKS BETWEEN GRADES.MIN_MARK AND GRADES.MAX_MARK
ORDER BY GRADE DESC, STUDENTS.NAME ASC, STUDENTS.MARKS ASC;

SELECT if(g.GRADE > 7, s.NAME, NULL), g.GRADE, s.MARKS
FROM STUDENTS s join GRADES g -- aliasing
ON s.MARKS  BETWEEN g.MIN_MARK AND g.MAX_MARK
ORDER BY GRADE DESC, s.NAME ASC, s.MARKS ASC;

SELECT if(g.GRADE > 7, s.NAME, NULL), g.GRADE, s.MARKS
FROM STUDENTS as s join GRADES as g -- aliasing
ON s.MARKS BETWEEN g.MIN_MARK AND g.MAX_MARK
ORDER BY GRADE DESC, s.NAME ASC, s.MARKS ASC;


---- Top Competitors
-- Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard!
-- Write a query to print the respective hacker_id and name of hackers who achieved full scores
-- for more than one challenge. Order your output in descending order by the total number of challenges
-- in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges,
-- then sort them by ascending hacker_id.
------------------------------------------------------------------
-- [challenges]     [difficulty]        [hackers]   [submissions] 
------------------------------------------------------------------
-- challenge_id     difficulty_level    hacker_id   submission_id
-- hacker_id        score               name        hacker_id
-- difficulty_level                                 challenge_id
--                                                  score
------------------------------------------------------------------
SELECT H.hacker_id, H.name
FROM Hackers H JOIN Submissions S ON H.hacker_id = S.hacker_id
     JOIN Challenges C ON S.challenge_id = C.challenge_id
     JOIN Difficulty D ON C.difficulty_level = D.difficulty_level
WHERE S.score = D.score -- filter only the full-scored submissions
GROUP BY H.hacker_id, H.name HAVING COUNT(S.hacker_id) > 1
ORDER BY COUNT(s.hacker_id) DESC, H.hacker_id ASC


---- Ollivander's Inventory
-- Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.
-- Hermione decides the best way to choose is by determining the minimum number of gold galleons needed
-- to buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed,
-- and power of the wands that Ron's interested in, sorted in order of descending power.
-- If more than one wand has same power, sort the result in order of descending age.
------------------------------------------------------------------------
-- [wands]         [wands_property]
------------------------------------------------------------------------
-- id              code
-- code            age
-- coins_needed    is_evil
-- power
------------------------------------------------------------------------
-- efficient: it joins three tables, only once
SELECT W.id, P.age, W.coins_needed, W.power
FROM wands W
JOIN wands_property P ON W.code = P.code
JOIN ( 
	SELECT PX.age, WX.power, MIN(WX.coins_needed) as min_coins
	FROM Wands WX JOIN Wands_Property PX ON WX.code = PX.code
	WHERE PX.is_evil = 0
	GROUP BY PX.age, WX.power) as X ON P.age = X.age and W.power = X.power
WHERE W.coins_needed = X.min_coins
ORDER BY W.power DESC, P.age DESC;

-- inefficient: it joins two tables, as many as COUNT(*)
SELECT W.id, P.age, W.coins_needed, W.power
FROM Wands W JOIN Wands_Property P ON W.code = P.code
WHERE P.is_evil = 0 and W.coins_needed = (
    SELECT min(W2.coins_needed)
    FROM Wands W2 JOIN Wands_Property P2 ON W2.code = P2.code
    WHERE P.age = P2.age and W.power = W2.power )
ORDER BY W.power DESC, P.age DESC;


---- Challenges
-- Julia asked her students to create some coding challenges. Write a query to print the hacker_id, name, and the total
-- number of challenges created by each student. Sort your results by the total number of challenges in descending order.
-- If more than one student created the same number of challenges, then sort the result by hacker_id.
-- If more than one student created the same number of challenges and the count is less than the maximum number of
-- challenges created, then exclude those students from the result.
----------------------------------------------------------------------------
-- [challenges]    [hackers]
----------------------------------------------------------------------------
-- challenge_id    hacker_id
-- hacker_id       name
----------------------------------------------------------------------------
SELECT tbl_a.hid, tbl_a.hname, tbl_a.cnt
FROM (
    SELECT h.hacker_id as hid, h.name as hname, count(c.challenge_id) as cnt
    FROM Hackers h JOIN Challenges c
    ON h.hacker_id = c.hacker_id
    GROUP BY hid, hname) as tbl_a
WHERE tbl_a.cnt = (
			SELECT max(tbl.cnt)
			FROM (
				SELECT h.hacker_id, count(*) as cnt
				FROM Hackers h JOIN Challenges c
				ON h.hacker_id = c.hacker_id
				GROUP BY h.hacker_id) as tbl)
	  or tbl_a.cnt IN (
			SELECT tbl.cnt
			FROM (
				SELECT h.hacker_id as hid2, count(*) as cnt
				FROM Hackers h JOIN Challenges c
				ON h.hacker_id = c.hacker_id
				GROUP BY h.hacker_id) as tbl
			GROUP BY tbl.cnt HAVING count(tbl.cnt) = 1)
ORDER BY tbl_a.cnt DESC, tbl_a.hid ASC


---- Contest Leaderboard
-- You did such a great job helping Julia with her last coding contest challenge that she wants you to work on this one,
-- too! The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print
-- the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved
-- the same total score, then sort the result by ascending hacker_id.
-- Exclude all hackers with a total score of 0 from your result.
---------------------------------------------------------------------
-- [hackers]    [submissions]
---------------------------------------------------------------------
-- hacker_id    submission_id
-- name         hacker_id
--              challenge_id
--              score
---------------------------------------------------------------------
-- efficient: 2 temp tables
select s1.hacker_id, h.name, SUM(s1.max_score) as tot
from hackers h join (
    select challenge_id, hacker_id, max(score) as max_score
    from submissions
    group by challenge_id, hacker_id) s1
on h.hacker_id = s1.hacker_id
group by s1.hacker_id, h.name having tot > 0
order by tot desc, s1.hacker_id asc;

-- inefficient: 3 temp tables
select h.hacker_id, h.name, s2.tot
from hackers h JOIN (
     select s1.hacker_id, SUM(s1.max_score) as tot
     from (
         select challenge_id, hacker_id, max(score) as max_score
         from submissions
         group by challenge_id, hacker_id) s1
     group by s1.hacker_id) s2
     on h.hacker_id = s2.hacker_id
where s2.tot > 0
order by s2.tot desc, h.hacker_id asc;

