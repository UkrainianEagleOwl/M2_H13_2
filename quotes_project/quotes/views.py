from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Quote, Author, Tag
from .forms import AuthorForm,QuoteForm


def main(request, page = 1):
    quotes = Quote.objects.all()
    
    per_page = 10
    
    paginator = Paginator(list(quotes),per_page)
    quotes_on_page = paginator.page(page)
    
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'quotes/author.html', {"author": author})

@login_required
def new_author(request):

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            new_author = form.save()

            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/new_author.html', {'form': form})

    return render(request, 'quotes/new_author.html', {'form': AuthorForm()})

@login_required
def new_quote(request):
    tags = Tag.objects.all()
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            
            # Fix the way you assign the author
            author_name = request.POST.get('author')
            choice_author = Author.objects.filter(fullname=author_name).first()
            if choice_author:
                new_quote.author = choice_author
                new_quote.save()  # Save the quote after assigning the author

            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/new_quote.html', {"tags": tags, 'authors': authors, 'form': form})

    return render(request, 'quotes/new_quote.html', {"tags": tags, 'authors': authors, 'form': QuoteForm()})



