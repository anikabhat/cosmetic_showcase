from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Product, Feedback
from .forms import FeedbackForm
from .forms import ContactForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from .models import Feedback, ContactMessage

# Homepage: Product List (8 products)
class HomeListView(ListView):
    model = Product
    template_name = "hello/home.html"
    context_object_name = "product_list"

# Product Detail: Info + Comment Box + Blog-style feedback
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    feedbacks = product.feedbacks.all()
    
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = FeedbackForm()
        
    return render(request, "hello/product_detail.html", {
        "product": product, 
        "feedbacks": feedbacks, 
        "form": form
    })

# Admin-only Report
@staff_member_required
def feedback_report(request):
    # This gathers every review from every product into one list
    all_feedback = Feedback.objects.all().order_by('-created_at')
    return render(request, "hello/feedback_report.html", {
        "all_feedback": all_feedback
    })

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")




def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent! We will look into adding those products.")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "hello/contact.html", {"form": form})


