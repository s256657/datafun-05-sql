-- Inner join 
SELECT first, title
FROM authors
INNER JOIN books
ON authors.author_id = books.author_id;