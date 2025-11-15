#Hash Type Detector&MD5 Generator
MD5 لاكتشاف نوع الهاش لتوليد Kali Linux تعمل من سطر الاوامر على اداه بسيطه بلغه python

## تشغيل الاولي 
python3 hash_task1.py
#ثم اختار:
#1-كشف نوع الهاش 
#2-توليد MD5 من نص
#3-خروج

example:python3 hash_task1.py 5d41402abc4b2a76b9719d911017c592
#يطبع:DETECTED:MD5

##المزايا (features)
.يكشف الانواع:MD5,SHA1,SHA256,SHA384,SHA512
.يولد MD5 من نص عادي
.يتحقق من صحه لادخال(hex)ويتعامل مع الاخطاء
.لا يحتاج مكتبات خارجيه,يعتمد على python3 القياسي 


##الفكره باختصار(Design)
1.ينظف الادخال(يقطع الفراغات)
2.يتاكد ان النص احرف hexفقط (a-f 9-0)
3.يحدد النوع حسب الطول:
.MD5(32)
.SHA1(40)
.SHA256(64)
.SHA384(96)
.SHA512(128)
4. ان لم يطابق  يطبع (Unknown)

##لقطات الشاشه(screenshots)
وضعت الصور بمجلد	screenshots/
.MD5-detect.png
.SHA256- detect.png
.MD5 generate.png
.invalid-input.png


##مرخص بموجب MIT License انظر الى ملف LICENSE
والاداة لتعلم فقط لا تستخدمها لشيء غير قانوني###


##معلومات الطالب
الاسم حسين طويسات
الرقم الجامعي:202310004
الجامعه :اربد الاهلية

























