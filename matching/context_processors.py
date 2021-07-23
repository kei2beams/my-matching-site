from django.http import HttpRequest

# コンテクストプロセッサで共通の変数を保管しておけるので、すべてのtemplate内で変数が利用できる。
def some_processor(request: HttpRequest):
    # 何かテンプレートコンテキストに追加するものを生成
    # dic = create_dict()
    # return dic
    return {
        # 'some_test_msg': '後から効いてくるスパイス'
        'user_name': 'Keisuke'
        ,'age': 23
        ,'address': 'Tokyo'
        ,'blood_type': 'A'
        ,'hobbys': ['game','basketball','run']
        }