import math
import time

start = time.time()

# 定数
N = 64
a = 100


max_nk = 0
best_params = None

# for n in range(1, N + 1):
#     for k in range(1, a + 1):
#         nk = n * k
#         if nk <= max_nk:
#             continue  # 最大値更新の可能性がないならスキップ
#         for v in range(1, a + 1):
#             if v * k > N:
#                 break
#             for m in range(1, a + 1):
#                 if v * m > N or 2 * k + m > a:
#                     break
#                 if 2 * math.floor((n - 1) / v) + 1 <= m:
#                     if nk > max_nk:
#                         max_nk = nk
#                         best_params = (n, k, m, v)

found = False
for nk in range(N * a, 0, -1):  # 大きい順にnkを探す
    for n in range(1, N + 1):
        if nk % n != 0:
            continue  # kは整数じゃないとダメ
        k = nk // n
        if k > a:
            continue
        for v in range(1, a + 1):
            if v * k > N:
                break
            for m in range(1, a + 1):
                if v * m > N or 2 * k + m > a:
                    break
                if 2 * math.floor((n - 1) / v) + 1 <= m:
                    max_nk = nk
                    best_params = (n, k, m, v)
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        break


end = time.time()

print("最大 n*k =", max_nk)
print("最適な (n, k, m, v) =", best_params)
print(f"実行時間: {end - start:.4f} 秒")
