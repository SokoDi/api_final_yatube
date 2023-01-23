from rest_framework import mixins, viewsets


class PackMix(mixins.CreateModelMixin,
              mixins.ListModelMixin,
              viewsets.GenericViewSet):
    pass
