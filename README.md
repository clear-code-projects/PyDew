Stardew Valley clone made in Pygame-ce. Created by Christian Koch / Clear code. 
The code for this project is in the public domain (Creative commons 0) you can use it for any purpose, including commercial ones, without permission. Attributions are not necessary but would be appreciated. 

This code is intended for a community project and is intended to be expanded. 

**To add additional characters:**
All the imports happen in the load_assets in main.py and the character_importer method imports the content of images/characters. The name of the subfolder will be a key in the dictionary 
and the files within that subfolder should be tileset images with each tile being 48x48. Each of these images will be stored in a sub dictionary attached to the subfolder key; the first row    
should be the up animation, the second one the down animation and the third row the left aimation; animations for the right side will be a flipped copy of the left side. 
If you want to add more character animations just check out the rabbit folder in characters to understand how it works. 

In sprites.py there is a Player class that currently controls the rabbit in the game you could inherit from that and overwrite methods or use the Entity class as a parent and add more to it. 
(The Player class currently has too many methods, quite a few of those could be stored in Entity to make the whole setup more flexible) 

**Adding to the tileset**
The level was created in Tiled (mapeditor.org). The layers are fairly self-explanatory (or at least I hope they are). Add more things as needed and then expand the setup method in the Level class to import it. 
The graphics folders contain a few more graphics that could be used to decorate the map. 

**Extracting data**
in the Level class there is an apply_tool method that lets an entity interact with the world (i.e. use a tool or plant a seed); if you want to measure what's going on in the game this should be a good starting point. 

