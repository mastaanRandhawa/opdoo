from odoo import http
from odoo.http import request


class CriocoWebsite(http.Controller):

    @http.route('/', type='http', auth='public', website=True, sitemap=True)
    def homepage(self, **kwargs):
        env = request.env
        base_domain = request.website.website_domain()

        Product = env['product.template'].sudo()
        featured = Product.search(
            base_domain + [('is_published', '=', True), ('is_featured', '=', True)],
            limit=6,
            order='website_sequence asc',
        )
        if not featured:
            featured = Product.search(
                base_domain + [('is_published', '=', True)],
                limit=6,
                order='create_date desc',
            )

        Category = env['product.public.category'].sudo()
        cats = {
            rec.name: rec
            for rec in Category.search([
                ('name', 'in', ['Wild Chocolate', 'Signature Bars']),
            ])
        }

        return request.render('crioco_theme.homepage', {
            'featured_products': featured,
            'cat_wild': cats.get('Wild Chocolate'),
            'cat_signature': cats.get('Signature Bars'),
        })

    @http.route('/box-picks', type='http', auth='public', website=True, sitemap=True)
    def box_picks(self, **kwargs):
        env = request.env
        base_domain = request.website.website_domain()

        Category = env['product.public.category'].sudo()
        category = Category.search([('name', '=', 'Box Picks')], limit=1)

        domain = base_domain + [('is_published', '=', True)]
        if category:
            domain += [('public_categ_ids', 'in', [category.id])]

        products = env['product.template'].sudo().search(
            domain, limit=12, order='website_sequence asc',
        )

        return request.render('crioco_theme.box_picks', {
            'category': category,
            'products': products,
        })
