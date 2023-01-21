# TODO:  Напишите свой вариант
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import PermissionDenied
from rest_framework.pagination import LimitOffsetPagination


from posts.models import Group, Post, Comment, Follow
from .serializers import GroupSerializer, PostSerializer, CommentSerializer, FollowSerializer
from .permissions import AuthorOrReadOnly, ReadOnly

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AuthorOrReadOnly,)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = PageNumberPagination


    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        super(CommentViewSet, self).perform_destroy(serializer)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    pagination_class = PageNumberPagination
    

    def perform_create(self, serializer):
        serializer.save(Following=self.request.user)
