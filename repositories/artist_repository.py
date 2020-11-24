from models.artist import Artist
from models.album import Album
from db.run_sql import run_sql


#CREATE
# save (create) artist
def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist


# READ
# find (read) artist by id
def select(id):
    artist = None

    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['id'])

    return artist


# list (read) artists
def select_all():
    artists = []

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'] )
        artists.append(artist)
    return artists


# UPDATE
# edit artists
def update(artist):
    sql = "UPDATE artists SET name = %s WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)


# DELETE
# deletes (all) artists
def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

# DELETE - delete one
def delete(id):
  sql = "DELETE FROM artists WHERE id = %s"
  values = [id]
  run_sql(sql, values)