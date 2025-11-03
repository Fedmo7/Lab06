from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio
import mysql.connector

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None


        """
        try:
            cnx = get_connection()
            if not cnx:
                return None
            cursor = cnx.cursor()
            query= "SELECT codice, marca, modello, anno, posti, disponibile FROM automobile"
            cursor.execute(query)
            automobili = []
            for (codice, marca, modello, anno, posti, disponibile) in cursor:
                auto=Automobile(codice, marca, modello, anno, posti, bool(disponibile))
                automobili.append(auto)
            cursor.close()
            cnx.close()
            return automobili if automobili else None
        except mysql.connector.Error as err:
            print(f'Errore durante la lettura delle automobili: {err}')
            return None






        # TODO

    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        # TODO
        try:
            cnx = get_connection()
            if not cnx:
                return None
            cursor = cnx.cursor()
            query="""
            SELECT codice, marca, modello, anno, posti, disponibile
            FROM automobile
            WHERE modello LIKE %s 
            """
            cursor.execute(query, (f"%{modello}%",))
            automobili = []
            for (codice,marca,modello,anno,posti,disponibile) in cursor:
                auto=Automobile(codice, marca, modello, anno, posti, bool(disponibile))
                automobili.append(auto)
            cursor.close()
            cnx.close()
            return automobili if automobili else None
        except mysql.connector.Error as err:
            print(f"Errore durante la ricerca: {err}")
            return None