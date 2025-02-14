-- Count number of books
SELECT COUNT(*) FROM books;

-- Show first published book
SELECT MIN(year_published) FROM books

-- Show last published book
SELECT MAX(year_published) FROM books