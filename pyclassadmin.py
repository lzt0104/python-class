## By Lzt
import os

def home():
    os.system("cls")
    print(" ****************************")
    print("*        班級管理程式        *")
    print(" ****************************")

    print("1>新增學生資料")
    print("2>查詢學生資料")
    print("3>修改學生資料")
    print("4>刪除學生資料")
    print("5>顯示學生資料")
    print("6>新增學生成績")
    print("7>顯示學生成績")
    print("8>修改學生成績")
    print("9>結束程式")
    menu = int(input("請選擇下列功能(1,2,3,4,5,6,7,8,9) : "))
    return menu

def fun1():
    a = "0"
    while a != "done":
        os.system("cls")
        print(" ****************************")
        print("*      1.新增學生資料        *")
        print(" ****************************")
        stu_name = input("請輸入學生姓名: ")
        stu_num = input("請輸入學生座號: ")  
        stu_id = input("請輸入學生學號: ")    
        stu_age = input("請輸入學生年齡: ")  
        stu_phone = input("請輸入學生手機: ")
        f.write(stu_name + "|" + stu_num +"|"+ stu_id + "|" + stu_age +"|"+ stu_phone +"\n")
        a = input("輸入done結束，按Enter繼續")

def fun2():
    b = "0"
    while b != "done":
      os.system("cls")
      print(" ****************************")
      print("*      2.查詢學生資料        *")
      print(" ****************************")
      stuid = input("請輸入學生學號以查詢")
      line = f.readline()
      sid = line.split("|")[2]
      if stuid == sid:
        print("姓名: " + line.split("|")[0])
        print("座號: " + line.split("|")[1])
        print("學號: " + line.split("|")[2])
        print("年齡: " + line.split("|")[3])
        print("手機: " + line.split("|")[4])
        b = input("輸入done結束，按Enter繼續")
        

def fun3():
    c = "0"
    while c != "done":
        os.system("cls")
        print(" ****************************")
        print("*      3.修改學生資料        *")
        print(" ****************************") 
        f = open("StuFile.txt", "r")
        data = f.read()
        f.close()
        print(data)
        old_str = input("請輸入舊資料: ")
        new_str = input("請輸入新資料: ")
        data = data.replace(old_str, new_str)
        print(data)  
        f = open("StuFile.txt", "w")
        f.write(data)
        f.close()
        c = input("輸入done結束，按Enter繼續")       

def fun4():
    d = "0"
    while d != "done":
        stu_data = ""
        os.system("cls")
        print(" ****************************")
        print("*      4.刪除學生資料        *")
        print(" ****************************") 
        f = open("StuFile.txt", "r")
        all_data = f.read()
        print("修改前資料")
        print(all_data)
        f.seek(0)
        delet_str = input("請輸入欲刪除的代表資料: ")
        line = f.readline()
        while line:
            a = line.find(delet_str)
            if a == -1:
                stu_data += line
            line = f.readline()   
        f.close()

        f = open("StuFile.txt", "w")
        f.write(stu_data)
        f.close()
        f = open("StuFile.txt", "r")
        all_data = f.read()
        print("修改後資料:")
        print(all_data)
        f.close()
        d = input("輸入done結束，按Enter繼續")         

def fun5():
    line = f.readline()
    while line:
        name = line.split("|")[0]
        num = line.split("|")[1]
        sid = line.split("|")[2]
        age = line.split("|")[3]
        phone = line.split("|")[4]
        print("%s:%s號，學號:%s，%s歲，手機:%s"%(name, num, sid, age, phone))  
        line = f.readline()
    e = input("按任意鍵離開")

def fun6():
    a = "0"
    while a != "done":
        os.system("cls")
        print(" ****************************")
        print("*      6.新增學生成績        *")
        print(" ****************************")
        obj = input("請輸入欲加入成績的科目: ")
        
        stu_data = str()
        s = open("StuScore.txt", "r")
        line = s.readline()
        while line:
            title = line.split(",")[0]
            if obj == title:
                line = line.replace("\n","")
                data = list(line.split(','))
                print("科目", line.split(",")[0])
                print("範圍", line.split(",")[1])
                for i in range(2, len(data)):
                    print(i-1, "號: ",data[i])
                score = input("請輸入欲加入的成績: ")
                data.append(score)
                stu_data += data[0]
                for i in range(len(data)-1):
                    stu_data = stu_data + "," + data[i+1]
                stu_data += "\n"
            else:
                stu_data += line     
            line = s.readline()
        print(stu_data)
        s.close()
        s = open("StuScore.txt", "w")
        s.write(stu_data)
        s.close()
        a = input("輸入done結束，按Enter繼續")

def fun7():
    line = s.readline()
    while line:
        data = list(line.split(","))
        print("科目: ", data[0])
        print("範圍: ", data[1])
        for i in range(len(data)-2):
            print("第", i+1, "號成績: ", data[i+2])
        line = s.readline()
    e = input("按任意鍵離開")

def fun8(): 
    c = "0"
    while c != "done":
        os.system("cls")
        print(" ****************************")
        print("*      8.修改學生成績        *")
        print(" ****************************") 
        s = open("StuScore.txt", "r")
        line = s.readline()
        obj = input("請輸入欲修改成績的科目: ")
        stu_data = str()
        while line:
            title = line.split(",")[0]
            if obj == title:
                line = line.replace("\n","")
                data = list(line.split(','))
                print("科目", line.split(",")[0])
                print("範圍", line.split(",")[1])
                for i in range(2, len(data)):
                    print(i-1, "號: ",data[i])
                num =  int(input("請輸入欲修改成績的座號: "))
                new_str = input("請輸入新成績: ")
                data[num+1] = new_str
                stu_data += data[0]
                for i in range(len(data)-1):
                    stu_data = stu_data + "," + data[i+1]
                stu_data += "\n"
            else:
                stu_data += line     
            line = s.readline()
        s.close()
        print(stu_data)  
        s = open("StuScore.txt", "w")
        s.write(stu_data)
        s.close()
        c = input("輸入done結束，按Enter繼續")

###############主程式###############
while(True):
    menu = home()
    print(menu)
    if menu == 1:
        f = open("StuFile.txt", "a")
        fun1()
        f.close() 

    elif menu == 2:
        f = open("StuFile.txt", "r")
        fun2()
        f.close() 

    elif menu == 3:
        fun3() 

    elif menu == 4:
        fun4()  

    elif menu == 5: 
        os.system("cls")
        print(" ****************************")
        print("*      5.顯示學生資料        *")
        print(" ****************************")  
        f = open("StuFile.txt", "r")
        fun5()
        f.close()
    
    elif menu == 6:
        fun6()

    elif menu == 7:
        os.system("cls")
        print(" ****************************")
        print("*      7.顯示學生成績        *")
        print(" ****************************")  
        s = open("StuScore.txt", "r")
        fun7()
        s.close()  

    elif menu == 8:
        fun8()

    elif menu == 9:
        break
