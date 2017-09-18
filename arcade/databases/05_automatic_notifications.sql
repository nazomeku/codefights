/*The resulting table should contain a single email column and be sorted
by emails in ascending order.*/

CREATE PROCEDURE automaticNotifications()
    SELECT email
    FROM users
    WHERE role NOT IN ("admin", "premium")

    ORDER BY email;
