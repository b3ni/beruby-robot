# -*- coding: utf-8 -*-
from yapsy.PluginManager import PluginManager

# cargamos los plugins
simplePluginManager = PluginManager()
simplePluginManager.setPluginPlaces(["plugins"])
simplePluginManager.collectPlugins()

# activate all loaded plugins
for pluginInfo in simplePluginManager.getAllPlugins():
    simplePluginManager.activatePluginByName(pluginInfo.name)
    
# creamos el nucleo
beruby = Beruby()

# login
beruby.login()