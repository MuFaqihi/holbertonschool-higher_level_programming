# Python - Classes and Objects
## ما هي البرمجة الكائنية التوجه (OOP)؟
البرمجة الكائنية التوجه (Object-Oriented Programming) هي نمط برمجي يعتمد على الكائنات (Objects) والفئات (Classes) لتنظيم الكود وجعله أكثر قابلية لإعادة الاستخدام.

## "first-class everything"
في بايثون، كل شيء تقريبًا يُعامل ككائن من الدرجة الأولى، مما يعني أنه يمكن تمريره كمعامل، تخزينه في متغيرات، وإعادته من الدوال.

## ما هي الفئة (Class)؟
الفئة هي قالب يُستخدم لإنشاء كائنات. تحتوي على سمات (Attributes) وطرق (Methods) تحدد سلوك الكائنات.

## ما هو الكائن (Object) وما هي النسخة (Instance)؟
الكائن هو مثال حي من الفئة. عندما تُنشئ كائنًا من فئة، يُسمى ذلك نسخة (Instance) من الفئة.

## الفرق بين الفئة والكائن؟
الفئة هي التصميم أو القالب.

الكائن هو التطبيق الفعلي لهذا التصميم.

## ما هي السمة (Attribute)؟
السمة هي متغير يُخزن بيانات داخل الكائن أو الفئة.

## السمات العامة، المحمية، والخاصة
- العامة (Public): يمكن الوصول إليها من أي مكان.

- المحمية (Protected): تُستخدم للإشارة إلى أن السمة لا يجب تعديلها مباشرة.

- الخاصة (Private): لا يمكن الوصول إليها إلا من داخل الفئة.

## ما هو self؟
هو self  إشارة إلى الكائن الحالي داخل الفئة، ويُستخدم للوصول إلى سماته وطرقه.

## ما هي الطريقة (Method)؟
الطريقة هي دالة داخل الفئة تُحدد سلوك الكائنات.

## ما هي __init__؟
هي __init__  طريقة خاصة تُستخدم لتهيئة الكائن عند إنشائه.

## التجريد، التغليف، وإخفاء المعلومات
- التجريد (Abstraction): إخفاء التفاصيل غير الضرورية.

-  التغليف (Encapsulation): حماية البيانات داخل الفئة.

- إخفاء المعلومات (Information Hiding): منع الوصول المباشر إلى البيانات الحساسة.

## ما هي الخاصية (Property)؟
الخاصية هي طريقة تُستخدم للوصول إلى السمات بطريقة منظمة.

## الفرق بين السمة والخاصية
السمة هي متغير، بينما الخاصية هي طريقة تُستخدم للوصول إلى السمة.

## الطريقة البايثونية لكتابة getters و setters
بايثون تستخدم @property لإنشاء getter و setter بطريقة أكثر أناقة.

## كيفية إنشاء سمات جديدة ديناميكيًا
يمكنك إضافة سمات جديدة إلى الكائنات باستخدام:
```c
obj.new_attr = "New Value"
```
## كيفية ربط السمات بالكائنات والفئات
يمكنك تعريف السمات داخل الفئة أو داخل الكائن مباشرة.

## ما هو __dict__؟
هو __dict__  قاموس يحتوي على جميع السمات الخاصة بالكائن أو الفئة.

## كيف يجد بايثون السمات؟
بايثون يبحث عن السمات داخل:

الكائن نفسه.

الفئة التي ينتمي إليها.

الفئات الموروثة.

## كيفية استخدام getattr
تُستخدم getattr  للوصول إلى السمات بطريقة ديناميكية:
```c
value = getattr(obj, "attribute_name", "Default Value")
```
# Requirements
## General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
