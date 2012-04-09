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
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from qgistilemillexportdialog import QGISTileMillExportDialog

class QGISTileMillExport:
    
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.mapLayerRegistry = QgsMapLayerRegistry.instance()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/qgistilemillexport/icon.png"), \
            "Export Layer to TileMIll", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Export Layer to TileMIll", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Export Layer to TileMIll",self.action)
        self.iface.removeToolBarIcon(self.action)

    def processGraduatedRenderer(self, renderer):
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

        '''for ran in rendererV2.ranges():
          print "%f - %f: %s %s" % (
              range.lowerValue(),
              range.upperValue(),
              range.label(),
              str(range.symbol())
              )'''

    def get_vector_layers(self):
        availableLayers = self.mapLayerRegistry.mapLayers()
        vectorLayers = []
        for layer in availableLayers.values():
            if layer.type() == layer.VectorLayer:
                if is_supported_layer(layer):
                    vectorLayers.append(layer)
        return vectorLayers

    def is_supported_layer(self, layer):
        if layer.isUsingRendererV2() and layer.rendererV2().type() == 'graduatedSymbol':
            return True

    # run method that performs all the real work
    def run(self):
        vectorLayers = self.get_vector_layers()
        
        # get the currently active layer (if any)
        layer = self.iface.mapCanvas().currentLayer()
        if not hasattr(layer, 'isUsingRendererV2'):
            QMessageBox.information(None,"TileMill Exporter", "Please upgrade your version of qgis")
            return
        # test for valid vector layer
        if layer:
            if layer.type() == layer.VectorLayer:
                if layer.isUsingRendererV2() and layer.rendererV2().type() == 'graduatedSymbol':
                    self.processGraduatedRenderer(renderer=layer.rendererV2())
                    return
            QMessageBox.information(None,"TileMill Exporter","Unsupported renderer")
            return
        QMessageBox.information(None,"TileMill Exporter", "A vector layer must be selected")
        #return


        # create and show the dialog
        dlg = QGISTileMillExportDialog(vectorLayers)
        # show the dialog
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass
    
        
        
