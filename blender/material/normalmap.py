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
from .texture import *

def create_blender_normalmap_cycles(gltf_normalmap, mat_name):
    material = bpy.data.materials[mat_name]
    node_tree = material.node_tree

    blender_texture(gltf_normalmap.texture)
    
    # retrieve principled node and output node
    principled = [node for node in node_tree.nodes if node.type == "BSDF_PRINCIPLED"][0]

    # add nodes
    mapping = node_tree.nodes.new('ShaderNodeMapping')
    mapping.location = -1000,-500
    uvmap = node_tree.nodes.new('ShaderNodeUVMap')
    uvmap.location = -1500, -500
    uvmap["gltf2_texcoord"] = gltf_normalmap.texCoord # Set custom flag to retrieve TexCoord

    text  = node_tree.nodes.new('ShaderNodeTexImage')
    text.image = bpy.data.images[gltf_normalmap.texture.image.blender_image_name]
    text.color_space = 'NONE'
    text.location = -500, -500

    normalmap_node = node_tree.nodes.new('ShaderNodeNormalMap')
    normalmap_node.location = -250,-500


    # create links
    node_tree.links.new(mapping.inputs[0], uvmap.outputs[0])
    node_tree.links.new(text.inputs[0], mapping.outputs[0])
    node_tree.links.new(normalmap_node.inputs[1], text.outputs[0])

    # following  links will modify PBR node tree
    node_tree.links.new(principled.inputs[17], normalmap_node.outputs[0])

def blender_normalmap(gltf_normalmap, mat_name):
    engine = bpy.context.scene.render.engine
    if engine == 'CYCLES':
        create_blender_normalmap_cycles(gltf_normalmap, mat_name)
    else:
        pass #TODO for internal / Eevee in future 2.8