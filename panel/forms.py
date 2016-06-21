from django import forms

from .models import panel

class panelForm(forms.ModelForm):
	class Meta:
		model = panel
		fields = [
			"title",
			"description",
			"image",
			"cells",
			"draft",
			"publish",
		]