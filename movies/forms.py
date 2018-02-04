from django import forms

class BrowseForm (forms.Form):
    search= forms.CharField(required=False , widget=forms.TextInput(attrs={'class': 'form-control',}))

    GenresType = (('', 'All'), ('Action', 'Action'),('Adventure','Adventure'), ('Comedy', 'Comedy'), ('Crime', 'Crime'),
                  ('Drama', 'Drama'), ('Horro', 'Horro'),('History','History'))
    genre=forms.ChoiceField(choices=GenresType,label='',initial='', widget=forms.Select(attrs={'class': 'spinner',}), required=False)

    SortBy = (("production_date", 'Production Date'), ("name", 'Name'))
    sort = forms.ChoiceField(choices=SortBy,label='',initial='', widget=forms.Select(attrs={'class': 'spinner', }), required=False)