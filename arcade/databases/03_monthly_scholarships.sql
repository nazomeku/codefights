/*Now you need to calculate the amount of money each student should get per
month. Given the table scholarships, build the resulting table*/

CREATE PROCEDURE monthlyScholarships()
BEGIN
	SELECT id, scholarship/12 as scholarship from scholarships;
END
