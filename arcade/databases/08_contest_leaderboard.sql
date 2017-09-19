/*You have already interviewed all the prize winners (the top 3 participants),
but that's not enough right now. Your company needs more specialists, so now
you would like to connect with the participants who took the next 5 places.*/

CREATE PROCEDURE contestLeaderboard()
BEGIN
	SELECT name from leaderboard
    ORDER BY score DESC
    LIMIT 3,5;
END
