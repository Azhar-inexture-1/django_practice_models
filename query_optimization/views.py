from django.shortcuts import render
from .models import Book, Shope


def home(request):
    # qs = Post.objects.all()
    # # The DB query has not been executed at this point
    # x = qs
    # # Just assigning variables doesn't do anything
    # for x in qs:
    #     print(x)
    # # The query is executed at this point, on iteration
    # for x in qs:
    #     print("%d" % x.id)
    # # The query is not executed this time, due to caching

    post_qs = Book.objects.order_by('id')
    for start, end, total, qs in batch_qs(post_qs):
        print("Now processing %s - %s of %s" % (start + 1, end, total))
        for post in qs:
            print(post.name)
    return render(request, 'query_optimization/home.html')


def batch_qs(qs, batch_size=10):
    """
    Returns a (start, end, total, queryset) tuple for each batch in the given
    queryset.
    
    Usage:
        # Make sure to order your querset
        article_qs = Article.objects.order_by('id')
        for start, end, total, qs in batch_qs(article_qs):
            print "Now processing %s - %s of %s" % (start + 1, end, total)
            for article in qs:
                print article.body
    """
    total = qs.count()
    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        yield (start, end, total, qs[start:end])



# def home(request):
#     books = Book.objects.all().only("name", "create_date")
#     for each in books:
#         print(each.name)
#     print(f"Cache {books._result_cache}")
#     return render(request, 'query_optimization/home.html')


def home(request):
    queryset = Shope.objects.prefetch_related('book').all()
    stores = []
    for store in queryset:
        books = [book.name for book in store.book.all()]
        stores.append({'id': store.id, 'name': store.name, 'books': books})
    return render(request, 'query_optimization/home.html')


    queryset = Store.objects.prefetch_related(
            Prefetch('books', queryset=Book.objects.filter(price__range=(250, 300))))


