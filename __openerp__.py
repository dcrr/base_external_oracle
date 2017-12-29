# -*- coding: utf-8 -*-
##############################################################################
#
#    Diana Rojas 2017
#    Lead Solutions
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'External Database Oracle',
    'version': '1.0',
    'category': 'Tools',
    'description': """This module allow fix bugs in module base_external_dbsource, for connection with cx_Oracle (6.1).""",
    'author': "Diana Rojas, Lead Solutions CIA",
    'license': 'AGPL-3',
    'depends': ['base_external_dbsource'],
    'external_dependencies': {'python': ['cx_Oracle']},
    'installable': True,
}