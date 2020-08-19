from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ideas.api.permissions import IsAuthorOrReadOnly
from ideas.api.serializers import CommentsSerializer, IdeasSerializer
from ideas.models import Comments, Ideas


class IdeasViewSet(viewsets.ModelViewSet):
    queryset = Ideas.objects.all()
    lookup_field = "slug"
    serializer_class = IdeasSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsCreateAPIView(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        idea = get_object_or_404(Ideas, slug=kwarg_slug)

        if idea.comments.filter(author=request_user).exists():
            raise ValidationError("You have already commented on this topic")

        serializer.save(author=request_user, idea=idea)


class CommentsListAPIView(generics.ListAPIView):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get("slug")
        return Comments.objects.filter(idea__slug=kwarg_slug).order_by("-created_at")


class CommentsRUDAPIView(generics.RetrieveUpdateDestroyAPIView):  # Gives the CRUD ability.
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class CommentLikeAPIView(APIView):
    serializer_class = CommentsSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        comment = get_object_or_404(Comments, pk=pk)
        user = request.user

        comment.voters.remove(user)
        comment.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        comment = get_object_or_404(Comments, pk=pk)
        user = request.user

        comment.voters.add(user)
        comment.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


