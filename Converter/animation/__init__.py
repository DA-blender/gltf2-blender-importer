"""
 * ***** BEGIN GPL LICENSE BLOCK *****
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 *
 * Contributor(s): Julien Duroure.
 *
 * ***** END GPL LICENSE BLOCK *****
 * This development is done in strong collaboration with Airbus Defence & Space
 """

import bpy
from mathutils import Quaternion, Matrix

def blender_anim(self):
    if self.node.is_joint:
        blender_bone_anim()
    else:
        blender_node_anim()

def blender_bone_anim():
    pass
    # def anim(self):
    #     obj   = bpy.data.objects[self.animation.gltf.skins[self.animation.node.skin_id].blender_armature_name]
    #     bone  = obj.pose.bones[self.animation.node.blender_bone_name]
    #     fps = bpy.context.scene.render.fps
    #     delta = Quaternion((0.7071068286895752, 0.7071068286895752, 0.0, 0.0))

    #     for anim in self.animation.anims.keys():
    #         if not self.animation.gltf.animations[anim].blender_action:
    #             if self.animation.gltf.animations[anim].name:
    #                 name = self.animation.gltf.animations[anim].name
    #             else:
    #                 name = "Animation_" + str(self.animation.gltf.animations[anim].index)
    #             action = bpy.data.actions.new(name)
    #             self.animation.gltf.animations[anim].blender_action = action.name
    #         if not obj.animation_data:
    #             obj.animation_data_create()
    #         obj.animation_data.action = bpy.data.actions[self.animation.gltf.animations[anim].blender_action]

    #         for channel in self.animation.anims[anim]:
    #             if channel.path == "translation":
    #                 blender_path = "location"
    #                 for key in channel.data:
    #                     transform = Matrix.Translation(self.animation.gltf.convert.location(list(key[1])))
    #                     if not self.animation.node.parent:
    #                         mat = transform * delta.to_matrix().to_4x4()
    #                     else:
    #                         if not self.animation.gltf.scene.nodes[self.animation.node.parent].is_joint: # TODO if Node in another scene
    #                             parent_mat = bpy.data.objects[self.animation.gltf.scene.nodes[self.animation.node.parent].blender_object].matrix_world
    #                             mat = transform * parent_mat.inverted()
    #                         else:
    #                             parent_mat = self.animation.gltf.scene.nodes[self.animation.node.parent].blender_bone_matrix

    #                             mat = (parent_mat.to_quaternion() * delta.inverted() * transform.to_quaternion() * delta).to_matrix().to_4x4()
    #                             mat = Matrix.Translation(parent_mat.to_translation() + ( parent_mat.to_quaternion() * delta.inverted() * transform.to_translation() )) * mat
    #                             #TODO scaling of bones

    #                     bone.location = self.animation.node.blender_bone_matrix.to_translation() - mat.to_translation()
    #                     bone.keyframe_insert(blender_path, frame = key[0] * fps, group='location')


    #                 # Setting interpolation
    #                 for fcurve in [curve for curve in obj.animation_data.action.fcurves if curve.group.name == "rotation"]:
    #                     for kf in fcurve.keyframe_points:
    #                         self.animation.set_interpolation(channel.interpolation, kf)

    #             elif channel.path == "rotation":
    #                 blender_path = "rotation_quaternion"
    #                 for key in channel.data:
    #                     transform = (self.animation.gltf.convert.quaternion(key[1])).to_matrix().to_4x4()
    #                     if not self.animation.node.parent:
    #                         mat = transform * delta.to_matrix().to_4x4()
    #                     else:
    #                         if not self.animation.gltf.scene.nodes[self.animation.node.parent].is_joint: # TODO if Node in another scene
    #                             parent_mat = bpy.data.objects[self.animation.gltf.scene.nodes[self.animation.node.parent].blender_object].matrix_world
    #                             mat = transform * parent_mat.inverted()
    #                         else:
    #                             parent_mat = self.animation.gltf.scene.nodes[self.animation.node.parent].blender_bone_matrix

    #                             mat = (parent_mat.to_quaternion() * delta.inverted() * transform.to_quaternion() * delta).to_matrix().to_4x4()
    #                             mat = Matrix.Translation(parent_mat.to_translation() + ( parent_mat.to_quaternion() * delta.inverted() * transform.to_translation() )) * mat
    #                             #TODO scaling of bones

    #                     bone.rotation_quaternion = self.animation.node.blender_bone_matrix.to_quaternion().inverted() * mat.to_quaternion()
    #                     bone.keyframe_insert(blender_path, frame = key[0] * fps, group='rotation')

    #                 # Setting interpolation
    #                 for fcurve in [curve for curve in obj.animation_data.action.fcurves if curve.group.name == "rotation"]:
    #                     for kf in fcurve.keyframe_points:
    #                         self.animation.set_interpolation(channel.interpolation, kf)


    #             elif channel.path == "scale":
    #                 blender_path = "scale"
    #                 for key in channel.data:
    #                     s = self.animation.gltf.convert.scale(list(key[1]))
    #                     transform = Matrix([
    #                         [s[0], 0, 0, 0],
    #                         [0, s[1], 0, 0],
    #                         [0, 0, s[2], 0],
    #                         [0, 0, 0, 1]
    #                     ])

    #                     if not self.animation.node.parent:
    #                         mat = transform * delta.to_matrix().to_4x4()
    #                     else:
    #                         if not self.animation.gltf.scene.nodes[self.animation.node.parent].is_joint: # TODO if Node in another scene
    #                             parent_mat = bpy.data.objects[self.animation.gltf.scene.nodes[self.animation.node.parent].blender_object].matrix_world
    #                             mat = transform * parent_mat.inverted()
    #                         else:
    #                             parent_mat = self.animation.gltf.scene.nodes[self.animation.node.parent].blender_bone_matrix

    #                             mat = (parent_mat.to_quaternion() * delta.inverted() * transform.to_quaternion() * delta).to_matrix().to_4x4()
    #                             mat = Matrix.Translation(parent_mat.to_translation() + ( parent_mat.to_quaternion() * delta.inverted() * transform.to_translation() )) * mat
    #                             #TODO scaling of bones


    #                     #bone.scale # TODO
    #                     bone.keyframe_insert(blender_path, frame = key[0] * fps, group='scale')

    #                 # Setting interpolation
    #                 for fcurve in [curve for curve in obj.animation_data.action.fcurves if curve.group.name == "rotation"]:
    #                     for kf in fcurve.keyframe_points:
    #                         self.animation.set_interpolation(channel.interpolation, kf)


