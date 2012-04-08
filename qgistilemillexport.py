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


    # run method that performs all the real work
    def run(self):
        def processGraduatedRenderer(renderer):
            mss = ''
            attr = str(renderer.classAttribute())
            for i,ran in enumerate(renderer.ranges()):
                if i==0:
                    mss += "[{} <= {}]{{ {} }}\n".format(attr, ran.upperValue(), str(ran.symbol().dump()))
                elif i==len(renderer.ranges())-1:
                    mss+= "[{} > {}]{{ {} }}\n".format(attr, ran.lowerValue(), str(ran.symbol().dump()))
                else:
                    mss += "[{attr} > {lower}][{attr} <= {upper}]{{ {sym} }}\n".format(attr=attr, lower=ran.lowerValue(), upper=ran.upperValue(), sym=str(ran.symbol().dump()))
            QMessageBox.information(None,"TileMill Exporter",mss)
            return

            '''for ran in rendererV2.ranges():
              print "%f - %f: %s %s" % (
                  range.lowerValue(),
                  range.upperValue(),
                  range.label(),
                  str(range.symbol())
                  )'''
        # get the currently active layer (if any)
        layer = self.iface.mapCanvas().currentLayer()
        if not hasattr(layer, 'isUsingRendererV2'):
            QMessageBox.information(None,"TileMill Exporter", "Please upgrade your version of qgis")
            return
        # test for valid vector layer
        if layer:
            if layer.type() == layer.VectorLayer:
                if layer.isUsingRendererV2() and layer.rendererV2().type() == 'graduatedSymbol':
                    processGraduatedRenderer(renderer=layer.rendererV2())
                    return
            QMessageBox.information(None,"TileMill Exporter","Unsupported renderer")
            return
        QMessageBox.information(None,"TileMill Exporter", "A vector layer must be selected")
        return


        # create and show the dialog
        dlg = QGISTileMillExportDialog()
        # show the dialog
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass
        
        
