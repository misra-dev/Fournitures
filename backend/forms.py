from django import forms

from backend.models import Category, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['cat_name']

        widgets = {
            'cat_name': forms.TextInput(
                attrs={
                    'class': 'form-control', 'placeholder': 'Saisir une catégorie', 'id': 'id'
                }
            ),

            'id': forms.TextInput(attrs={'type': 'hidden', 'name': 'id', 'id': 'id'})
        }


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.none(),
        empty_label="Choisir une catégorie",
        widget=forms.Select(attrs={'class': 'form-select form-control input-with-bottom-line',
                                   'type': 'text', 'id': 'catField'})
    )

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control input-with-bottom-line',
                    'placeholder': 'Saisir le nom du produit',
                    'type': 'text', 'required': True
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control input-with-bottom-line', 'placeholder': 'Saisir le prix',
                    'type': 'number', 'required': True
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'class': 'form-control input-with-bottom-line',
                    'placeholder': 'Saisir la quantité',
                    'type': 'number', 'required': True
                }
            ),
            'thumbnail': forms.TextInput(
                attrs={
                    'class': 'form-control input-with-bottom-line',
                    'placeholder': 'Selectionnez une image',
                    'type': 'file'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control input-with-bottom-line',
                    'placeholder': 'Description',
                    'rows': 3
                }
            )
        } # Fin widgets
    # Fin Meta:

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()  # Chargement dynamique
