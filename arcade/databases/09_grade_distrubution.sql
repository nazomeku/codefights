/*As a Teaching Assistant (TA), you need to query the name and id of
all the students whose best grade comes from Option 3.*/

CREATE PROCEDURE gradeDistribution()
BEGIN
	SELECT Name, ID FROM Grades
    WHERE Final > (Midterm1 * 0.5 + Midterm2 * 0.5)
    ORDER BY LEFT(Name,3), ID ASC;
END
