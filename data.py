#+----------------------------------------------------------------+
#|                            USER DATA                           |
#+----------------------------------------------------------------+
# Datos almacenados de manera local en el momento de la ejecucion del programa.
class UserData():
    def __init__(self):
        self._id = None
        self._imgs = {}

    # ============ ID ============
    # Almacena el id del usuario ingresado
    def add_id(self, user_id):
        self._id = user_id

    def get_id(self):
        return self._id

    # ============ IMGS ============
    # Almacena imagenes descargadas en drive y posteriormente registradas en dearpygui para su uso
    def add_imgs(self, id_drive, img):
        self._imgs[id_drive] = img

    def get_imgs(self):
        return self._imgs

user_data = UserData()