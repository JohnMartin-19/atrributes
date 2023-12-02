class Album:
    GENRES = ['Hiphop','Jazz','Pop']
    album_count = 0

    def __init__(self, date,genre):
        self.increase_album_count()
        self.release_date = date
        self.genre = genre
    @classmethod
    def increase_album_count(cls, increment=1):
        cls.album_count += increment
    
    @classmethod
    def check_genre(cls,genre):
        return genre in cls.GENRES