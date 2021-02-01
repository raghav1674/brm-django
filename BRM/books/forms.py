from django import forms


# Create your forms here.

class BookForm(forms.Form):
    title = forms.CharField(label='Title',max_length=30)
    author = forms.CharField(label='Author Name',max_length=60)
    price = forms.FloatField(label='Price')
    publisher = forms.CharField(label='Publisher',max_length=120)


    def __str__(self):
        return f'{self.title} - {self.author}'
