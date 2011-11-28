# -*- coding: utf-8 -*-
from yapsy.PluginManager import PluginManager

simplePluginManager = PluginManager()
simplePluginManager.setPluginPlaces(["plugins"])
simplePluginManager.collectPlugins()

# Activate all loaded plugins
for pluginInfo in simplePluginManager.getAllPlugins():
    simplePluginManager.activatePluginByName(pluginInfo.name)