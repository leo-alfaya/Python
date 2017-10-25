from core import user_table, engine

conn = engine.connect()

ins = user_table.insert()

new_user = ins.values(nome='Leonardo',
					 idade=28,
					 senha='1234')

conn.execute(new_user)