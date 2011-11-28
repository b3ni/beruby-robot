# -*- coding: utf-8 -*-
from plugins.click import Click

class BlogBeruby(Click):
    name = "Click para ver el block de beruby"
    id = 2267

    def visit(self):
        return True