#!/usr/bin/env python3

import sys
import hashlib

def is_hex_string(text):
    if text == "":
        return False
    for ch in text:
        if ch not in "0123456789abcdefABCDEF":
            return False
    return True

def detect_hash_type(h):
    h = h.strip()
    if not is_hex_string(h):
        return "النص ليس قيم هكس صحيحة (ليس هاش معروف)"

    length = len(h)

    if length == 32:
        return "MD5"
    elif length == 40:
        return "SHA1"
    elif length == 64:
        return "SHA256"
    elif length == 96:
        return "SHA384"
    elif length == 128:
        return "SHA512"
    else:
        return "غير معروف (الطول لا يطابق أي نوع)"

def make_md5_from_text(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def interactive_menu():
    while True:
        print("\n===== برنامج الهاش البسيط =====")
        print("1) اكتشاف نوع هاش")
        print("2) توليد MD5 من نص")
        print("3) خروج")

        choice = input("اختر: ")

        if choice == "1":
            h = input("أدخل الهاش: ")
            print("النتيجة:", detect_hash_type(h))
        elif choice == "2":
            text = input("أدخل النص: ")
            print("MD5:", make_md5_from_text(text))
        elif choice == "3":
            break
        else:
            print("اختيار غير صحيح")

def main():
    if len(sys.argv) > 1:
        h = sys.argv[1]
        print("النتيجة:", detect_hash_type(h))
    else:
        interactive_menu()

if __name__ == "__main__":
    main()
