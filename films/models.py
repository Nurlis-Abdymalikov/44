from django.db import models

class Film(models.Model):
    GENRE = (
        ('Фантастика','Фантастика'),
        ('Ужасы','Ужасы'),
        ('История','История')
    )
    image = models.ImageField(upload_to='films/', verbose_name='Загрузите фильм')
    title = models.CharField(max_length=100, verbose_name='Укажите название фильма')
    create_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=100, choices=GENRE, verbose_name='Укажите жанр', default='История')
    author = models.CharField(max_length=100, default='Иван Петрович')
    description = models.TextField(verbose_name='Укажите описание фильма')
    audio_film = models.URLField(verbose_name='Вставьте ссылку аудио фильма')
    views = models.PositiveIntegerField(
        default=0, verbose_name="Количество просмотров", null=True
    )  # Поле просмотров

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'Фильмы'
    

class Reviews(models.Model):
    films_choice = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')
    user_name = models.CharField(max_length=100, verbose_name='Как вас зовут ?')
    text = models.TextField(verbose_name='как вам фильм ?')

    def __str__(self):
        return f'{self.films_choice}-{self.user_name}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'коментарии'
