bl_info = {
    "name": "Mecabricks Scaler",
    "description": "Scales Mecabricks models to 0.1",
    "author": "rioforce",
    "version": (1, 1, 0),
    "blender": (2, 80, 0),
    "location": "World Properties",
    "wiki_url": "https://github.com/rioforce/Mecabricks-Scaler-for-Blender/blob/main/README.md",
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
        for obj in bpy.context.selected_objects :
            obj.scale *= 0.1

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

class MB_EPIC_SELECT(bpy.types.Operator):
    bl_idname = "epic.select"
    bl_label = "EpicFigRig Selector"
    
    
    def execute(self, context):
        #Select only empties
        objects = bpy.context.scene.objects
        for obj in objects:
            if obj.name.startswith("FinishedRig"):
                obj.select_set(obj.type == "ARMATURE")
        return{'FINISHED'};
    
class MB_EPIC_SCALE(bpy.types.Operator):
    bl_idname = "epic.scale"
    bl_label = "EpicFigRig Scale"
    
    
    def execute(self, context):
        #Unlock transformation
        objects = bpy.context.scene.objects
        for obj in bpy.context.selected_objects :
            obj.lock_scale[0] = False
            obj.lock_scale[1] = False
            obj.lock_scale[2] = False

            #Revert scale on selection
        bpy.ops.object.scale_clear(clear_delta=False)
            #Scale selection to 0.1
        for obj in bpy.context.selected_objects :
            obj.scale *= 0.1
            obj.lock_scale[0] = True
            obj.lock_scale[1] = True
            obj.lock_scale[2] = True
        return{'FINISHED'};
    
class MB_EPIC_REVERT(bpy.types.Operator):
    bl_idname = "epic.revert"
    bl_label = "EpicFigRig Revert"
    
    
    def execute(self, context):
        #Unlock transformation
        objects = bpy.context.scene.objects
        for obj in bpy.context.selected_objects :
            obj.lock_scale[0] = False
            obj.lock_scale[1] = False
            obj.lock_scale[2] = False

            #Revert scale on selection
        bpy.ops.object.scale_clear(clear_delta=False)
            #Scale selection to 0.1
        for obj in bpy.context.selected_objects :
            obj.scale *= 1
            obj.lock_scale[0] = True
            obj.lock_scale[1] = True
            obj.lock_scale[2] = True
        return{'FINISHED'};
    
class MB_EPIC_SHADERS(bpy.types.Operator):
    bl_idname = "epic.shader"
    bl_label = "Mecabricks Epic Shader Scaler"
    
    
    def execute(self, context):
        #Scale materials to 0.1
        objects = bpy.context.selected_objects
        for o in bpy.context.selected_objects:
            # Set the active materials value to 0.1 scale
            o.active_material.node_tree.nodes["Value"].outputs[0].default_value = 0.1
        return{'FINISHED'};
    
class MB_EPIC_REVERT_SHADERS(bpy.types.Operator):
    bl_idname = "epic.revertshader"
    bl_label = "Mecabricks Epic Shader Revert"
    
    
    def execute(self, context):
        #Scale materials to 0.1
        objects = bpy.context.selected_objects
        for o in bpy.context.selected_objects:
            # Set the active materials value to 0.1 scale
            o.active_material.node_tree.nodes["Value"].outputs[0].default_value = 1
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
        row.operator("meca.empties", text="Select all Empties in scene", icon="OUTLINER_DATA_EMPTY")
        row = layout.row()
        row.operator("meca.scaler", text="Scale Down", icon="TRANSFORM_ORIGINS")
        row.operator("meca.revert", text="Revert Scale", icon="LOOP_BACK")
        

class MecaScale(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "EpicFigRig Scaler"
    bl_idname = "EpicFig_Scale"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "world"
    
    def draw(self, context):
        layout = self.layout

        obj = context.object
    
        row = layout.row()
        row.label(text="Scale The EpicFigRig to match (after rigging).", icon='OUTLINER_DATA_ARMATURE')
        row = layout.row()
        row.operator("epic.select", text="Select all EpicFigRigs", icon="RESTRICT_SELECT_OFF")
        row = layout.row()
        row.operator("epic.scale", text="Scale Down", icon="TRANSFORM_ORIGINS")
        row.operator("epic.revert", text="Revert Scale", icon="LOOP_BACK")
        row = layout.row()
        row.label(text="Select all minifig body meshes before this!", icon='ERROR')
        row = layout.row()
        row.operator("epic.shader", text="Scale Materials", icon="NODE_MATERIAL")
        row.operator("epic.revertshader", text="Revert Materials", icon="MATERIAL")

def register():
    bpy.utils.register_class(MecaScale)
    bpy.utils.register_class(MB_EMPTIES)
    bpy.utils.register_class(MB_SCALER)
    bpy.utils.register_class(MB_REVERT)
    bpy.utils.register_class(MB_EPIC_SELECT)
    bpy.utils.register_class(MB_EPIC_SCALE)
    bpy.utils.register_class(MB_EPIC_REVERT)
    bpy.utils.register_class(MB_EPIC_SHADERS)
    bpy.utils.register_class(MB_EPIC_REVERT_SHADERS)


def unregister():
    bpy.utils.unregister_class(MecaScale)
    bpy.utils.unregister_class(MB_EMPTIES)
    bpy.utils.unregister_class(MB_SCALER)
    bpy.utils.unregister_class(MB_REVERT)
    bpy.utils.unregister_class(MB_EPIC_SELECT)
    bpy.utils.unregister_class(MB_EPIC_SCALE)
    bpy.utils.unregister_class(MB_EPIC_SHADERS)
    bpy.utils.unregister_class(MB_EPIC_REVERT_SHADERS)
    
    


if __name__ == "__main__":
    register()
