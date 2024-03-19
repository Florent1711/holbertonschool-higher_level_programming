-- Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)
-- Write a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT tv.title, tvg.genre_id
FROM hbtn_0d_tvshows AS tv
LEFT JOIN hbtn_0d_tvshows_genres AS tvg ON tv.id = tvg.show_id
ORDER BY tv.title ASC, tv.genre_id ASC;
