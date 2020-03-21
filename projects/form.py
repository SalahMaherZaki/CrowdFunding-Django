from .models import Comment ,Report
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['report_content']

