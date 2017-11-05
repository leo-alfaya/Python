from sqlalchemy import update
from core import user_table, engine

conn = engine.connect()

u = update(user_table).where(user_table.c.nome == 'Juacy')

# u = u.values(nome='Juacy')
u = u.values(idade=(user_table.c.idade + 1))

result = conn.execute(u)

print(result.rowcount)