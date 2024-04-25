from .serializers import PositionSerializer, TagSerializer
from .models import Position,Comment,Order
from rest_framework import permissions, generics, pagination, viewsets, filters
from taggit.models import Tag
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer,CommentSerializer,OrderSerializer
from .models import Comment


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    ordering = 'added_at'

#Позиции меню
class PositionViewSet(viewsets.ModelViewSet):
    search_fields = ['$name']
    filter_backends = (filters.SearchFilter,)
    serializer_class = PositionSerializer
    queryset = Position.objects.all()
    lookup_field = 'slug'
    permission_classes = [permissions.AllowAny]
    pagination_class = PageNumberSetPagination

#ТЕГИ
class TagDetailView(generics.ListAPIView):
    serializer_class = PositionSerializer
    pagination_class = PageNumberSetPagination
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug'].lower()
        tag = Tag.objects.get(slug=tag_slug)
        return Position.objects.filter(tags=tag)

class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]

#Последние пара позиций
class AsideView(generics.ListAPIView):
    queryset = Position.objects.all().order_by('-id')[:3]
    serializer_class = PositionSerializer
    permission_classes = [permissions.AllowAny]

#РЕГИСТРАЦИЯ  и ПРОФИЛЬ
class RegisterView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "Пользователь успешно создан",
        })


class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return Response({
            "user": UserSerializer(request.user, context=self.get_serializer_context()).data,
        })

#ОТЗЫВЫ
class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        position_slug = self.kwargs['position_slug'].lower()
        position = Position.objects.get(slug=position_slug)
        return Comment.objects.filter(position=position)
    
# ЗАКАЗЫ
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        position_slug = self.kwargs['position_slug'].lower()
        position = Position.objects.get(slug=position_slug)
        return Order.objects.filter(position=position)