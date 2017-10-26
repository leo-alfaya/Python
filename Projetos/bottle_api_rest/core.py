from sqlalchemy import (create_engine, MetaData, Column, Table, Integer, String, ForeignKey, select)
from pdb import set_trace

engine = create_engine('sqlite:///base.db', echo=False)

metadata = MetaData(bind=engine)

artists = Table('artistas', metadata,
				 Column('id', Integer, primary_key=True, autoincrement=True),
				 Column('nome', String(40), index=True, nullable=False, unique=True))

discs = Table('discos', metadata,
				 Column('id', Integer, primary_key=True, autoincrement=True),
				 Column('artista_id', ForeignKey('artistas.id'), nullable=False),
				 Column('album', String(40), nullable=False),
				 Column('ano', Integer, nullable=False))

metadata.create_all()

def search_all_artists():
	set_trace()
	return {_id: artist for _id, artist in select([artists]).execute()}
	