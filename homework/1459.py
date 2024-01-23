# main.py

# 수정된 클래스
class StringRepeater:
    def repeat_string(self, cnt, text):
        print("\n".join(text for _ in range(cnt)))

# 사용 예시
repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")