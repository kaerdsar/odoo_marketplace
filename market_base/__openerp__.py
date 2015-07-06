# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010, 2014 Tiny SPRL (<http://tiny.be>).
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
    'name': 'Market Base',
    'version': '0.1',
    'author': 'OpenJAF',
    'website': 'http://www.openjaf.com',
    'category': 'Base',
    'description': """
        Market Base
    """,
    'depends': ['product', 'stock', 'stock_account', 
                'product_variants_extension', 'odoo_connector'],
    'data': [
        'security/ir.model.access.csv',
        'edi/stock_picking_data.xml',
        'views/product.xml',
        'views/stock.xml',
        'views/request.xml',
        'views/b2b.xml',
    ],
    'installable': True
}