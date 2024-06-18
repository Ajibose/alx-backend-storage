-- A script that contains Query to calculate the total number of fans
-- grouped by origin and display the results in descending order of fan count.
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC
