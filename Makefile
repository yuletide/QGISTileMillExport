#/***************************************************************************
# QGISTileMillExport
# 
# Export given map layer classes and styling to mss for MapBox TileMill
#                             -------------------
#        begin                : 2012-04-07
#        copyright            : (C) 2012 by Alex Yule
#        email                : ayule@alum.exeter.edu
# ***************************************************************************/
# 
#/***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/

# Makefile for a PyQGIS plugin 

PLUGINNAME = qgistilemillexport

PY_FILES = qgistilemillexport.py qgistilemillexportdialog.py __init__.py

EXTRAS = icon.png 

UI_FILES = ui_qgistilemillexport.py

RESOURCE_FILES = resources.py

default: compile

compile: $(UI_FILES) $(RESOURCE_FILES)

%.py : %.qrc
	pyrcc4 -o $@  $<

%.py : %.ui
	pyuic4 -o $@ $<

# The deploy  target only works on unix like operating system where
# the Python plugin directory is located at:
# $HOME/.qgis/python/plugins
deploy: compile
	mkdir -p $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	cp -vf $(PY_FILES) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	cp -vf $(UI_FILES) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	cp -vf $(RESOURCE_FILES) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)
	cp -vf $(EXTRAS) $(HOME)/.qgis/python/plugins/$(PLUGINNAME)

