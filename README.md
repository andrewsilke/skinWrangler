---- Skin Wrangler is by Chris Evans ------
============

This is a tool that I wrote for the proprietary Zeno software when at ILM years ago. It's largely based on the old 3dsMax Character Studio skin weight utility. In my spare time I decided to re-write it in Maya to help with the sheer amount of skinning work my team had at Crytek on Ryse: Son of Rome.

![alt tag](http://chrisevans3d.com/files/github/skinWrangler.png)

http://chrisevans3d.com
https://github.com/chrisevans3d/skinWrangler


---- Chris's Tutorial ----
https://www.youtube.com/watch?v=b__ABAKjDRI


---- Support 2019 - 2025 -----
This modified version simply adds support for PySide (UI) changes in 2020+ and also supports Python 3 in Maya 2022 and above.  No other changes have been made.

Contributors: Chris Evans, Andrew Silke, David Sparrow, Keen Foong, Le Simo

---- Install ----
Unzip this folder to a valid Maya scripts directory example:

username/Documents/maya/scripts/

Note you must rename the folder "skinWrangler-master" to "skinWrangler".

For example, the correct path would be:
username/Documents/maya/scripts/skinWrangler/  (skinWrangler_ui.py and other files here)

Start or restart Maya.

Then in Maya run the code below in Python to open the tool, or create a shelf with the following.


# ---- Python Code ----
from skinWrangler import skinWranglerui
skinWranglerWindow = skinWranglerui.show()