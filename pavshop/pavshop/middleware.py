from django.utils.deprecation import MiddlewareMixin
from base.models import BlockedIps

class SaveIpAdressMiddleware(MiddlewareMixin):
    

    def process_request(self, request):
        print(request.META.get('REMOTE_ADDR'))  
        # bu bize daxil oldugumuz IP adresi verir
        # local'da oldugumuz ucun hazir ki 127.0.0.1 verecek, amma serverde olanda serverin IP adresini verir
        if request.user.is_authenticated:
            ip_address = request.META.get('REMOTE_ADDR')
            if not request.user.ips:
                request.user.ips = []
            if ip_address not in request.user.ips:
                request.user.ips.append(ip_address)
            return request.user.save()





class BlockIpAddress(MiddlewareMixin):
    def process_request(self, request):
        print(request.META.get('REMOTE__ADDR'))

        ip = request.META.get('REMOTE_ADDR')
        x = BlockedIps.objects.filter(ip_address = ip)
        if x:
            raise PermissionError("You are blocked")