import bpy


def create_cube():
    bpy.ops.mesh.primitive_cube_add(size=4)
    cube = bpy.context.active_object
    cube.location.z = 5
