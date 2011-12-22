# -*- coding: utf-8 -*-
from yapsy.IPlugin import IPlugin
from plugins.click import Click

class BlogBeruby(IPlugin):
    name = "Click para ver el block de beruby"
    id = 2267

    def visit(self):
        return True