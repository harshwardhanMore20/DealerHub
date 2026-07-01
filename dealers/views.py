from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Dealer, Review


def home(request):
    dealers = Dealer.objects.all()
    state = request.GET.get('state')
    if state:
        dealers = dealers.filter(state__icontains=state)
    return render(request, 'dealers/home.html', {'dealers': dealers, 'state': state})


def dealer_detail(request, pk):
    dealer = get_object_or_404(Dealer, pk=pk)
    reviews = dealer.reviews.all().order_by('-created_at')
    avg_rating = dealer.reviews.aggregate(avg=Avg('rating'))['avg'] or 0
    return render(request, 'dealers/dealer_detail.html', {'dealer': dealer, 'reviews': reviews, 'avg_rating': avg_rating})


def about(request):
    team = [
        {'name': 'Ava Johnson', 'role': 'Founder & CEO', 'details': 'Leads strategy and customer experience.', 'email': 'ava@dealers.com', 'image': 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=80'},
        {'name': 'Liam Chen', 'role': 'Operations Director', 'details': 'Oversees service quality and dealer partnerships.', 'email': 'liam@dealers.com', 'image': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80'},
        {'name': 'Mia Patel', 'role': 'Product Designer', 'details': 'Creates polished, intuitive experiences for buyers.', 'email': 'mia@dealers.com', 'image': 'https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?auto=format&fit=crop&w=400&q=80'},
    ]
    return render(request, 'dealers/about.html', {'team': team})


def contact(request):
    return render(request, 'dealers/contact.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            return render(request, 'dealers/register.html', {'error': 'Username already exists'})
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        login(request, user)
        return redirect('home')
    return render(request, 'dealers/register.html')


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        return render(request, 'dealers/login.html', {'error': 'Invalid credentials'})
    return render(request, 'dealers/login.html')


@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def post_review(request, pk):
    dealer = get_object_or_404(Dealer, pk=pk)
    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        rating = int(request.POST.get('rating', 5))
        Review.objects.create(dealer=dealer, user=request.user, rating=rating, comment=comment)
        return redirect('dealer_detail', pk=dealer.pk)
    return render(request, 'dealers/post_review.html', {'dealer': dealer})


def api_dealers(request):
    dealers = list(Dealer.objects.values('id', 'name', 'state', 'city', 'address', 'phone', 'email'))
    return JsonResponse({'dealers': dealers})


def api_dealer_detail(request, pk):
    dealer = get_object_or_404(Dealer, pk=pk)
    data = {
        'id': dealer.id,
        'name': dealer.name,
        'state': dealer.state,
        'city': dealer.city,
        'address': dealer.address,
        'phone': dealer.phone,
        'email': dealer.email,
    }
    return JsonResponse(data)


def api_reviews(request, pk):
    dealer = get_object_or_404(Dealer, pk=pk)
    reviews = list(dealer.reviews.values('id', 'comment', 'rating', 'created_at', 'user__username'))
    return JsonResponse({'reviews': reviews})


def api_car_makes(request):
    data = [
        {'make': 'Toyota', 'model': 'Camry'},
        {'make': 'Honda', 'model': 'Civic'},
        {'make': 'Ford', 'model': 'F-150'},
    ]
    return JsonResponse({'cars': data})


def analyze_review(request):
    review_text = request.GET.get('text', 'Fantastic services')
    text = review_text.lower()
    sentiment = 'positive' if any(word in text for word in ['fantastic', 'great', 'excellent', 'good', 'love']) else 'neutral'
    return JsonResponse({'text': review_text, 'sentiment': sentiment})
