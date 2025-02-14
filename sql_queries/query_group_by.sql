-- Group by years published
SELECT
    CASE
        WHEN year_published < 1930 THEN 'Before 1930'
        WHEN year_published BETWEEN 1931 AND 1940 THEN '1931-1940'
        WHEN year_published BETWEEN 1941 AND 1950 THEN '1941-1950'
        WHEN year_published > 1950 THEN 'After 1950'
    END AS year_range,
    COUNT(*) AS books_count
FROM books
GROUP BY year_range
ORDER BY year_range;