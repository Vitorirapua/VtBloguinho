from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.validators import MinLengthValidator, MaxLengthValidator


class NewPost(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='static/bloguinho/images/')
    title = models.CharField(
        max_length=127,
        validators=[
            MinLengthValidator(5, "O título deve ter pelo menos 5 caracteres.")
        ],
        blank=False
    )
    content = models.TextField(
        validators=[
            MinLengthValidator(
                10, "O conteúdo deve ter pelo menos 10 caracteres."),
            MaxLengthValidator(
                255, "O conteúdo deve ter no máximo 255 carateres.")
        ],
        blank=False
    )
    expires = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[
            ('on', 'Online'),
            ('off', 'Offline'),
            ('del', 'Apagado')
        ],
        default='on'
    )
    max_image = {
        'size': 50,  # Tamanho máximo da imagem em MB
        'width': 256,  # Largura máxima da imagem
        'height': 256,  # Altura máxima da imagem
    }

    def clean(self):
        if len(self.content) > 255:
            raise ValidationError(
                'A imagem não pode exceder 255 caracteres.')

        # Bloqueia imagens maiores que max_image['size']
        if self.image and self.image.size > self.max_image['size'] * 1024 * 1024:
            raise ValidationError(f'A imagem não pode exceder {
                                  self.max_image['size']} MB.')

    def save(self, *args, **kwargs):

        # Redimensionar a imagem antes de salvar
        if self.image:
            img = Image.open(self.image)

            if img.height > self.max_image['height'] or img.width > self.max_image['width']:
                output_size = (
                    self.max_image['height'],
                    self.max_image['width']
                )
                img.thumbnail(output_size)

                # Salvar a imagem redimensionada em memória
                img_io = io.BytesIO()
                img.save(img_io, format='PNG')
                img_io.seek(0)

                # Substituir a imagem original pela redimensionada
                self.image = InMemoryUploadedFile(
                    img_io, 'ImageField', self.image.name, 'image/png', img_io.getbuffer().nbytes, None
                )

        self.full_clean()
        super().save(*args, **kwargs)
