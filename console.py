import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

# adding delete all first so to clear our example for next run
album_repository.delete_all()
artist_repository.delete_all()

#creating and saving an artist
metallica = Artist('Metallica')
artist_repository.save(metallica)

#creating and saving an album
black_album = Album('Black Album', 'Heavy Metal', metallica)
album_repository.save(black_album)



pdb.set_trace()