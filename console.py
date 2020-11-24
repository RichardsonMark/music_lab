import pdb 
from models.artist import Artist

from models.album import Album
import repositories.artist_repository as artist_repository

import repositories.album_repository as album_repository

# adding delete all first so to clear our example for next run
album_repository.delete_all()
artist_repository.delete_all()

# creating and saving an artist
metallica = Artist('Metallica')
artist_repository.save(metallica)
deftones = Artist('Deftones')
artist_repository.save(deftones)

# creating and saving an album
black_album = Album('Black Album', 'Heavy Metal', metallica)
album_repository.save(black_album)

white_pony = Album('White Pony', 'Metal', deftones)
album_repository.save(white_pony)

# updating an album
black_album.genre = "Metal"
album_repository.update(black_album)

# printing results of the above so we can see what's in the db at he end of the changes
for album in album_repository.select_all():
    print(album.__dict__)

pdb.set_trace()