def blender_node_anim():
    pass
    
    # def anim(self):
    #     obj = bpy.data.objects[self.animation.node.blender_object]
    #     fps = bpy.context.scene.render.fps

    #     for anim in self.animation.anims.keys():
    #         if not self.animation.gltf.animations[anim].blender_action:
    #             if self.animation.gltf.animations[anim].name:
    #                 name = self.animation.gltf.animations[anim].name
    #             else:
    #                 name = "self.animation_" + str(self.animation.gltf.animations[anim].index)
    #             action = bpy.data.actions.new(name)
    #             self.animation.gltf.animations[anim].blender_action = action.name
    #         if not obj.animation_data:
    #             obj.animation_data_create()
    #         obj.animation_data.action = bpy.data.actions[self.animation.gltf.animations[anim].blender_action]

    #         for channel in self.animation.anims[anim]:
    #             if channel.path in ['translation', 'rotation', 'scale']:

    #                 if channel.path == "translation":
    #                     blender_path = "location"
    #                     for key in channel.data:
    #                        obj.location = Vector(self.animation.gltf.convert.location(list(key[1])))
    #                        obj.keyframe_insert(blender_path, frame = key[0] * fps, group='location')

    #                     # Setting interpolation
    #                     for fcurve in [curve for curve in obj.animation_data.action.fcurves if curve.group.name == "rotation"]:
    #                         for kf in fcurve.keyframe_points:
    #                             self.animation.set_interpolation(channel.interpolation, kf)

    #                 elif channel.path == "rotation":
    #                     blender_path = "rotation_quaternion"
    #                     for key in channel.data:
    #                         obj.rotation_quaternion = self.animation.gltf.convert.quaternion(key[1])
    #                         obj.keyframe_insert(blender_path, frame = key[0] * fps, group='rotation')

    #                     # Setting interpolation
    #                     for fcurve in [curve for curve in obj.animation_data.action.fcurves if curve.group.name == "rotation"]:
    #                         for kf in fcurve.keyframe_points:
    #                             self.animation.set_interpolation(channel.interpolation, kf)


    #                 elif channel.path == "scale":
    #                     blender_path = "scale"
    #                     for key in channel.data:
    #                         obj.scale = Vector(self.animation.gltf.convert.scale(list(key[1])))
    #                         obj.keyframe_insert(blender_path, frame = key[0] * fps, group='scale')

    #                     # Setting interpolation
    #                     for fcurve in [curve for curve in obj.animation_data.action.fcurves if curve.group.name == "rotation"]:
    #                         for kf in fcurve.keyframe_points:
    #                             self.animation.set_interpolation(channel.interpolation, kf)

    #             elif channel.path == 'weights':
    #                 cpt_sk = 0
    #                 for sk in channel.data:
    #                     for key in sk:
    #                         obj.data.shape_keys.key_blocks[cpt_sk+1].value = key[1]
    #                         obj.data.shape_keys.key_blocks[cpt_sk+1].keyframe_insert("value", frame=key[0] * fps, group='ShapeKeys')

    #                     cpt_sk += 1
