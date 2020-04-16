from rest_framework import serializers

from users.serializers import PersonSerializer

from post.models import Internship


class InternshipSerializer(serializers.ModelSerializer):

    user = PersonSerializer(
        read_only=True
    )

    # bookmark = serializers.SerializerMethodField('is_bookmark')

    class Meta:
        model = Internship
        exclude = ['bookmarks']

    # def is_bookmark(self, obj):
    #     person = self.context.get('user', None)
    #     starred_posts = obj.bookmarks.all()

    #     return starred_posts.filter(person=person).exists()
