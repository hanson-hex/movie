# movie
sqlalchemy.exc.IntegrityError: (pymysql.err.IntegrityError) (1452, 'Cannot add or update a child row: a foreign key constraint f
ails (`movie_project`.`comment`, CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`))') [SQL: 'INSERT I
NTO comment (content, addtime, movie_id, user_id) VALUES (%(content)s, %(addtime)s, %(movie_id)s, %(user_id)s)'] [parameters: {'
content': "this is user10's comment", 'movie_id': 6, 'user_id': 23, 'addtime': datetime.datetime(2017, 11, 15, 12, 31, 1, 133822
)}]

