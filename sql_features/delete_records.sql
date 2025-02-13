-- Delete JK Rowling from Authors
DELETE FROM authors WHERE author_id = '6b693b96-394a-4a1d-a4e2-792a47d7a568';

-- Delete books published after 1990
DELETE FROM books WHERE author_id = '6b693b96-394a-4a1d-a4e2-792a47d7a568';
