from django.core.exceptions import ValidationError
from django import forms
from .models import ExcelFile
from excel_upload import excel_parser


class ExcelForm(forms.ModelForm):
    class Meta:
        model = ExcelFile
        fields = ('excel',)

    # def clean_excel(self):
    #     file = self.cleaned_data['excel']
    #     # file_extension = os.path.splitext(value.name)[1]
    #     # if not (file_extension == '.xls' or file_extension == 'xlsx'):
    #     #     print("not valid extension")
    #     #     raise ValidationError(
    #     #         ('Not a valid excel file.'),
    #     #         code='invalid'
    #     #     )

    #     if not excel_parser.verifyExcel(file):
    #         print("not valid excel")
    #         raise ValidationError(
    #             ('Not a valid excel file.'),
    #             code='invalid'
    #         )

    #     if not excel_parser.verifyTemplate(file):
    #         print("not valid template")
    #         raise ValidationError(
    #             ('Not a valid invoice book template.'),
    #             code='invalid'
    #         )
