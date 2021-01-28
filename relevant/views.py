from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views import generic
from relevant.forms import RelevantForm
from relevant.models import Relevant


User = get_user_model()


class UserList(generic.ListView):
    template_name = 'relevant/user_list.html'
    context_object_name = 'user_list'
    model = User

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # ログインユーザーを取得して ログインユーザー以外のQuerysetを返す
        user = self.request.user
        qs = User.objects.exclude(pk=user.id).order_by('last_login')
        ctx['qs'] = qs
        ctx['form'] = RelevantForm()
        return ctx

    def post(self, *args, **kwargs):
        """
        お気に入りユーザーを登録
        すでにRelevantに登録済みなら更新、未登録ならインスタンスを新規作成
        """
        if self.request.method == 'POST':
            try:
                Relevant.objects.get(user=self.request.user)
            except Relevant.DoesNotExist:
                user_obj = User.objects.get(pk=self.request.user.pk)
                rl_obj = Relevant.objects.create(user=user_obj)
                form = RelevantForm(self.request.POST, instance=rl_obj)
            else:
                obj = Relevant.objects.get(user=self.request.user.pk)
                form = RelevantForm(self.request.POST, instance=obj)
            finally:
                if form.is_valid():
                    form.save()
        return redirect('relevant:user_list')