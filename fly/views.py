from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    # If no posts yet, show demo data
    if not posts.exists():
        demo_posts = [
            {'title': 'Private Jet Lagos to Abuja', 'location': 'Lagos', 'price': 4500000, 'content': 'Gulfstream G650 - Luxury 8 seater', 'image_url': 'https://images.unsplash.com/photo-1540962351504-03099e0a754b?w=600'},
            {'title': 'Helicopter Tour Over Abuja', 'location': 'Abuja', 'price': 800000, 'content': '30 mins aerial view of Aso Rock', 'image_url': 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=600'},
            {'title': 'Business Class to Calabar', 'location': 'Calabar', 'price': 1200000, 'content': 'Challenger 350 - Perfect for weekend getaway', 'image_url': 'https://images.unsplash.com/photo-1556388158-158ea5ccacbd?w=600'},
        ]
        return render(request, 'post/post_list.html', {'posts': demo_posts, 'demo': True})
    return render(request, 'post/post_list.html', {'posts': posts})
