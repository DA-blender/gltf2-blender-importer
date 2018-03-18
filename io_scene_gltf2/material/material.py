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
 """

import bpy

class Material():
    def __init__(self, index, json, gltf):
        self.index = index
        self.json = json # Material json
        self.gltf = gltf # Reference to global glTF instance

        self.blender_material = None

    def create_blender(self):
        if 'name' in self.json:
            self.name = self.json['name']
        else:
            self.name = "Material_" + str(self.index)

        mat = bpy.data.materials.new(self.name)
        self.blender_material = mat.name

    def debug_missing(self):
        keys = [

                ]

        for key in self.json.keys():
            if key not in keys:
                print("MATERIAL MISSING " + key)
