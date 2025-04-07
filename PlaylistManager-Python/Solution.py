class Song:
    
    def __init__(self,title,artist,album,genre,duration):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration

    def display_details(self):
        return f"Title: {self.title}, Artist: {self.artist}, Album: {self.album}, Genre: {self.genre}, Duration:{self.duration}"   

class Playlist:

    def __init__(self,name):
        self.songs = []
        self.name = name 

    def add_song(self,song):
        self.songs.append(song)

    def remove_song(self,identifier):
        for i in self.songs:
            if i.title == identifier:
                self.songs.remove(i)
                return True
        return False

    def get_songs(self):
        return self.songs
    

    def filter_songs(self,criteria, value):
        lst = []
        if  criteria == "artist":
            for i in self.songs:
                if i.artist == value:
                    lst.append(i)
            return lst     
        
        # lst = []
        if  criteria == "title":
            for i in self.songs:
                if i.title == value:
                    lst.append(i)
            return lst 
        
        # lst = []
        if  criteria == "album":
            for i in self.songs:
                if i.album == value:
                    lst.append(i)
            return lst 
        
        # lst = []
        if  criteria == "genre":
            for i in self.songs:
                if i.genre == value:
                    lst.append(i)
            return lst 
        
        if  criteria == "duration":
            for i in self.songs:
                if i.duration == value:
                    lst.append(i)
            return lst 

               


    def search_songs(self,keyword):
        lst = []
        for i in self.songs:
            if keyword.lower() in i.artist.lower() or keyword.lower() in i.album.lower() or keyword.lower() in i.genre.lower() or keyword.lower() in i.title.lower():
                lst.append(keyword)
        return lst

class PlaylistManager:
    
    def __init__(self):
        self.somu = []

    def create_playlist(self,name):
        self.somu.append(Playlist(name))

    def delete_playlist(self,name):
        for i in self.somu:
            if i.name  == name:
                self.somu.remove(i)
                return True
        return False

    def get_playlist(self,name):

        for i in self.somu:
            if i.name == name:
                return i
        return "None"    
            
    def list_playlists(self):
        return self.somu

    def cross_playlist_search(self,keyword):
        lst = []
        for i in self.somu:
            j = i.search_songs(keyword)
            lst.extend(j)
        return lst    

                
