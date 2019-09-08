from triss import _houdini
import hou


hou.hipFile.addEventCallback(_houdini.scene_was_loaded)