# 終極密碼 讓使用者能夠重複猜數字，直到猜對為止
# 告訴使用者需要輸入的數字範圍 input()
# 超出範圍要顯示「超出範圍請重新輸入」
# 數字太大 要提示「請輸入更小的數字」
# 數字太小 要提示「請輸入更大的數字」
# 使用者猜對要回傳「恭喜中獎」


while True:
    guess= int(input("請在1~100輸入數字："))
    ans=73
    if guess>100 or guess<1:
        print("超出範圍請重新輸入")
    elif guess>ans:
        print("請輸入更小的數字")
    elif guess<ans:
        print("請輸入更大的數字")
    else: 
        print("恭喜中獎")
        break










