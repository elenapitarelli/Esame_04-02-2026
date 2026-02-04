from database.DB_connect import DBConnect
from model.authorship import Authorship
from model.artist import Artist



class DAO:

    @staticmethod
    def get_authorship():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ SELECT * 
                    FROM authorship"""
        cursor.execute(query)

        for row in cursor:
            result.append(row)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_roles():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ select distinct role
from artsmia.authorship au, artsmia.artists ar 
where au.artist_id = ar.artist_id """
        cursor.execute(query)

        for row in cursor:
            role = Authorship(row["role"])
            result.append(role)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_role_artist(role):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ select distinct ar.name, ar.artist_id
from artsmia.authorship au, artsmia.artists ar 
where au.artist_id = ar.artist_id and au.role = '%s'
                group by ar.name, ar.artist_id"""
        cursor.execute(query, (role), )

        for row in cursor:
            role_artist = Artist(row["name"],row["artist_id"])
            result.append(role_artist)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_edges():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ select a1.artist_id as id1, a2.artist_id as id2
from authorship a1, authorship a2, objects o
where a1.object_id = o.object_id and a2.object_id = o.object_id and curator_approved = 1 and a1.role = '%s'
and a2.role = '%s'
and a1.artist_id <> a2.artist_id
group by a1.artist_id, a2.artist_id"""
        cursor.execute(query)

        for row in cursor:


            result.append( (row['id1'], row['id2']))

        cursor.close()
        conn.close()
        return result

    def get_indice_produttivita():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        query = """ select au.artist_id, count(*) as indice_produttivita
from authorship au, objects o
where au.object_id = o.object_id and o.curator_approved =1 and au.role = '%s'
group by artist_id"""

        cursor.execute(query)
        for row in cursor:
            result.append(row)
            cursor.close()
            conn.close()
            return result


        


