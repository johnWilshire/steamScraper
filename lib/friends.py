class Friends:
    def __init__(self, connection):
        self.connection = connection


    def addFriends(self, pid,  friendsList):
        friendsList = " . ".join(friendsList)
        tup = (str(pid), friendsList,  )
        statement = """INSERT INTO FriendsList (steamid, friends) VALUES (?,?);"""
        c = self.connection.cursor()
        c.execute(statement, tup)
        self.connection.commit()