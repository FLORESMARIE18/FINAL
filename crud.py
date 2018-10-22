from mysqlconnect import run_query

def create():
	query="CREATE TABLE audio( usuario varchar(20) ,nombre_audio varchar(50) not null, formato varchar(20)not null, duracion varchar(20) not null,frecuencia varchar(20) not null, canal varchar(20)not null, ruta varchar(200)not null)"
	print query
	run_query(query)

def  guardar(usuario,nombre_audio,formato,duracion,frecuencia,canal,ruta):
	
	query="INSERT INTO registro (usuario,nombre_audio,formato,duracion,frecuencia,canal,ruta) values"
	query+= "('" +usuario+"','" +nombre_audio+ "','" +formato+ "','" +str(duracion)+ "','"+str(frecuencia)+ "','"+canal+"','" +ruta+ "')"
	print query
	run_query(query)
	
def read(usuario):
	query="SELECT usuario FROM registro WHERE usuario ='%s'" %usuario
	print query
	run_query(query)

def delete(usuario):
	query="DELETE FROM registro WHERE usuario ='%s'" %usuario
	print query
	run_query(query)

def update(usuario):
	new_usuario=raw_input("Ingrese nuevo Usuario: ")
	query="UPDATE registro SET  usuario ='%s' WHERE usuario='%s' " %(new_usuario,usuario)
	print query
	run_query(query)

