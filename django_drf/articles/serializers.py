from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('id', 'title', 'content')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)
        depth = 1

class ArticleSerializer(serializers.ModelSerializer):
    # comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True) related_name을 설정하면 comment_set으로 설정된 default name을 바꿀 수 있다.
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # 모든 댓글 정보를 출력하려면 CommentSeralizer
    comment_set = CommentSerializer(many=True, read_only=True)
    # 댓글 개수 확인
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # 첫번째 댓글 확인
    # comment_first = serializers.CharField(source='comment_set.furst', read_only=True)
    # 첫 댓글의 모든 내용 가져오기
    comment_first = CommentSerializer(source='coment_set.first', read_only=True)
    # 특정 조건 댓글 찾기(id 값이 15 이하인 댓글 찾기)
    comment_filter = serializers.SerializerMethodField('less_15')

    def less_15(self, article):
        print(article) # views.py article_detail에서 들고온 article instance
        qs = Comment.objects.filter(pk__lte=15, article=article)
        serializer = CommentSerializer(instance=qs, many=True)
        return serializer.data

    class Meta:
        model = Article
        fields = '__all__'
