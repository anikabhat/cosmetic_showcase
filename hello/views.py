from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Product, Feedback
from .forms import FeedbackForm

# Homepage: Product List (Minimum 8 products)
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
def feedback_report(request):
    all_feedback = Feedback.objects.all().order_by('-created_at')
    return render(request, "hello/feedback_report.html", {"all_feedback": all_feedback})

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")