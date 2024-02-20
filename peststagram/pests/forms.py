from django import forms
from peststagram.pests.models import Pest
from typing import Union


class PestBaseForm(forms.ModelForm):
    class Meta:
        model = Pest
        fields = ["name", "date_of_sight", "photo"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Pest name"}),
            "date_of_sight": forms.DateTimeInput(attrs={"type": "date"}),
            "photo": forms.TextInput(attrs={"placeholder": "Link to image"}),
        }
        labels = {
            "name": "Pest name",
            "date_of_sight": "Date of sight",
            "photo": "Link to Image",
        }


class PestAddForm(PestBaseForm):
    pass


class PestEditForm(PestBaseForm):
    pass


class PestDeleteForm(PestBaseForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.attrs["readonly"] = "readonly"

    def save(self, commit=True) -> Union[Pest, None]:
        if commit:
            self.instance.delete()
        return self.instance
