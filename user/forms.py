from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput, required=False)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı", required=False)
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput, required=False)
    confirm  = forms.CharField(max_length=20, label="Parolayı doğrulayınız", widget=forms.PasswordInput, required=False)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm  = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Girilen parolalar uyuşmuyor...")
        if not username or not password or not confirm:
            raise forms.ValidationError("Kullanıcı adı ve parola alanı boş bırakılamaz...")


        values = {
            "username" : username,
            "password" : password,
                 }
        return values
