import sqlite3
import pandas as pd


def main():
    connection = sqlite3.connect("playlist.db")
    conn = connection.cursor()

    # conn.execute('''
    #              CREATE TABLE IF NOT EXISTS playlist
    #              ([song_id] INTEGER PRIMARY KEY, [song_name] TEXT)
    #              ''')

    # conn.execute('''
    #              INSERT INTO playlist (song_id, song_name)
                 
    #                 VALUES
    #                 (1, 'Where she goes'),
    #                 (2, 'Buenos Aires'),
    #                 (3, 'La Varita de Cana')   
    #              ''')

    conn.execute('''
                    SELECT * FROM playlist
                 ''')

    df = pd.DataFrame(conn.fetchall(), columns=['song_id', 'song_name'])
    print(df)

    # connection.commit()


if __name__ == "__main__":
    main()
