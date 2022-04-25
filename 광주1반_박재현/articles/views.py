from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_list_or_404, get_object_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    # Q 2.
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # Q 3.
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    # Q 4.
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': article_pk,
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    # Q 5.
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    # Q 7.
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    # Q 8.
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE'])
def comment_detail(request, comment_pk):
    # Q 9.
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    # Q 10.
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': comment_pk,
        }
        return Response(data)

