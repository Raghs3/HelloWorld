import sqlite3
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

# conn = sqlite3.connect('music.sqlite')


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__(self, window, **kwargs)  # for python2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        # tkinter.Listbox.grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1,
        # **kwargs)  # for python2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        # Scrollbox.__init__(self, window, **kwargs)  # python2
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.link_value = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        self.link_value = link_value  # store the id, so we know the "master" record we're populated from
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            print(sql)    # TODO delete this line
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)     #TODO delete this line
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the listbox contents before re-loading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

            if self.linked_box:
                self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box and self.curselection():
            print(self is event.widget)    # TODO delete this line
            # lb = event.widget
            index = self.curselection()[0]
            value = self.get(index),

            # get the ID from the database row
            # make sure we're getting the correct one, by including the link_value if appropriate
            if self.link_value:
                value = value[0], self.link_value
                sql_where = " WHERE " + self.field + "=? AND " + self.link_field + "=?"
            else:
                sql_where = " WHERE " + self.field + "=?"

            # get the artist ID from the database row
            # link_id = self.cursor.execute(self.sql_select + " WHERE " + self.field + "=?", value).fetchone()[1]  # may cause errors on other programs using different connection names (not conn)
            link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]  # may cause errors on other programs using different connection names (not conn)

            # SELECT name, _id FROM albums WHERE name = 'Greatest Hits'  # due to this we get duplicates, as in all ppl have same songs in that album  # fix this

            self.linked_box.requery(link_id)

        # artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name=?", artist_name).fetchone()
        # alist = []
        # for row in conn.execute("SELECT albums.name FROM albums WHERE albums.artist=? ORDER BY albums.name", artist_id):
        #     alist.append(row[0])
        # albumLV.set(tuple(alist))
        # songLV.set(("Choose an album",))

# def get_songs(event):  # don't want to do this as duplication
#     lb = event.widget
#     index = int(lb.curselection()[0])
#     album_name = lb.get(index),
#
#     # get the artist ID grom the database row
#     album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
#     alist = []
#     for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album=? ORDER BY songs.track", album_id):
#         alist.append(x[0])
#     songLV.set(tuple(alist))

if __name__ == '__main__':
    conn = sqlite3.connect('music.sqlite')

    mainWindow = tkinter.Tk()
    mainWindow.title("Music DB Browser")
    mainWindow.geometry('1024x768')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)  # spacer column on right

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # ===== labels =====
    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    # ===== Artists Listbox =====
    # artistList = Scrollbox(mainWindow)
    artistList = DataListBox(mainWindow, conn, "artists", "name")
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30,0))
    artistList.config(border=2, relief='sunken')
    # don't need to create scrollbar, as it displays its own scrollbar that we did in class
    # artistScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)
    # artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
    # artistList['yscrollcommand'] = artistScroll.set  # does the communication between listbox and scroll bar

    # for artist in conn.execute("SELECT artists.name FROM artists ORDER BY artists.name"):
    #     artistList.insert(tkinter.END, artist[0])
    #

    artistList.requery()
    # artistList.bind('<<ListboxSelect>>', get_albums)  # now in class init function

    # ===== Albums Listbox =====
    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(("Choose an artist",))
    # albumList = Scrollbox(mainWindow, listvariable=albumLV)
    albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))
    # albumList.requery(12)
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30,0))
    albumList.config(border=2, relief='sunken')
    # going to see how to create scrollable list box class to avoid duplication  # see class, hence don't need bottom lines
    # albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
    # albumScroll.grid(row=1, column=1, sticky='nse')
    # albumList['yscrollcommand'] = albumScroll.set  # does the communication between listbox and scroll bar

    # albumList.bind('<<ListboxSelect>>', get_songs)
    artistList.link(albumList, "artist")

    # ===== Songs Listbox =====
    songLV = tkinter.Variable(mainWindow)
    songLV.set(("Choose an album",))
    # songList = Scrollbox(mainWindow, listvariable=songLV)
    songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
    # songList.requery()
    songList.grid(row=1, column=2, sticky='nsew', padx=(30,0))
    songList.config(border=2, relief='sunken')

    albumList.link(songList, "album")

    # ===== Main loop =====
    # testList = range(0, 100)
    # albumLV.set(tuple(testList))
    # albumLV.set((1, 2, 3, 4, 5))  # updates the listbox in gui with the values in the tuple
    mainWindow.mainloop()
    print("closing database connection")
    conn.close()
