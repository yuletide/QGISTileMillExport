#Install instructions (untested):
    $ make install
    
if that doesn't work try

    $ sh reinstall.sh
    
- Then, in QGIS, go to Plugins --> Manage Plugins
- Check the box to enable the plugin
    - A toolbar button should appear

#Usage

1. Click the toolbar button or go to Plugins --> Export Layer to TileMill --> Export Layer to TileMill
2. Select the layer you'd like to use (currently everything gets output as line-color)
3. Copy the mss and paste into tilemill

## Limitations

- Only supports graduated renderers
- Everything is output as a line-color style, not sure if it works with polygon layers

![img](https://github.com/yuletide/QGISTileMillExport/raw/master/dialog.png)
![img](https://github.com/yuletide/septa_frequency_map/raw/master/septa.png)

Yay.