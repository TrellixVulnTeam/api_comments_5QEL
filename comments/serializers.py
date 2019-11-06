from rest_framework import serializers

from .models import Address, Comment, Post, User


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('street', 'suite', 'city', 'zip_code',)


class UserSerializer(serializers.ModelSerializer):
    address = serializers.SlugRelatedField(queryset=Address.objects.all(), slug_field='zip_code')

    class Meta:
        model = User
        fields = ('name', 'username', 'phone', 'website', 'email', 'address', 'company')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    post_id = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ('email', 'body', 'post_id', 'name', 'date',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'body', 'date', 'user_id', 'comments',)


class DatabaseSerializer(serializers.Serializer):
    file = serializers.FileField()