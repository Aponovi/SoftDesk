from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.models import Project, Contributor, Issue, Comment
from app.permissions import IsAuthor, IsContributor
from app.serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self):
        return Project.objects.all()


class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsAuthor]

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs["project_pk"])


class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsContributor]

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs["project_pk"])


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsContributor]

    def get_queryset(self):
        return Comment.objects.filter(issue=self.kwargs["issue_pk"])

