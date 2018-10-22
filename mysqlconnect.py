import MySQLdb


host='localhost'    # your host, usually localhost
user='root'        # your username
passwd='miguel221'  # your password
db='audio'


def run_query(query):
	datos = [host,user,passwd,db]
	conn = MySQLdb.connect(*datos)
	cursor= conn.cursor()
	cursor.execute(query)
	if query.upper().startswith('SELECT'):
		data= cursor.fetchall()
	else:
		conn.commit()
		data= ""
	cursor.close()
	conn.close

	return data

