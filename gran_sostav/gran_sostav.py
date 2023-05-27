import pandas as pd
import csv
import numpy as np
from tkinter import *
import tkinter.messagebox as mb

class MyWindow:
    def __init__(self, win):
        
        
        self.lbl001=Label(win, text='Галька\n (щебень)')
        self.lbl1=Label(win, text='> 10')
        self.lbl0=Label(win, text='Гравий\n (дресва)')
        self.lbl2=Label(win, text='10 - 5')
        self.lbl3=Label(win, text='5 - 2')
        self.lbl01=Label(win, text='Песок')
        self.lbl4=Label(win, text='2 - 1')
        self.lbl5=Label(win, text='1 - 0.5')
        self.lbl6=Label(win, text='0.5 - 0.25')
        self.lbl7=Label(win, text='0.25 - 0.1')
        self.lbl8=Label(win, text='0.1 - 0.05')
        self.lbl9=Label(win, text='Пыль')
        self.lbl10=Label(win, text='0.05-0.01')
        self.lbl11=Label(win, text='0.01-0.002')
        self.lbl12=Label(win, text='Глина')
        self.lbl13=Label(win, text='<0.002')
        self.lbl14=Label(win, text='Необходимое количество проб:')
        self.lbl15=Label(win, text=u"\u03bc:")
        self.lbl16=Label(win, text=	u"\u03C3:")
        
        self.t1=Entry(bd=3, width=6)
        self.t2=Entry(bd=3, width=6)
        self.t3=Entry(bd=3, width=6)
        self.t4=Entry(bd=3, width=6)
        self.t5=Entry(bd=3, width=6)
        self.t6=Entry(bd=3, width=6)
        self.t7=Entry(bd=3, width=6)
        self.t8=Entry(bd=3, width=6)
        self.t10=Entry(bd=3, width=6)
        self.t11=Entry(bd=3, width=6)
        self.t13=Entry(bd=3, width=6)
        self.t14=Entry(bd=3, width=6)
        self.t15=Entry(bd=3, width=6)
        self.t16=Entry(bd=3, width=6)
        
        self.lbl1.place(x=40, y=50)       
        self.lbl001.place(x=40, y=10)
        self.lbl0.place(x=150, y=10)
        self.lbl2.place(x=120, y=50)
        self.lbl3.place(x=180, y=50)
        self.lbl01.place(x=360, y=10)
        self.lbl4.place(x=240, y=50)
        self.lbl5.place(x=300, y=50)
        self.lbl6.place(x=360, y=50)
        self.lbl7.place(x=420, y=50)
        self.lbl8.place(x=480, y=50)
        self.lbl9.place(x=570, y=10)
        self.lbl10.place(x=540, y=50)
        self.lbl11.place(x=600, y=50)
        self.lbl12.place(x=660, y=10)
        self.lbl13.place(x=660, y=50)
        self.lbl14.place(x=470, y=130)
        self.lbl15.place(x=400, y=100)
        self.lbl16.place(x=400, y=130)
        
        self.t1.place(x=40, y=70)
        self.t2.place(x=120, y=70)
        self.t3.place(x=180, y=70)
        self.t4.place(x=240, y=70)
        self.t5.place(x=300, y=70)
        self.t6.place(x=360, y=70)
        self.t7.place(x=420, y=70)
        self.t8.place(x=480, y=70)
        self.t10.place(x=540, y=70)
        self.t11.place(x=600, y=70)
        self.t13.place(x=660, y=70)
        self.t14.place(x=660, y=130)  
        self.t15.place(x=420, y=100) 
        self.t16.place(x=420, y=130)        
        self.b1=Button(win, text='GO!', command=self.make_proba)
        self.b1.place(x=40, y=130)
        
        self.var1 = BooleanVar()
        self.var1.set(0)
        self.c1 = Checkbutton(win, text="Песок",
                 variable=self.var1,
                 onvalue=1, offvalue=0,
                 command=self.operate1)
        self.c1.pack(anchor=W, padx=10)
        self.c1.place(x=120, y=100)
        
        self.var2 = BooleanVar()
        self.var2.set(0)        
        self.c2 = Checkbutton(win, text="Супесь",
                 variable=self.var2,
                 onvalue=1, offvalue=0)
                #  command=operate)
        self.c2.pack(anchor=W, padx=10)
        self.c2.place(x=120, y=130)
        
        self.var3 = BooleanVar()
        self.var3.set(0)        
        self.c3 = Checkbutton(win, text="Суглинок",
                 variable=self.var3,
                 onvalue=1, offvalue=0)
                #  command=operate)
        self.c3.pack(anchor=W, padx=10)
        self.c3.place(x=240, y=100)
        
        self.var4 = BooleanVar()
        self.var4.set(0)        
        self.c4 = Checkbutton(win, text="Глина",
                 variable=self.var4,
                 onvalue=1, offvalue=0)
                #  command=operate)
        self.c4.pack(anchor=W, padx=10)
        self.c4.place(x=240, y=130)
    
       
    
    def show_error(self):
        msg = "Сумма введенных значений не равна 100!"
        mb.showerror("Ошибка", msg)
    
       
    
    def get_isch(self):
        n1=float(self.t1.get())
        n2=float(self.t2.get())
        n3=float(self.t3.get())
        n4=float(self.t4.get())
        n5=float(self.t5.get())
        n6=float(self.t6.get())
        n7=float(self.t7.get())
        n8=float(self.t8.get())
        n10=float(self.t10.get())
        n11=float(self.t11.get())
        n13=float(self.t13.get())
        isch_data = [n1,n2, n3, n4, n5, n6, n7, n8, n10, n11, n13]
        
        if round(sum(isch_data),1) != 100.0:
            return self.show_error()
        else:
            return isch_data
        
          
    def sort_first (self):
        ischod = self.get_isch()
        enum = list(enumerate(ischod))
        sorted_ischod = sorted(enum, key=lambda x:x[1])
        return sorted_ischod
    def normal(self):
        ischod_list = self.get_isch()
        n15=float(self.t15.get())
        n16=float(self.t16.get())
        self.dist_f = np.random.normal(n15, n16, len(ischod_list))
        return np.sort(abs(self.dist_f))
        
        
        
    def make_new_dist(self):
        ishod_sort = self.sort_first() 
        raspr = self.normal()
        poradok = [i[0] for i in ishod_sort]
        norm_raspr = [round(i, 1) for i in raspr]
        ish_rasp = [i[1] for i in ishod_sort]
        res_list = list(map(lambda x, y: x+y, norm_raspr, ish_rasp))
        list_preobr = list(zip(poradok, res_list))
        list_preobr_itog = sorted(list_preobr, key=lambda x:x[0])
        return list_preobr_itog
    
    def make_hund(self):
        itog_list = self.make_new_dist()
        sum_gr = [i[1] for i in itog_list]
        if sum(sum_gr) > 100:
            while sum(sum_gr) > 100 and sum(sum_gr) !=100:
                for i in range(len(sum_gr)):
                    sum_gr[i]= sum_gr[i] - 0.1
                    sum_gr[i] = round(abs(sum_gr[i]), 1)
                sum_gr=sum_gr 
            result_dist =sum_gr       
            return result_dist
   
    
    def operate1(self):
        result_chek = self.make_hund()
        self.silt = result_chek[-3:]  
        if sum(self.silt) < 3 and self.var1.get() == 1:
            result_chek = result_chek     
        if sum(self.silt) > 3 and self.var1.get()==1:
            while sum(self.silt) > 3:
                for i in range(len(self.silt)):
                    self.silt[i]= self.silt[i] - 0.1
                    self.silt[i] = round(abs(self.silt[i]), 1)
                self.silt=self.silt
            result_chek[-3:] = self.silt      
        return result_chek
    
    def operate2(self):
        result_chek = self.make_hund()
        self.silt = result_chek[-3:]  
        if sum(self.silt) > 3 and sum(self.silt) < 10 and self.var2.get() == 1:
            result_chek = result_chek     
        if sum(self.silt) < 3 and self.var2.get()==1:
            while sum(self.silt) < 3 and sum(self.silt) < 3:
                for i in range(len(self.silt)):
                    self.silt[i]= self.silt[i] + 0.1
                    self.silt[i] = round(abs(self.silt[i]), 1)
                self.silt=self.silt
            result_chek[-3:] = self.silt   
        if sum(self.silt) > 10 and self.var2.get()==1:
            while sum(self.silt) > 10 and sum(self.silt) > 3:
                for i in range(len(self.silt)):
                    self.silt[i]= self.silt[i] - 0.1
                    self.silt[i] = round(abs(self.silt[i]), 1)
                self.silt=self.silt
            result_chek[-3:] = self.silt    
        return result_chek
    
    def operate3(self):
        result_chek = self.make_hund()
        self.silt = result_chek[-3:]  
        if sum(self.silt) > 10 and sum(self.silt) < 30 and self.var3.get() == 1:
            result_chek = result_chek     
        if sum(self.silt) < 10 and self.var3.get()==1:
            while sum(self.silt) < 10 and sum(self.silt) < 30:
                for i in range(len(self.silt)):
                    self.silt[i]= self.silt[i] + 0.1
                    self.silt[i] = round(abs(self.silt[i]), 1)
                self.silt=self.silt
            result_chek[-3:] = self.silt   
        if sum(self.silt) > 30 and self.var3.get()==1:
            while sum(self.silt) > 30 and sum(self.silt) > 10:
                for i in range(len(self.silt)):
                    self.silt[i]= self.silt[i] - 0.1
                    self.silt[i] = round(abs(self.silt[i]), 1)
                self.silt=self.silt
            result_chek[-3:] = self.silt    
        return result_chek
    
    def operate4(self):
        result_chek = self.make_hund()
        self.silt = result_chek[-3:]  
        if sum(self.silt) > 30 and self.var4.get() == 1:
            result_chek = result_chek     
        if sum(self.silt) < 30 and self.var4.get()==1:
            while sum(self.silt) < 30:
                for i in range(len(self.silt)):
                    self.silt[i]= self.silt[i] + 0.1
                    self.silt[i] = round(abs(self.silt[i]), 1)
                self.silt=self.silt
            result_chek[-3:] = self.silt      
        return result_chek
    
    def type_disp(self):
        if self.var1.get() == 1:
            result_proba = self.operate1()
        elif self.var2.get() == 1:
            result_proba = self.operate2()
        elif self.var3.get() == 1:
            result_proba = self.operate3()
        elif self.var4.get() == 1:
            result_proba = self.operate4()
        return result_proba     
           

    
    def sum_sostav (self):
        result_proba = self.type_disp() 
        if sum(result_proba) < 100:
            ma_gr = max(result_proba)
            ma_gr = round(max(result_proba)+ (100-sum(result_proba)), 1)
            result_proba[result_proba.index(max(result_proba))] = ma_gr
        elif sum(result_proba) > 100:
            ma_gr = max(result_proba)
            ma_gr = round(max(result_proba)- (sum(result_proba)-100), 1)
            result_proba[result_proba.index(max(result_proba))] = ma_gr          
        result_proba.append(round(sum(result_proba), 1))
        return result_proba
    
    def sand_type (self):
        result = self.sum_sostav()
        if sum(result[:3]) > 25:
            result.append('Песок гравелистый')
        elif sum(result[:5]) > 50:
            result.append('Песок крупный')
        elif sum(result[:6]) > 50:
            result.append('Песок средней крупности')
        elif sum(result[:7]) >= 75:
            result.append('Песок мелкий')
        elif sum(result[:7]) < 75:
            result.append('Песок пылеватый')   
        return result
    
    def supes_type(self):
        result = self.sum_sostav()
        if sum(result[3:8]) >= 50:
            result.append('Супесь песчанистая')
        elif sum(result[3:8]) < 50:
            result.append('Супесь пылеватая')
        return result
    
    def sugl_type(self):
        result = self.sum_sostav()
        if sum(result[3:8]) >= 40:
            result.append('Суглинок песчанистый')
        elif sum(result[3:8]) < 40:
            result.append('Суглинок пылеватый')
        return result
    
    def clay_type(self):
        result = self.sum_sostav()
        if sum(result[3:8]) >= 40:
            result.append('Глина песчанистая')
        elif sum(result[3:8]) < 40:
            result.append('Глина пылеватая')
        return result
    
        
    
    def dispers_class(self):
        if self.var1.get() == 1:
            result = self.sand_type()
        elif self.var2.get() == 1:
            result = self.supes_type()
        elif self.var3.get() == 1:
            result = self.sugl_type()
        elif self.var4.get() == 1:
            result = self.clay_type()
        return result
    
    def make_amount_gr(self):
        n14=int(self.t14.get())
        itog = pd.DataFrame()
        for i in range(n14):
            itog[i] = self.dispers_class()
        return itog
        
        
    
    def make_proba(self):
        self.frame_itog = pd.DataFrame(self.make_amount_gr().transpose())
        self.frame_itog.columns=['>10',  '10 - 5', '5 - 2', '2 - 1', \
            '1 - 0.5', '0.5 - 0.25', '0.25 - 0.1', '0.1 - 0.05', '0.05 - 0.01', '0.01 - 0.002', '<0.002', 'Сумма', 'Наименование грунта']
        arrays = [['Галька (щебень)', 'Гравий (дресва)', 'Гравий (дресва)', 'Песок','Песок','Песок','Песок','Песок', 'Пыль', 'Пыль', 'Глина', 'Гр.сост.', '-'], \
                 self.frame_itog.columns] 
        self.frame_itog.columns = pd.MultiIndex.from_arrays(arrays)            
        self.frame_itog.to_csv('res_gran_sostav')
window=Tk()
mywin=MyWindow(window)
window.title('ДЕСЯТЬ!')
window.geometry("800x170+10+10")
window.mainloop()