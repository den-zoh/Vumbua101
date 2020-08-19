from rest_framework import serializers
from ideas.models import Ideas, Comments


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()

    class Meta:
        model = Comments
        exclude = ['idea', 'voters', 'updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d %B %Y")

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()


class IdeasSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    comments_count = serializers.SerializerMethodField()
    user_has_commented = serializers.SerializerMethodField()

    class Meta:
        model = Ideas
        exclude = ['updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d %B %Y")

    def get_comments_count(self, instance):
        return instance.comments.count()

    def get_user_has_commented(self, instance):
        request = self.context.get("request")
        return instance.comments.filter(author=request.user).exists()
