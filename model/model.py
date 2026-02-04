import networkx as nx
from database.dao import DAO
from model.artist import Artist


class Model:
    def __init__(self):
        self.G = nx.DiGraph()
        self.artists = []
        self.roles_list = []
        self.load_all_roles()
        self._role_artist_list = []
        self.load_role_artist =[]
        self.peso_dict = {}

    def load_all_roles(self):
        self._roles_list = DAO.get_roles()
        print(f"Ruoli: {self._roles_list}")


    def load_role_artist(self, role):
        self._role_artist_list = DAO.get_role_artist(role)
        print(f"Ruoli: {self._role_artist_list}")

    def load_edges(self):
        self._edges = DAO.get_edges()
        print(f"Ruoli: {self._edges}")



    def build_graph(self, role: str):
        self._nodes = []
        self._edges = []
        self.id_map = {}
        # carico nodi e archi
        self.load_role_artist(role)
        self.load_edges()
        self.G.clear()
        for role in self._roles_artist_list:
            self._nodes.append(role)
            self.id_map[role] = role

        self._G.add_nodes_from(self._nodes)

        for id1, id2, peso  in self._edges:
            self.G.add_edge(id1, id2)
            if id1 in self.id_map and id2 in self.id_map:
                artista1 = self.id_map[id1]
                artista2 = self.id_map[id2]
                peso = abs(self.peso_dict(artista1) - self.peso_dict(artista2))






    def classifica(self):
        pass
