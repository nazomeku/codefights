/*Your boss wants to identify the successful projects running in 
your company, so he asked you to prepare a list of all the 
currently active projects and their average monthly income.*/

CREATE PROCEDURE projectList()
BEGIN
	SELECT project_name, team_lead, income
    FROM Projects
    ORDER BY internal_id;
END
