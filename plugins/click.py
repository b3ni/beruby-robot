# -*- coding: utf-8 -*-
from anunciante import Anunciante

class Click(Anunciante):
    name = "Click sobre un anunciante"
    id = None

    def visit(self):
        return True