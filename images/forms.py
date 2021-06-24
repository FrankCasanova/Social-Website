from django import forms
from .models import Image  # 5-5

from urllib import request  # 5-7
from django.core.files.base import ContentFile  # 5-7
from django.utils.text import slugify  # 5-7


class ImageCreateForm(forms.ModelForm):  # 5-5

    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):  # 5-6

        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jepg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('the vigen URL does not'
                                        'match valid image extensions.')

        return url

    def save(self, force_insert=False,
             force_update=False,
             commit=True):
        image = super().save(commit=False)  # that create an image instance
        # get the URL from the cleaned_data dictionary of the form
        image_url = self.cleaned_data['url']
        name = slugify(image.title)  # generate image name
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'

        # download image from the given URL
        response = request.urlopen(image_url)
        image.image.save(image_name,
                         ContentFile(response.read()),
                         save=False)
        if commit:
            image.save()
        return image
        # after that install certifi to retrieve images from URLs served HTTPS
