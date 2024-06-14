from django import forms
from .models import Ocorrencia, Movimentacao
from acesso.models import Usuario
from django.forms import inlineformset_factory, BaseInlineFormSet

class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['cliente', 'empreendimento', 'operador_responsavel']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(OcorrenciaForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['operador_responsavel'].queryset = Usuario.objects.filter(pk=user.pk)

class MovimentacaoForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['comentario', 'operador_responsavel', 'status']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MovimentacaoForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['operador_responsavel'].queryset = Usuario.objects.filter(pk=user.pk)

class BaseMovimentacaoFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(BaseMovimentacaoFormSet, self).__init__(*args, **kwargs)
        for form in self.forms:
            form.user = self.user

MovimentacaoFormSet = inlineformset_factory(Ocorrencia, Movimentacao, form=MovimentacaoForm, formset=BaseMovimentacaoFormSet, fields=['comentario', 'operador_responsavel', 'status'], extra=1, can_delete=True)