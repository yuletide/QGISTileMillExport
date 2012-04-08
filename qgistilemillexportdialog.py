"""
/***************************************************************************
 QGISTileMillExportDialog
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
"""

from PyQt4 import QtCore, QtGui
from ui_qgistilemillexport import Ui_QGISTileMillExport
# create the dialog for zoom to point
class QGISTileMillExportDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_QGISTileMillExport()
        self.ui.setupUi(self)
