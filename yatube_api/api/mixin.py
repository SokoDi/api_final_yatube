from rest_framework import mixins, viewsets


class PackMixin(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    pass
