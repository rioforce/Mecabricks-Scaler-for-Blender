# Mecabricks Scaler (for Blender)

Blender plugin to scale Mecabricks files to a more managable size for use in Blender.

**NOTE:** This plugin is in no way associated with Mecabricks, and is only for convenience by the end user.

### What's the issue?
Mecabricks files, when imported into Blender without the provided template file, are giant. They cause major issues for people wishing to use them alongside other 3D models, and present issues with scaling of camera, lights, Depth of Field, and physics.

Because of this, I've created this plugin to automatically shrink all imported Mecabricks files to

## Installing

First, download the plugin from [Releases](https://github.com/rioforce/Mecabricks-Scaler-for-Blender/releases/). Then, in Blender, open Edit > Preferences > Add-ons. Click "Install," and browse for the .zip file you just downloaded.

Search for the plugin in the add-ons list, and hit the check mark to activate it.

![Add-ons panel in Blender](https://i.imgur.com/Yvk8Std.png)
## How to use

Inside Blender, navigate to the settings sidebar. Go to the **World** panel. You'll find a row called "Mecabricks Scaler." There, you'll find options.

![World panel in Blender](https://i.imgur.com/QaeWDin.png)

Mecabricks Scaler scales all Mecabricks items in the scene to 0.1 scale (scale varies depending on project settings, but I'm using default Blender units).

- Pressing **Select Empties** selects all the empties in the scene. Be sure to deselect any empties you don't want to be affected before moving to the next step.
- Pressing **Scale Down** scales all selected items (which, if you pressed *Select Empties* prior to this step, will be only Empties) to 0.1. The plugin reverts any previous scaling before scaling to 0.1 for consistency's sake. It also scales **all materials** to 0.1 scale. Even un-scaled bricks are affected by this.
- The **Revert Scale** button reverts scaling on *all* selected items and Mecabricks materials. *Press Select Empties before using this.* Don't press this if you don't want your scale back to normal.


#### What's this about empties?
All Mecabrick models are children of Empties. It's cleaner to select the empties that control the location and the scaling of the bricks instead of selecting the brick meshes themselves to scale. Mecabricks Empties do not have a unique naming scheme, so this is why all empties in the scene are affected by the scaling plugin.

## Development
This is just an informal plugin that I made to make my life easier, and I'm offering it to you.
One day, I'd like to add the following features. But that may never happen, so feel free to make a pull request!

- Select only empties that are associated with a brick that's associated with a material that begins with `mb:o:` (basically, select only Mecabricks empties)
- Make scaling of mateirals only affect selected bricks instead of all bricks (which would correspond to above)
- Add fancy "Import Mecabricks" button to menu where it automatically scales on import.
