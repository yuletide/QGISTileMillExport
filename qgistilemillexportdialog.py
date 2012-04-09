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
    def __init__(self, vectorLayers):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_QGISTileMillExport()
        self.ui.setupUi(self)
        self.vectorLayers = vectorLayers
        QtCore.QObject.connect(self.ui.layerComboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.new_layer_selected)
        self.ui.layerComboBox.insertItems(0, [la.name() for la in self.vectorLayers])
    
    def new_layer_selected(self):
        QMessageBox.information(None,"TileMill Exporter","New Layer Selected: "+self.ui.layerComboBox.currentText())
        
    
    def get_current_layer(self):
        layerName = self.ui.layerComboBox.currentText()
        currentLayer = None
        for layer in self.vectorLayers:
            if layer.name() == layerName:
                currentLayer = layer
        return currentLayer
    
    def process_graduated_renderer(self, renderer):
        mss = ''
        attr = str(renderer.classAttribute())
        for i,ran in enumerate(renderer.ranges()):
            r = ran.symbol().symbolLayer(0).color().red()
            g = ran.symbol().symbolLayer(0).color().green()
            b = ran.symbol().symbolLayer(0).color().blue()
            a = ran.symbol().symbolLayer(0).color().alpha()
            if float(a) < 1:
                color = "rgba({},{},{},{})".format(r,g,b,a)
            else:
                color = "rgb({},{},{})".format(r,g,b)
            line_symbol = "line-color: {};".format(color)

            if i==0:
                mss += "[{} <= {:.5}]{{ {} }}\n".format(attr, ran.upperValue(), line_symbol)
            elif i==len(renderer.ranges())-1:
                mss+= "[{} > {:.5}]{{ {} }}\n".format(attr, ran.lowerValue(), line_symbol)
            else:
                mss += "[{attr} > {lower:.5}][{attr} <= {upper:.5}]{{ {sym} }}\n".format(attr=attr, lower=ran.lowerValue(), upper=ran.upperValue(), sym=line_symbol)
        QMessageBox.information(None,"TileMill Exporter",mss)
        return
