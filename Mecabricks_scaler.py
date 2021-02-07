bl_info = {
    "name": "Mecabricks Scaler",
    "description": "Scales Mecabricks models to 0.1",
    "author": "rioforce",
    "version": (1, 0, 0),
    "blender": (2, 80, 0),
    "location": "World Properties",
    "wiki_url": "www.github.com/rioforce/Mecabricks_Scaler",
    "category": "Object",
}

import bpy
from bpy.types import (Panel, Operator)

# ------------------------------------------------------------------------
#    Operators
# ------------------------------------------------------------------------

class MB_EMPTIES(bpy.types.Operator):
    bl_idname = "meca.empties"
    bl_label = "Mecabrick Empties"
    
    
    def execute(self, context):
        #Select only empties
        objects = bpy.context.scene.objects
        for obj in objects:
            obj.select_set(obj.type == "EMPTY")       
        return{'FINISHED'};   
    
class MB_SCALER(bpy.types.Operator):
    bl_idname = "meca.scaler"
    bl_label = "Mecabrick Scaler"
    
    
    def execute(self, context):
        #Revert scale on selection
        bpy.ops.object.scale_clear(clear_delta=False)
        #Scale selection to 0.1
        bpy.ops.transform.resize(value=(0.1, 0.1, 0.1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        #Scale materials to 0.1

        for material in bpy.data.materials:
            if material.name.startswith("mb:o:"):
                material.node_tree.nodes["Value"].outputs[0].default_value = 0.1       
        return{'FINISHED'};
    
class MB_REVERT(bpy.types.Operator):
    bl_idname = "meca.revert"
    bl_label = "Mecabrick Scale Revert"
    
    
    def execute(self, context):
        #Scale selection to default
        bpy.ops.object.scale_clear(clear_delta=False)

        #Scale materials to 1
        for material in bpy.data.materials:
            if material.name.startswith("mb:o:"):
                material.node_tree.nodes["Value"].outputs[0].default_value = 1       
        return{'FINISHED'};

# ------------------------------------------------------------------------
#    Panel in Object Mode
# ------------------------------------------------------------------------

class MecaScale(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Mecabricks Scaler"
    bl_idname = "Mecabricks_Scale"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "world"

    def draw(self, context):
        layout = self.layout

        obj = context.object
        
        row = layout.row()
        row.label(text="Scales Mecabricks assets to 0.1 from default", icon='FILE_VOLUME')

        row = layout.row()
        row.operator("meca.empties", text="Select Empties", icon="OUTLINER_DATA_EMPTY")
        row = layout.row()
        row.operator("meca.scaler", text="Scale Down", icon="TRANSFORM_ORIGINS")
        row.operator("meca.revert", text="Revert Scale", icon="LOOP_BACK")


def register():
    bpy.utils.register_class(MecaScale)
    bpy.utils.register_class(MB_EMPTIES)
    bpy.utils.register_class(MB_SCALER)
    bpy.utils.register_class(MB_REVERT)


def unregister():
    bpy.utils.unregister_class(MecaScale)
    bpy.utils.unregister_class(MB_EMPTIES)
    bpy.utils.unregister_class(MB_SCALER)
    bpy.utils.unregister_class(MB_REVERT)
    
    


if __name__ == "__main__":
    register()
