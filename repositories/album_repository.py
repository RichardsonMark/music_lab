from db.run_sql import run_sql

import repositories.artist_repository as artist_repository

from models.album import Album

#CREATE
# save (create) album
def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    #  for last item we are referencing the album objects, artist objects id as a reference
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    # if id was 4 then rhs says its the 0th index of the results list where the key is 'id' and the associated value of that key is 4
    id = results[0]['id']
    # assigns our album with its own id  - i.e if it was 4 on the line above our album.id is now 4
    album.id = id
    return album


# READ
# find (read) album by id
def select(id):
    album = None

    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], result['genre'], artist, result['id'])
    return album

# UPDATE


# DELETE
# deletes (all) artists
def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)