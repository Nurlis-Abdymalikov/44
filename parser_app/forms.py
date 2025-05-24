from django import forms
from . import models, parser_movie 

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('movie.ag', 'movie.ag'),
       
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]
    
    def parser_data(self):
        if self.data['media_type'] == 'movie.ag':
            movie_films = parser_movie.parsing_movie()
            for i in movie_films:
                models.Parser_Movie.objects.create(**i)
