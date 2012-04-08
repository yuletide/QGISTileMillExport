"""
/***************************************************************************
 QGISTileMillExport
                                 A QGIS plugin
 Export given map layer classes and styling to mss for MapBox TileMill
                             -------------------
        begin                : 2012-04-07
        copyright            : (C) 2012 by Alex Yule
        email                : ayule@alum.exeter.edu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "TileMill Layer Exporter"
def description():
    return "Export given map layer classes and styling to mss for MapBox TileMill"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load QGISTileMillExport class from file QGISTileMillExport
    from qgistilemillexport import QGISTileMillExport
    return QGISTileMillExport(iface)
