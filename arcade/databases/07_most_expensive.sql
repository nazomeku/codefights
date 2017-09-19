/*The resulting table should contain one row with a single column: the product
with the lexicographically smallest name on which Mr. Cash spent the largest
amount of money.*/

CREATE PROCEDURE mostExpensive()
BEGIN
	SELECT name FROM Products
    ORDER BY price * quantity DESC, name ASC limit 1;
END
