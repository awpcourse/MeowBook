from models import CatProfile


def test(request):
    cat_list = None
    if hasattr(request, 'user') and request.user.is_authenticated():
        cat_list = CatProfile.objects.filter(user=request.user)
    return {"cats": cat_list}