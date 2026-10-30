bl_info = {
    "name": "Auto3D (prototipo)",
    "author": "Tu",
    "version": (0, 1, 0),
    "blender": (5, 2, 0),
    "location": "Vista 3D > Barra laterale (tasto N) > Auto3D",
    "description": "Genera un albero parametrico ed esporta in GLB",
    "category": "Object",
}

import os
import bpy


def make_material(name, color):
    mat = bpy.data.materials.new(name)
    mat.diffuse_color = color
    try:
        if mat.node_tree is None:
            mat.use_nodes = True
        bsdf = mat.node_tree.nodes.get("Principled BSDF")
        if bsdf:
            bsdf.inputs["Base Color"].default_value = color
    except Exception:
        pass
    return mat


def remove_old_tree():
    for obj in list(bpy.data.objects):
        if obj.name.startswith("Auto3D_Albero"):
            bpy.data.objects.remove(obj, do_unlink=True)


class AUTO3D_OT_generate(bpy.types.Operator):
    bl_idname = "auto3d.generate_tree"
    bl_label = "Genera albero"

    def execute(self, context):
        scene = context.scene
        h = scene.auto3d_height
        layers = scene.auto3d_layers
        remove_old_tree()

        trunk_h = h * 0.3
        bpy.ops.mesh.primitive_cylinder_add(
            radius=h * 0.04, depth=trunk_h, location=(0, 0, trunk_h / 2)
        )
        trunk = context.active_object
        trunk.data.materials.append(make_material("Auto3D_Tronco", (0.35, 0.2, 0.1, 1)))
        parts = [trunk]

        leaf_mat = make_material("Auto3D_Foglie", (0.1, 0.5, 0.15, 1))
        crown_h = h * 0.7
        step = crown_h / layers * 0.6
        cone_h = crown_h / layers * 1.4
        for i in range(layers):
            radius = h * 0.25 * (1 - i / (layers + 1))
            z = trunk_h * 0.8 + i * step + cone_h / 2
            bpy.ops.mesh.primitive_cone_add(
                radius1=radius, radius2=0, depth=cone_h, location=(0, 0, z)
            )
            cone = context.active_object
            cone.data.materials.append(leaf_mat)
            parts.append(cone)

        bpy.ops.object.select_all(action="DESELECT")
        for p in parts:
            p.select_set(True)
        context.view_layer.objects.active = trunk
        bpy.ops.object.join()
        trunk.name = "Auto3D_Albero"
        return {"FINISHED"}


class AUTO3D_OT_export(bpy.types.Operator):
    bl_idname = "auto3d.export_glb"
    bl_label = "Esporta GLB"

    def execute(self, context):
        obj = bpy.data.objects.get("Auto3D_Albero")
        if obj is None:
            self.report({"WARNING"}, "Genera prima un albero")
            return {"CANCELLED"}
        bpy.ops.object.select_all(action="DESELECT")
        obj.select_set(True)
        context.view_layer.objects.active = obj
        path = os.path.expanduser(context.scene.auto3d_path)
        bpy.ops.export_scene.gltf(filepath=path, export_format="GLB", use_selection=True)
        self.report({"INFO"}, f"Esportato in {path}")
        return {"FINISHED"}


class AUTO3D_PT_panel(bpy.types.Panel):
    bl_label = "Auto3D"
    bl_idname = "AUTO3D_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Auto3D"

    def draw(self, context):
        col = self.layout.column(align=True)
        col.prop(context.scene, "auto3d_height")
        col.prop(context.scene, "auto3d_layers")
        col.operator("auto3d.generate_tree", icon="MESH_CONE")
        col.separator()
        col.prop(context.scene, "auto3d_path", text="File")
        col.operator("auto3d.export_glb", icon="EXPORT")


CLASSES = (AUTO3D_OT_generate, AUTO3D_OT_export, AUTO3D_PT_panel)


def register():
    bpy.types.Scene.auto3d_height = bpy.props.FloatProperty(
        name="Altezza (m)", default=4.0, min=1.0, max=20.0
    )
    bpy.types.Scene.auto3d_layers = bpy.props.IntProperty(
        name="Strati di foglie", default=3, min=1, max=6
    )
    bpy.types.Scene.auto3d_path = bpy.props.StringProperty(
        name="File", default="~/albero.glb", subtype="FILE_PATH"
    )
    for c in CLASSES:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(CLASSES):
        bpy.utils.unregister_class(c)
    del bpy.types.Scene.auto3d_height
    del bpy.types.Scene.auto3d_layers
    del bpy.types.Scene.auto3d_path


if __name__ == "__main__":
    register()