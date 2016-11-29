from Model import Model

class Presenter:
    def __init__(self, app, session):
        self._app = app
        self._model = Model(session)

    def handleDefault(self):
        return "leer"

    def handleLogin(self):
        return "login"

    def handleLogout(self):
        return "logut"

    def handleBooking(self):
        return "booking"

    def handleRegister(self):
        return "register"