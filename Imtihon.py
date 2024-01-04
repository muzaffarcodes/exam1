# Problem A: 
db_name = 'Muzaffar'
db_password = 1626
imkon = 3 
while(True):
    if(imkon > 0):
        user = input("Username: ")
        password = input("Password: ")
        if(db_name != user and db_password == password):
            print("Username is ERROR!")
            imkon -= 1
            print("Tries:",imkon)
        elif(db_name == user and db_password != password):
            print("Password is ERROR!")
            imkon -= 1
            print("Imkon:",imkon)
        elif(db_name != user and db_password != password):
            print("Password and Username are ERROR!")
            imkon -= 1
            print("Imkon:",imkon)
        if(imkon == 0):
            tanlov = input("""Parolni tiklashni istaysizmi? 
Eski parolni kiritib, yangisiga almashitiring{ha/Yo'q]: """)
            if(tanlov == 'ha' or tanlov == 'Ha'):
                db_password = input("Eski parolni kiriting: ")
                newPass = input("Yangi parolni kiriting: ")
                db_password = newPass
                newPass = db_password
                newPass = input("Yangi parolni tasdiqlang: ")
                print(f"""Parol Muvaffaqiyatli tiklandi! - {newPass}
Tizimga kirishingiz mumkin, ser!""")
                break
            elif(tanlov == "yo'q" or tanlov == "Yo'q"):
                print("Siz tizimga kirishni xohlamadingiz!!!")   
                break
            else:
                print("Siz parolni yangilamadingiz! Tizimga kira olmaysiz!")
                break
#%% Problem B
class PersonalInfo():
    def __init__(self,name,age,expirience,maleOrF):
        self.name = name
        self.age = age
        self.expirience = expirience
        self.maleOrF = maleOrF
    def showInfo(self):
        print("----------------------------------------------------------")
        print(f"|            |          |                 |{self.maleOrF}|")
        print(f"|            |          |{self.expirience}|              |")
        print(f"|            |{self.age}|                 |              |")
        print(f"|{self.name} |          |                 |              |")
        print("----------------------------------------------------------")
 
muzaffar = PersonalInfo(input("Your Name: "),input("Your age: "),input("Your Expirience: "),input("Your Gender: "))
muzaffar.showInfo()
#%% Problem C
import time
word = input("So'zni kiriting: ")
for i in range(len(word) - 1):
    print(word[i] + '...',end='.')
    time.sleep(2)
print(word[-1])
for i in range(len(word)-1,0,-1):
    print(word[i] + '...',end=('.'))
    time.sleep(2)
print(word[0])
#%% Problem D
class Employee():
    def __init__(self,name,surname,age,salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
    def showEmployee(self):
        print(f"""Name: {self.name}
Surname: {self.surname}
Age: {self.age}
Salary: {self.salary}
""")

em1 = Employee("Muzaffar", "Khaydarov", 16, 14000000)
em1.showEmployee()

# step1: Employee klassini kiritb oldim
# step2: def __init__ kiritdim va uni ichiga name,surname,age,salary parametr kiritdim
# step3: def employee kiritdim va u ekranga malumotlarni chiqaradi
# va 2-funksiyani ishlatdim
# ekranga bostirdim
#%% Problem E 
natija1 = 0
while(True):
    son1 =  input("Son kiriting: ")
    if(son1 == 'q'):
        print("Javob: ",natija1)
        print("Yana kutib qolamiz!")
        break
    natija1 += int(son1)
#%% Problem F
"""
Compiled - butun boshli kodni boshidan oxirigacha kompil(tahlil qilib), xato bo'lsa 
natija ekranga chiqmaydi, keyin natijani 
ekranga bostiradi. Bu kabi dasturlash tillari - interpreted dasturlash tilidan tezroq
ishlaydi! Hozirgi kunda C compiled dasturlash tili - embedded(ko'milgan tizimlarda)
tizimlarda ishlatiladi  . Compiled dasturlash tillari: C,C++,C#,Go,Java,Pascal
                                                           
Interpreted - yozilgan kodni satrma-satr oqib tahlil qiladi va ekranga natijani bostiradi.
Interpretedda esa dasturining biror bir satrida xato bo'lsa dastur portlaydi!
Interpreted dasturlash tillari Compileddan sekinroq.
Interpreted dasturlash tillariga misollar: Python, JavaScript,Ruby,Swift,Php,Kotlin,Perl

"""
#%% Problem G
"""
False - 0, Boolean qiymat (true or false)
True - 1, Boolean qiymat (true or false)
None - o'zgaruvchiga qiymat bermaslik uchun ishlatiladi
and - va operatori bo'lib, if va while'larda ishlatiladi! True and False = False
import - metod yoki kutubxona chaqirish 
class - oopning elementi.
pass - o'tkazib yuborish 
in - ichida print va forda
def - funksiya kiritish

"""


