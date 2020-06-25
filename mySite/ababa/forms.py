 　ｐｙてょfrom django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm): #usercreationformを継承
    def __init__(self, *args, **kwargs): #*,**はそれぞれ可変長タプル、辞書
        super().__init__(*args, **kwargs) #super()は親クラスのやつを使う時に宣言

        self.fields['username'].widget.attrs['class'] = 'form-control'

