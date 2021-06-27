from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from utils.models import Box, Fefco, Layer

from utils.forms import BoxModelForm, StockModelForm, FefcoModelForm, LayerModelForm

import stripe
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView, View

from utils.forms import CheckoutForm
from utils.models import Box, Fefco, Order, CheckoutAddress, Payment, OrderItem

from .models import (
    Box,
    Order,
    OrderItem,
    CheckoutAddress,
    Payment
)
from django.conf import settings

stripe.api_key = settings.STRIPE_KEY

def boxes(request):
    box_list = Box.objects.all()

    return render(request, template_name='goods_full_list.html', context={'boxes': box_list})



#from django.contrib.auth.mixins import PermissionRequiredMixin, AccessMixin


class StaffRequiredMixin(UserPassesTestMixin):
  def test_func(self):
    return self.request.user.is_staff

class BoxesListView(PermissionRequiredMixin, ListView, StaffRequiredMixin):
    permission_required = 'utils.utils'
    template_name = 'goods_list.html'
    model = Box

    def handle_no_permission(self):
        return redirect('bad-auth/')

class BoxUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Box
    form_class = BoxModelForm
    success_url = reverse_lazy('utils')
    permission_required = 'utils.utils'

    def handle_no_permission(self):
        return redirect('/')

class BoxDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'box_confirm_delete.html'
    model = Box
    success_url = reverse_lazy('utils')

    permission_required = 'utils.utils'

    def handle_no_permission(self):
        return redirect('/')

class ToStockUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Box
    form_class = StockModelForm
    success_url = reverse_lazy('utils')

    permission_required = 'utils.utils'

    def handle_no_permission(self):
        return redirect('/')

class BoxCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = BoxModelForm
    success_url = reverse_lazy('utils')

    permission_required = 'utils.utils'

    def handle_no_permission(self):
        return redirect('/')

class FefcoListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    template_name = 'fefco_list.html'
    model = Fefco

    permission_required = 'utils.utils'

    def handle_no_permission(self):
        return redirect('/')

class FefcoCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = FefcoModelForm
    success_url = reverse_lazy('utils')

    permission_required = 'utils.utils'

    def handle_no_permission(self):
        return redirect('/')

class FefcoUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Fefco
    form_class = FefcoModelForm
    success_url = reverse_lazy('utils/fefco')

    permission_required = 'utils.utils'

    def handle_no_permission(self):
        return redirect('/')

class LayerListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    template_name = 'layer_list.html'
    model = Layer

    permission_required = 'utils.utils'

    def handle_no_permission(self):
        return redirect('/')

class LayerCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = FefcoModelForm
    success_url = reverse_lazy('utils')

    permission_required = 'utils.utils'

    def handle_no_permission(self):
        return redirect('/')

class LayerUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Layer
    form_class = LayerModelForm
    success_url = reverse_lazy('utils/layer')

    permission_required = 'utils.utils'

    def handle_no_permission(self):
        return redirect('/')





class ProductView(DetailView):
    model = Box
    template_name = "product.html"


class FrontView(TemplateView):
    template_name = 'front.html'

class AuthFrontView(TemplateView):
    template_name = 'auth.html'


class AboutView(TemplateView):
    template_name = 'about.html'

class HowToShopView(TemplateView):
    template_name = 'how.html'

class ConditionsView(TemplateView):
    template_name = 'conditions.html'

class CompleteListView(ListView):
    template_name = 'front_full_list.html'
    model = Box

class ProductDetailView(DetailView):
    model = Box
    template_name = 'product_detail.html'


    #queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class FefcoView(ListView):
    template_name = 'fefco_front_list.html'
    model = Fefco

class FrontFefcoListView(ListView):
    template_name = "front_fefco_list.html"
    context_object_name = "fefcolist"

    def get_queryset(self):
        content = {
            'fefcotype': self.kwargs['fefco'],
            'products': Box.objects.filter(fefco__fefco_code=self.kwargs['fefco'])
        }
        return content

class FrontLayerListView(ListView):
    template_name = "front_layer_list.html"
    context_object_name = "layerlist"

    def get_queryset(self):
        content = {
            'layertype': self.kwargs['layer'],
            'products': Box.objects.filter(layer__id=self.kwargs['layer'])
        }
        return content

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("/")

