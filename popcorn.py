import Skype4Py
import time
from NetflixRoulette import *
from util import *


class Popcorn(object):
    def __init__(self):
        self.skype = Skype4Py.Skype()
        self.skype.Attach()
        self.skype.OnMessageStatus = self.cmd

        self.context = ''

    def cmd(self, Message, Status):
        if Status == 'SENT' or Status == 'RECEIVED':
            bot = Message.Body.split(' ')[0]
            cmd = Message.Body.split(' ')[1]
            if bot == '//popcorn' and cmd in self.cmds.keys():
                self.context = Message
                self.cmds[cmd](self)

    def movie_poster(self):
        movie = self.context.Body.split()[2]
        url = []
        put = str(get_media_poster(movie))
        url.append(put)
        self.context.Chat.SendMessage('/me [Popcorn Bot]: Poster for ' + movie + ' {link}: ' + short(url[0]))

    def movie_id(self):
        movie = self.context.Body.split()[2]
        self.context.Chat.SendMessage('/me [Popcorn Bot]: Netflix ID for ' + movie + ' {ID}: ' + str(get_netflix_id(movie)))

    def movie_director(self):
        movie = self.context.Body.split()[2]
        self.context.Chat.SendMessage('/me [Popcorn Bot]: Director(s) for ' + movie + ' {Director List}: ' + get_media_director(movie))

    def movie_summary(self):
        movie = self.context.Body.split()[2]
        self.context.Chat.SendMessage('/me [Popcorn Bot]: Plot Summary for ' + movie + ' {Summary}: ' + get_media_summary(movie))


    def movie_category(self):
        movie = self.context.Body.split()[2]
        self.context.Chat.SendMessage('/me [Popcorn Bot]: Netflix category for ' + movie + ' {Category}: ' + get_media_category(movie))

    def movie_cast(self):
        movie = self.context.Body.split()[2]
        self.context.Chat.SendMessage('/me [Popcorn Bot]: Cast Members for ' + movie + ' {Cast}: ' + get_media_cast(movie))

    def movie_rlsdate(self):
        movie = self.context.Body.split()[2]
        self.context.Chat.SendMessage('/me [Popcorn Bot]: Release date for ' + movie + ' {Release Date}: ' + get_media_release_year(movie))

    def gettype(self):
        movie = self.context.Body.split()[2]
        return get_media_type(movie)

    def movie_rating(self):
        movie = self.context.Body.split()[2]
        self.context.Chat.SendMessage('/me [Popcorn Bot]: Movie Rating for ' + movie + ' {Rating}: ' + get_media_rating(movie))

    def movie_full(self):
        movie = self.context.Body.split()[2]
        url = []
        put = str(get_media_poster(movie))
        url.append(put)
        self.context.Chat.SendMessage('/me [Popcorn Bot Presents]')
        self.context.Chat.SendMessage('/me {Movie}: ' + str(movie).capitalize())
        self.context.Chat.SendMessage('/me {Release Date}: ' + get_media_release_year(movie))
        self.context.Chat.SendMessage('/me {Category}: ' + get_media_category(movie))
        self.context.Chat.SendMessage('/me {Director}: ' + get_media_director(movie))
        self.context.Chat.SendMessage('/me {Rating}: ' + get_media_rating(movie))
        self.context.Chat.SendMessage('/me {Poster}: ' + short(url[0]))
        self.context.Chat.SendMessage('/me {Netflix ID}: ' + str(get_netflix_id(movie)))

    def c_list(self):
        self.context.Chat.SendMessage('/me [Popcorn Bot]: use //popcorn [cmd] [answer] {Commands are Poster,ID,director,summary,category,release_date,cast,rating,movie_full}')


    cmds = {'poster': movie_poster,
            'ID': movie_id,
            'director': movie_director,
            'summary': movie_summary,
            'category': movie_category,
            'release_date': movie_rlsdate,
            'cast': movie_cast,
            'rating': movie_rating,
            'movie_full': movie_full,
            'commands': c_list}


if __name__ == '__main__':
    Start = Popcorn()
    while True:
        time.sleep(1)





