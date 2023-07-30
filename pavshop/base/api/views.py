from base.models import Team, Sponsor, Contact, Newsletter
from django.http import JsonResponse
from base.api.serializers import TeamSerializer, SponsorSerializer, ContactSerializer, NewsletterSerializer


# rest framework -> function-based
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView




# GET
def teams(request):
    team_list = Team.objects.all()
    # team_dict_list = []
    # for team in team_list:
    #     team_dict_list.append({
    #         'team_id' : team.id,
    #         'full_name' : team.full_name,
    #         # 'image' : team.image,
    #         'major' : team.major,
    #     })
    serializer = TeamSerializer(team_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)




# POST 
class TeamCreateAPIView(CreateAPIView):
    serializer_class = TeamSerializer


# # GET  - gerek urls.py da elave bir route yaradaq, o da hansi yuxarida ise o isleyecek, elverisli deyil get ve post ucun API ayri yazmaq
# class TeamCreateAPIView(ListAPIView):
#     serializer_class = TeamSerializer
#     queryset = Team.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class TeamCreateAPIView(ListCreateAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class TeamRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()





# POST 
class SponsorCreateAPIView(CreateAPIView):
    serializer_class = SponsorSerializer


# # GET  - gerek urls.py da elave bir route yaradaq, o da hansi yuxarida ise o isleyecek, elverisli deyil get ve post ucun API ayri yazmaq
# class SponsorCreateAPIView(ListAPIView):
#     serializer_class = SponsorSerializer
#     queryset = Sponsor.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class SponsorCreateAPIView(ListCreateAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class SponsorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SponsorSerializer
    queryset = Sponsor.objects.all()





# POST 
class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactSerializer


# # GET  - gerek urls.py da elave bir route yaradaq, o da hansi yuxarida ise o isleyecek, elverisli deyil get ve post ucun API ayri yazmaq
# class ContactCreateAPIView(ListAPIView):
#     serializer_class = ContactSerializer
#     queryset = Contact.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class ContactCreateAPIView(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class ContactRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()




# POST
class NewsletterCreateAPIView(CreateAPIView):
    serializer_class = NewsletterSerializer
    # queryset = Newsletter.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class NewsletterCreateAPIView(ListCreateAPIView):
    serializer_class = NewsletterSerializer
    queryset = Newsletter.objects.all()






# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def teams(request):
    if request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    team_list = Team.objects.all()
    serializer = TeamSerializer(team_list, context= {'request' : request}, many = True)
    return JsonResponse(data=serializer.data, safe=False)





# GET
def sponsors(request):
    sponsor_list = Sponsor.objects.all()
    serializer = SponsorSerializer(sponsor_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)



# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def sponsors(request):
    if request.method == 'POST':
        serializer = SponsorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    sponsor_list = Sponsor.objects.all()
    serializer = SponsorSerializer(sponsor_list, context= {'request' : request}, many = True)
    return JsonResponse(data=serializer.data, safe=False)



# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def contacts(request):
    if request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201)
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    contact_list = Contact.objects.all()
    serializer = ContactSerializer(contact_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)


