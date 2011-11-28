# -*- coding: utf-8 -*-
from anunciante import Anunciante

class Click(Anunciante):
    name = "No Format"
    id = None

    def visit(self):        
        return True