from django.shortcuts import render
# from django.views import generic
from django.views.generic import TemplateView

# def home(request):
#     return render(request, 'templates/home.html')

# request変数はもともとDjangoが用意している変数。アクセスしているユーザーのURLやIPなどのアクセス情報が詰まっている。

class home(TemplateView):
    template_name = 'home.html'
    # def get_context_data(self):
        # super()は親クラスを継承して、メソッドを呼び出すことができる。この中にuserなどの変数が入っている。
        # ctxt = super().get_context_data()
        # コンテキストの値は辞書形式。たぶんここにmodelのデータを入れるようにすれば画面に名前などを反映させることができる。
        # ctxt['user_name']= 'Keisuke'
        # return ctxt

class matching(TemplateView):
    template_name = 'matching.html'

class message(TemplateView):
    template_name = 'message.html'

class profile(TemplateView):
    template_name = 'profile.html'
    # def get_context_data(self):
    #     # super()は親クラスを継承して、メソッドを呼び出すことができる。この中にuserなどの変数が入っている。
    #     ctxt = super().get_context_data()
    #     # コンテキストの値は辞書形式。たぶんここにmodelのデータを入れるようにすれば画面に名前などを反映させることができる。
    #     # ctxt['user_name']= 'Keisuke'
    #     # ctxt['age']= 23
    #     # ctxt['address']= 'Tokyo'
    #     # ctxt['blood_type']= 'A'
    #     # ctxt['hobbys']= ['game'
    #     #                 ,'basketball'
    #     #                 ,'run']
    #     return ctxt