class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        order = Order.objects.get(user=self.request.user, ordered=False)
        context = {
            'form': form,
            'order': order
        }
        return render(self.request, 'checkout.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                apartment_address = form.cleaned_data.get('apartment_address')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                # TODO: add functionaly for these fields
                # same_billing_address = form.cleaned_data.get('same_billing_address')
                # save_info = form.cleaned_data.get('save_info')
                payment_option = form.cleaned_data.get('payment_option')

                checkout_address = CheckoutAddress(
                    user=self.request.user,
                    street_address=street_address,
                    apartment_address=apartment_address,
                    country=country,
                    zip=zip
                )
                checkout_address.save()
                order.checkout_address = checkout_address
                order.save()

                if payment_option == 'S':
                    return redirect('payment', payment_option='stripe')
                elif payment_option == 'P':
                    return redirect('payment', payment_option='paypal')
                else:
                    messages.warning(self.request, "Invalid Payment option")
                    return redirect('checkout')

        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("order-summary")

class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        context = {
            'order': order
        }
        return render(self.request, "payment.html", context)

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        token = self.request.POST.get('stripeToken')
        amount = int(order.get_total_price() * 100)  #cents

        try:
            charge = stripe.Charge.create(
                amount=amount,
                currency="usd",
                source=token
            )

            # create payment
            payment = Payment()
            payment.stripe_id = charge['id']
            payment.user = self.request.user
            payment.amount = order.get_total_price()
            payment.save()

            # assign payment to order
            order.ordered = True
            order.payment = payment
            order.save()

            messages.success(self.request, "Success make an order")
            return redirect('/')

        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get('error', {})
            messages.error(self.request, f"{err.get('message')}")
            return redirect('/')

        except stripe.error.RateLimitError as e:
            # Too many requests made to the API too quickly
            messages.error(self.request, "To many request error")
            return redirect('/')

        except stripe.error.InvalidRequestError as e:
            # Invalid parameters were supplied to Stripe's API
            messages.error(self.request, "Invalid Parameter")
            return redirect('/')

        except stripe.error.AuthenticationError as e:
            # Authentication with Stripe's API failed
            # (maybe you changed API keys recently)
            messages.error(self.request, "Authentication with stripe failed")
            return redirect('/')

        except stripe.error.APIConnectionError as e:
            # Network communication with Stripe failed
            messages.error(self.request, "Network Error")
            return redirect('/')

        except stripe.error.StripeError as e:
            # Display a very generic error to the user, and maybe send
            # yourself an email
            messages.error(self.request, "Something went wrong")
            return redirect('/')

        except Exception as e:
            # Something else happened, completely unrelated to Stripe
            messages.error(self.request, "Not identified error")
            return redirect('/')





@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Box, pk=pk )
    order_item, created = OrderItem.objects.get_or_create(
        item = item,
        user = request.user,
        ordered = False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added quantity Item")
            return redirect("order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "Item added to your cart")
            return redirect("order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item added to your cart")
        return redirect("order-summary")

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Box, pk=pk )
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order_item.delete()
            messages.info(request, "Item \""+order_item.item.item_name+"\" remove from your cart")
            return redirect("order-summary")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("product", pk=pk)
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("product", pk = pk)


@login_required
def reduce_quantity_item(request, pk):
    item = get_object_or_404(Box, pk=pk )
    order_qs = Order.objects.filter(
        user = request.user,
        ordered = False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists() :
            order_item = OrderItem.objects.filter(
                item = item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("order-summary")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("order-summary")
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("order-summary")

def search_product(request):
    """ search function  """
    if request.method == "GET":
        query_name = request.GET.get('name', None)
        if query_name:
            results = Box.objects.filter(Q(name__icontains=query_name)|Q(fefco__fefco_code__icontains=query_name)|Q(layer__layer__icontains=query_name)|Q(color__icontains=query_name))
            #results | =
            return render(request, 'search.html', {"item_list":results})

    return render(request, 'search.html')

class SearchView(ListView):
    model = Box
    template_name = "search.html"