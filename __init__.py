
bl_info = {
    "name": "Game Rig Tools",
    "author": "BlenderBoi, Xin",
    "version": (1, 7, 2),
    "blender": (3, 1, 0),
    "description": "Generate a Deform Rig base on CGDive's Game-Ready Rig Video",
    "warning": "",
    "doc_url": "https://tarry-dill-523.notion.site/Game-Rig-Tools-Documentation-dc61839fd1d04147a42aa89e366575fb",
    "category": "Armature",
}

import bpy

from . import GRT_Extra_Operators

from . import Deform_Rig_Generator
from . import Deform_Rig_Panel
from . import Preferences

from . import GRT_Action_Bakery
from . import addition

import os
import pathlib
import shutil

current_path = pathlib.Path(__file__).parent
script_directory = str(current_path.parents[1]) 
preset_directory = os.path.join(script_directory, "presets")
src_preset_path = os.path.join(current_path, "presets")

check_dir = os.path.join(preset_directory, "operator", "gamerigtool.generate_game_rig")

modules = [addition, GRT_Extra_Operators, Deform_Rig_Generator, Deform_Rig_Panel, GRT_Action_Bakery, Preferences]


def register():
    
    copy_preset = True

    if os.path.isdir(check_dir):

        for file in os.listdir(check_dir):
            if file.endswith(".py"):
                copy_preset = False
                break
    else:
        copy_preset = True 

    if copy_preset:
    # os.path.isdir(os.path.join(preset_directory, ""))
        shutil.copytree(src_preset_path, preset_directory, dirs_exist_ok=True)

    for module in modules:
        module.register()

def unregister():

    for module in modules:
        module.unregister()

if __name__ == "__main__":
    register()
