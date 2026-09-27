from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    origin_notes = fields.Text(
        string='Origin Notes',
        help='Cacao origin, terroir, and tasting notes — displayed on the product detail page.',
    )
    is_featured = fields.Boolean(
        string='Featured on Homepage',
        default=False,
        help='Show this product in the homepage featured grid (max 6 shown, ordered by Website Sequence).',
    )
