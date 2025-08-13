import math
import time 

# 時間計測スタート
start = time.time()

# 定数
N = 500   # ポート数
a = 100  # スイッチ数

max_nk = 0
best_params = None

# 全探索
for k in range(1, a + 1):
    for v in range(1, a + 1):
        if v * k <= N: 
            for m in range(1, a + 1):
                if v * m <= N and k + m <= a:
                    for n in range(1, N + 1):
                        if 2 * math.floor((n - 1) / v) + 1 <= m:
                            nk = n * k
                            if nk > max_nk:
                                max_nk = nk
                                best_params = (n, k, m, v)

end = time.time()

# 結果出力
print("最大 n*k =", max_nk)
print("最適な (n, k, m, v) =", best_params)
print(f"実行時間: {end - start:.4f} 秒")