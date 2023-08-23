from rest_framework import generics, viewsets
from .models import Item, Location
from .serializers import ItemSerializer, LocationSerializer

class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')

        if location is not None:
            queryset = queryset.filter(item_location=location)
        
        return queryset


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

