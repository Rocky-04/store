import logging

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import DetailView
from django.views.generic import TemplateView

from .forms import ReviewsForm
from .services import add_user_review
from .services import filter_products
from .services import get_active_color
from .services import get_active_size
from .services import get_filter_products
from .services import get_list_of_nested_category_id
from .services import get_products_list_pk
from .services import send_message_from_user
from .utils import *

logger = logging.getLogger(__name__)


class FilterView(ShopMixin):
    def get_queryset(self):
        """
        Filters the product by the selected attributes
        Available filters: min_price, max_price, color, size, manufacturer
        """
        self.product_list_pk = get_products_list_pk(self.request.GET.get('product_list_pk'))
        return filter_products(request=self.request, product_list_pk=self.product_list_pk)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Filter')
        return context


class SkipFilterView(ShopMixin):
    """
    Resets enabled filters
    """

    def get_queryset(self):
        self.product_list_pk = get_products_list_pk(self.request.GET.get('product_list_pk'))
        queryset = get_filter_products(pk__in=self.product_list_pk)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Products')
        return context


class ShopView(ShopMixin):
    """
    Shows all available products
    """

    def get_queryset(self):
        product = get_filter_products()
        self.product_list_pk = get_products_list_pk()
        return product


class CategoryView(ShopMixin):
    """
    Shows products by category
    """
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        self.cat = Category.get_category(slug=self.kwargs['slug'])
        list_categories_pk = get_list_of_nested_category_id(slug=self.kwargs['slug'])
        product = get_filter_products(category_id__in=list_categories_pk)
        self.product_list_pk = get_products_list_pk(product)
        return product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = self.cat
        context['slug'] = self.cat.slug
        context['parent'] = self.cat.pk
        return context


class TagView(ShopMixin):
    """
    Shows products by tag
    """
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        self.tag = Tag.get_tag(self.kwargs['slug'])
        product = get_filter_products(tags=self.tag)
        self.product_list_pk = get_products_list_pk(product)
        return product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.tag
        context['slug'] = self.tag.pk
        context['parent'] = False
        return context


class BrandView(ShopMixin):
    """
    Shows products by brand
    """
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        self.brand = Manufacturer.get_brand(self.kwargs['slug'])
        product = get_filter_products(manufacturer=self.brand)
        self.product_list_pk = get_products_list_pk(product)
        return product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.brand
        context['slug'] = self.brand.pk
        context['parent'] = False
        return context


class HomeView(ListView):
    """
    Shows the main page of the site
    """
    template_name = 'shop/index.html'
    context_object_name = 'category'

    def get_queryset(self):
        return Category.get_all_categories()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Main')
        return context


class SendUserMailView(TemplateView):
    template_name = 'shop/info/contact.html'

    def post(self, request):
        """
        Sends a message from the user to the email
        """
        send_message_from_user(request)
        return render(request, self.template_name)


class ProductDetailView(DetailView):
    """
    Shows the detailed page of the product card
    """
    model = Product
    template_name = 'shop/detail.html'
    context_object_name = 'context'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        product = Product.get_product(slug=self.kwargs['slug'])
        active_size = self.request.GET.get('size')
        active_color = self.request.GET.get('color')

        context['title'] = product.title
        context['product'] = product
        context['slug'] = product.category.pk
        context['colors'] = product.get_color(available=False)
        context['form'] = ReviewsForm
        context['active_color'] = get_active_color(product=product, color=active_color)
        context['active_size'] = get_active_size(active_color=context['active_color'],
                                                 size=active_size,
                                                 )
        return context


class AboutView(TemplateView):
    template_name = 'shop/info/about-us.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('About us')


class HelpView(TemplateView):
    template_name = 'shop/info/help.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Help')


class TermsView(TemplateView):
    template_name = 'shop/info/terms.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Terms')


class ContactView(TemplateView):
    template_name = 'shop/info/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Contact')


class SearchView(ListView):
    """
    Shows the product search page
    """
    template_name = 'shop/search.html'
    paginate_by = 9
    model = Product
    context_object_name = 'products'
    allow_empty = True

    def get_queryset(self):
        """
        The search is based on the name of the product
        """
        self.text = self.request.GET.get('text')
        if self.text:
            return get_filter_products(title__icontains=self.text)
        return Product.get_all_products()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Search')
        context['text'] = f"text={self.text}&"
        context['empty'] = self.text
        return context


class AddReviewView(View):
    """
    If form valid and user is authenticated, adds a product review.
    """
    def post(self, request):
        form = ReviewsForm(request.POST)
        current = request.POST.get('current')
        add_user_review(form, request)
        return HttpResponseRedirect(current)


def custom_page_not_found_view(request, exception):
    """
    Custom page not found.
    Status 404 is required for correct operation of LocaleMiddleware
    """
    context = {'text': _('There is no such page')}
    return render(request, 'shop/page_error.html', context=context, status=404)


def custom_page_server_error(request):
    """
    Custom page server error.
    Status 500 is required for correct operation of LocaleMiddleware
    """
    context = {'text': _('Server error. Our specialists are already repairing')}
    return render(request, 'shop/page_error.html', context=context, status=500)
