bl_info = {
    "name": "Auto3D (prototipo)",
    "author": "Tu",
    "version": (0, 2, 0),
    "blender": (5, 2, 0),
    "location": "Vista 3D > Barra laterale (tasto N) > Auto3D",
    "description": "Genera oggetti 3D parametrici (albero, roccia, casetta) ed esporta in GLB",
    "category": "Object",
}

import math
import os
import random

import bpy

OBJ_NAME = "Auto3D_Oggetto"

# Etichetta del cursore "dettaglio" per ogni preset
DETAIL_LABEL = {"TREE": "Strati di foglie", "ROCK": "Livello di dettaglio", "HOUSE": "Piani"}


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


def add_part(context, parts, material):
    obj = context.active_object
    obj.data.materials.append(material)
    parts.append(obj)
    return obj


def finish(context, parts):
    """Unisce tutti i pezzi in un unico oggetto chiamato Auto3D_Oggetto."""
    bpy.ops.object.select_all(action="DESELECT")
    for p in parts:
        p.select_set(True)
    context.view_layer.objects.active = parts[0]
    if len(parts) > 1:
        bpy.ops.object.join()
    parts[0].name = OBJ_NAME


def build_tree(context, size, detail, rng):
    parts = []
    trunk_h = size * 0.3
    bpy.ops.mesh.primitive_cylinder_add(
        radius=size * 0.04, depth=trunk_h, location=(0, 0, trunk_h / 2)
    )
    add_part(context, parts, make_material("Auto3D_Tronco", (0.35, 0.2, 0.1, 1)))
    leaf_mat = make_material("Auto3D_Foglie", (0.1, 0.5, 0.15, 1))
    crown_h = size * 0.7
    step = crown_h / detail * 0.6
    cone_h = crown_h / detail * 1.4
    for i in range(detail):
        radius = size * 0.25 * (1 - i / (detail + 1)) * rng.uniform(0.9, 1.1)
        z = trunk_h * 0.8 + i * step + cone_h / 2
        bpy.ops.mesh.primitive_cone_add(radius1=radius, radius2=0, depth=cone_h, location=(0, 0, z))
        add_part(context, parts, leaf_mat)
    return parts


def build_rock(context, size, detail, rng):
    parts = []
    bpy.ops.mesh.primitive_ico_sphere_add(
        subdivisions=max(1, min(detail, 4)), radius=size / 2, location=(0, 0, size / 3)
    )
    rock = add_part(context, parts, make_material("Auto3D_Roccia", (0.45, 0.45, 0.47, 1)))
    for v in rock.data.vertices:
        v.co.x *= rng.uniform(0.8, 1.2)
        v.co.y *= rng.uniform(0.8, 1.2)
        v.co.z *= rng.uniform(0.8, 1.2) * 0.7
    return parts


def build_house(context, size, detail, rng):
    parts = []
    wall_h = detail * size * 0.45
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, wall_h / 2))
    walls = add_part(context, parts, make_material("Auto3D_Pareti", (0.85, 0.8, 0.7, 1)))
    walls.scale = (size, size, wall_h)
    roof_h = size * 0.6
    bpy.ops.mesh.primitive_cone_add(
        vertices=4, radius1=size * 0.8, radius2=0, depth=roof_h,
        location=(0, 0, wall_h + roof_h / 2), rotation=(0, 0, math.radians(45)),
    )
    add_part(context, parts, make_material("Auto3D_Tetto", (0.6, 0.15, 0.1, 1)))
    return parts


BUILDERS = {"TREE": build_tree, "ROCK": build_rock, "HOUSE": build_house}


class AUTO3D_OT_generate(bpy.types.Operator):
    bl_idname = "auto3d.generate"
    bl_label = "Genera"

    def execute(self, context):
        s = context.scene
        old = bpy.data.objects.get(OBJ_NAME)
        if old:
            bpy.data.objects.remove(old, do_unlink=True)
        rng = random.Random(s.auto3d_seed)
        parts = BUILDERS[s.auto3d_preset](context, s.auto3d_size, s.auto3d_detail, rng)
        finish(context, parts)
        return {"FINISHED"}


class AUTO3D_OT_export(bpy.types.Operator):
    bl_idname = "auto3d.export_glb"
    bl_label = "Esporta GLB"

    def execute(self, context):
        obj = bpy.data.objects.get(OBJ_NAME)
        if obj is None:
            self.report({"WARNING"}, "Genera prima un oggetto")
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
        s = context.scene
        col = self.layout.column(align=True)
        col.prop(s, "auto3d_preset", text="Preset")
        col.prop(s, "auto3d_size")
        col.prop(s, "auto3d_detail", text=DETAIL_LABEL[s.auto3d_preset])
        col.prop(s, "auto3d_seed")
        col.operator("auto3d.generate", icon="MESH_ICOSPHERE")
        col.separator()
        col.prop(s, "auto3d_path", text="File")
        col.operator("auto3d.export_glb", icon="EXPORT")


CLASSES = (AUTO3D_OT_generate, AUTO3D_OT_export, AUTO3D_PT_panel)
PROPS = ("auto3d_preset", "auto3d_size", "auto3d_detail", "auto3d_seed", "auto3d_path")


def register():
    P = bpy.props
    bpy.types.Scene.auto3d_preset = P.EnumProperty(
        name="Preset",
        items=[("TREE", "Albero", ""), ("ROCK", "Roccia", ""), ("HOUSE", "Casetta", "")],
    )
    bpy.types.Scene.auto3d_size = P.FloatProperty(name="Dimensione (m)", default=4.0, min=0.5, max=30.0)
    bpy.types.Scene.auto3d_detail = P.IntProperty(name="Dettaglio", default=3, min=1, max=6)
    bpy.types.Scene.auto3d_seed = P.IntProperty(name="Seme (variazione)", default=1, min=0, max=9999)
    bpy.types.Scene.auto3d_path = P.StringProperty(name="File", default="~/auto3d_modello.glb", subtype="FILE_PATH")
    for c in CLASSES:
        bpy.utils.register_class(c)


def unregister():
    for c in reversed(CLASSES):
        try:
            bpy.utils.unregister_class(c)
        except Exception:
            pass
    for name in PROPS:
        if hasattr(bpy.types.Scene, name):
            delattr(bpy.types.Scene, name)


if __name__ == "__main__":
    register()
