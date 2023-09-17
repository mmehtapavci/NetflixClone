from.models import *

def get_profiles(request):
    profiller = Profile.objects.filter(user = request.user) if request.user.is_authenticated else ''
    # Bu aşağıdaki işlem tek satırda for döngüsü yazma işlemidir.Yukarıdaki authenticated yöntemi ile aynıdır.
    # profiller = Profile.objects.filter(user = request.user) if request.user.is_authenticated else ''
    
    
    context = {
        'profiller':profiller
    }
    return context