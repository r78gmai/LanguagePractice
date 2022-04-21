from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))

  #multiprocessing モジュールでは、threading モジュールには似たものが存在しない API も導入されています。その最たるものが Pool オブジェクトです。これは複数の入力データに対して、サブプロセス群に入力データを分配 (データ並列) して関数を並列実行するのに便利な手段を提供します。以下の例では、モジュール内で関数を定義して、子プロセスがそのモジュールを正常にインポートできるようにする一般的な方法を示します。 Pool を用いたデータ並列の基礎的な例
