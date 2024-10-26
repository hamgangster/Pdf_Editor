from cgi import test
from genericpath import exists
import os.path
from tkinter import messagebox
from pypdf import PdfReader ,PdfWriter
from tkinter import *
import os 
os.chdir('../')
dic_main=os.path.join(os.getcwd(),'PDF_EDITOR')
if not os.path.exists(dic_main):
 os.mkdir(dic_main)
#A pdf api
#tells pages in  a pdf
class Pages:
    def __init__(self,name) -> None:
        self.name=name
        self.reader=PdfReader(self.name)
        self.writer=PdfWriter()
    def printer(self):
     return(f'Number of pages in this pdf is {len(self.reader.pages)}')

# rotate all pages
class Pdfrotate(Pages):

    def Rotater(self,r):
        self.ro=r
        for i in range(len(self.reader.pages)):
            pageobj=self.reader.pages[i]
            pageobj.rotate(self.ro)
            self.writer.add_page(pageobj)
        outputpdf=self.name.split('.pdf')[0]+f"_Rotataed.pdf"
        with open (outputpdf,'wb')as f:
            self.writer.write(f)
            f.close()

#Read All Pages
class Read(Pages):
    def Read_(self):
     for i in range(len(self.reader.pages)):
       self.page=self.reader.pages[i]
       return(self.page.extract_text())

#Merges all Pages
class Merging:
    def __init__(self,name):
     self.__name=name
     pdf_write=PdfWriter()
     for pdf in self.__name:
         pdf_write.append(pdf)
     self.outputpdf_='Merge.pdf'
     with open(self.outputpdf_,'wb') as f:
         pdf_write.write(f)

#Splits Pdf's
class Splits_(Pages):
    def Splits(self,splits):
     
     self.splits=splits
     self.start=0
     self.end=self.splits[0]
     for i in range(len(self.splits)+1):
       if i<len(self.splits):
         self.end=self.splits[i]
       else:
        self.end=(len(self.reader.pages))
       for page in range(self.start,self.end):
           self.writer.add_page(self.reader.get_page(page))
       self.outpdf_=self.name.split('.pdf')[0]+f'_{i+1}.pdf'
       with open (self.outpdf_,'wb')as f:

           self.writer.write(f)
       self.start=self.end

#Extract page
class Extract(Pages):
    def _Extract_(self,exc,name):
        self.name=name
        self.extract=exc
        self.extract-=1
        self.writer.add_page(self.reader.get_page(self.extract))
        self.output_pdf=self.name+f'_ExtractedPagefrom{self.name.split(".pdf")[0]}.pdf'
        with open (self.output_pdf,'wb') as f:
            self.writer.write(f)

#Remove Pages
class Remove(Pages):
    def Remove_(self,rm):
        self.__remove=rm
        self.__remove=self.__remove-1
        for page in range(len(self.reader.pages)):
            if(page==self.__remove):
                continue
            self.writer.add_page(self.reader.get_page(page))
        self.output=self.name.split('.pdf')[0]+f'_Removedpage{rm}.pdf'
        with open(self.output,'wb')as f:
            self.writer.write(f)

#WaterMark pdf
class Watermark(Pages):
   @staticmethod
   def Add_watermark(wm,pageobj):
      reader=PdfReader(wm)
      pageobj.merge_page(reader.pages[0])
      return pageobj
   def Apply(self,waterm):
      self.watermark=waterm
      for page in range(len(self.reader.pages)):
         self.wmPageobj=self.Add_watermark(self.watermark,self.reader.pages[page])
         self.writer.add_page(self.wmPageobj)
      self.outputpdf=f'Watermakered{self.name.split('.pdf')[0]}.pdf'
      with open(self.outputpdf,'wb')as f:
         self.writer.write(f)

def clear():
   for widget in root.winfo_children():
    widget.destroy()

def Back():
 clear()
 Gui_setup()

def cb1():
     
     def submit():
      try:
        get_=read.get()+'.pdf'
        page_=Pages(get_)
        messagebox.showinfo('Number Of Pages',page_.printer())
        print(page_.printer())
        read.set('')
      except:
         messagebox.showerror("ERROR","PDF not found")
  
     clear()
     Label(root,text="Enter Pdf Name",font=('Ariel'),borderwidth=5,relief=SUNKEN).grid(row=0,column=0)
     read=StringVar()
     #Entry Widget
     read_1=Entry(root,textvariable=read)
     read_1.grid(row=0,column=1)
     #Buttton Widget
     sub=Button(root,text='Submit',command=submit)
     sub.grid(row=1,column=0)
     back=Button(root,text='Back',command=Back)
     back.grid(row=1,column=2) 
                             
def cb2():
   
   def submit():
      try:
         get_1=read.get()+'.pdf'
         value_in=value.get()
         rotate_=Pdfrotate(get_1)
         rotate_.Rotater(value_in)
         read.set('')
         value.set('')
      except:
         messagebox.showerror('ERROR','Pdf Not Found Or Degree Value is Wrong')
      
   clear()
   Label(root,text="Enter Pdf Name",font=('Ariel'),borderwidth=5,relief=SUNKEN).grid(row=0,column=0)
   Label(root,text="The Degree of Pdf You Want To Roate",borderwidth=5,relief=SUNKEN).grid(row=1,column=0)
   read=StringVar()
   value=IntVar()
   #Entry Widget
   read_1=Entry(root,textvariable=read)
   read_1.grid(row=0,column=2)
   value_read=Entry(root,textvariable=value)
   value_read.grid(row=1,column=2)
   #Submit and Back Button
   sub=Button(root,text='Submit',command=submit)
   sub.grid(row=2,column=0)
   back=Button(root,text='Back',command=Back)
   back.grid(row=2,column=2)
   #Usr Guide
   Label(root,text='90, 180, or 270 to rotate pages clockwise').grid()
   Label(root,text='-90, -180, or -270 to rotate pages anticlockwise').grid()
                        
def cb3():
 try:
  def submmit():
    read_fun=read.get()+'.pdf'
    read_w=Read(read_fun)
    print(f'{read_w.Read_()}')
    read.set('')
 except:
     messagebox.showerror("ERROR","Problem reading Pdf")
 clear()
 Label(root,text='Enter Pdf Name',borderwidth=5,relief=SUNKEN).grid(row=0,column=0)
 read=StringVar()
 #Entry Widget
 read_entry=Entry(root,textvariable=read)
 read_entry.grid(row=0,column=2)

 #Buttton submit and back
 sub=Button(root,text='Submit',command=submmit)
 sub.grid(row=5,column=0)
 back_=Button(root,text='Back',command=Back)
 back_.grid(row=5,column=2)
 #Usr Guide
 Label(root,text='NOTE:-The text would be printed in cmd').grid()

 
def cb4():
    
    def submit():
        try:
            lis_=[]
            lis_.append(read_1.get()+'.pdf')
            lis_.append(read_2.get()+'.pdf')
            Merg=Merging(lis_)
            read_1.set('')
            read_2.set('')
        except:
          messagebox.showerror("ERROR","Pdf Not Found Or Enter two Pdf You Want To Merge")

    clear()
    Label(root,text='Enter Pdf 1',borderwidth=5,relief=SUNKEN,font=('Arial')).grid(row=0,column=0)
    Label(root,text='Enter Pdf 2',borderwidth=5,relief=SUNKEN,font=('Arial')).grid(row=1,column=0)
    #Enter Widget
    read_1=StringVar()
    read_2=StringVar()

    read_e1=Entry(root,textvariable=read_1).grid(row=0,column=1)
    read_e2=Entry(root,textvariable=read_2).grid(row=1,column=1)

    #Button submit and back
    sub=Button(root,text='Submit',command=submit)
    sub.grid(row=3,column=0)
    back_=Button(root,text='Back',command=Back)
    back_.grid(row=3,column=2)

def cb5():
   try:
    def submit():
        s=pdf_splits.get().split(',')
        lis=[]
        for i in s:
            lis.append(int(i))
        def_=Splits_(read_.get()+'.pdf')
        def_.Splits(lis)
        read_.set('')
        pdf_splits.set('')

   except:
       messagebox.showerror('ERROR',"PDF Not Found Or Split's Given Are Not Correct")
   clear()
   Label(root,text='Enter Pdf Name',borderwidth=5,relief=SUNKEN,font=('Arial')).grid(row=0,column=0)
   Label(root,text='Enter The Split Numbers',borderwidth=5,relief=SUNKEN,font=("Arial")).grid(row=1,column=0)
    #Enter Widget
   read_=StringVar()
   pdf_splits=StringVar()
   read_1=Entry(root,textvariable=read_).grid(row=0,column=1)
   pdf_splits1=Entry(root,textvariable=pdf_splits).grid(row=1,column=1)
   #Button
   sub=Button(root,text='Submit',command=submit).grid(row=2,column=0)
   back=Button(root,text='Back',command=Back).grid(row=2,column=1)
   #Usr Guide
   Label(root,text='Give Split like 1,2,3,4 only').grid()


def cb6():
    
    def submit():
          try:
           s1=Extract(r1.get()+'.pdf')
           s1._Extract_(r2.get(),r3.get())
          except:
            messagebox.showerror('ERROR','Pdf Not Found Or Page is Not Presernt Or New Pdf name not given')
    clear()
    Label(root,text='Enter Pdf Name',borderwidth=5,relief=SUNKEN,font=('Arial')).grid(row=0,column=0)
    Label(root,text='Enter The Extract Name',borderwidth=5,relief=SUNKEN,font=('Arial')).grid(row=1,column=0)
    Label(root,text='Enter Extracted page name',borderwidth=5,relief=SUNKEN,font=('Arial')).grid(row=2,column=0)
    #Entery Widget
    r1=StringVar()
    r2=IntVar()
    r3=StringVar()
    r_a1=Entry(root,textvariable=r1).grid(row=0,column=1)
    r_a2=Entry(root,textvariable=r2).grid(row=1,column=1)
    r_a3=Entry(root,textvariable=r3).grid(row=2,column=1)
    #Button
    sub=Button(root,text='Submit',command=submit).grid(row=3,column=0)
    back=Button(root,text="Back",command=Back).grid(row=3,column=1)


def cb7():
    def submit():
        try:
            s=Remove(r_1.get()+'.pdf')
            s.Remove_(r_2.get())
        except:
            messagebox.showerror('ERROR',"PDF Not Found Or Page Not Presernt")
    clear()
    Label(root,text='Enter Pdf Name',borderwidth=5,relief=SUNKEN,font=('Arial')).grid(row=0,column=0)
    Label(root,text=' page',borderwidth=5,relief=SUNKEN,font=('Arial')).grid(row=1,column=0)
    #Entry Widget
    r_1=StringVar()
    r_2=IntVar()
    r_a1=Entry(root,textvariable=r_1).grid(row=0,column=1)
    r_a2=Entry(root,textvariable=r_2).grid(row=1,column=1)
    #BUtton
    sub=Button(root,text='Submit',command=submit).grid(row=2,column=0)
    back=Button(root,text='Back',command=Back).grid(row=2,column=1)

def cb8():
    def submit():
        try:
            s1=Watermark(r_1.get()+'.pdf')
            s1.Apply(r_2.get()+'.pdf')
        except:
            messagebox.showerror()
    clear()
    Label(root,text='Orginal Pdf',borderwidth=5,relief=SUNKEN,font=('Arial')).grid(row=0,column=0)
    Label(root,text='WaterMark Pdf',borderwidth=5,relief=SUNKEN,font=('Arial')).grid(row=1,column=0)
    #Entry Widget
    r_1=StringVar()
    r_2=StringVar()
    r_1a=Entry(root,textvariable=r_1).grid(row=0,column=1)
    r_2a=Entry(root,textvariable=r_2).grid(row=1,column=1)
    #Button
    sub=Button(root,text='Submit',command=submit).grid(row=2,column=0)
    back=Button(root,text='Back',command=Back).grid(row=2,column=1)
    #Usr Guide
    Label(root,text='The Water Mark should Be In Pdf from').grid()

def Gui_setup():
 #GUI
 Head=Frame(root,bg='grey',borderwidth=5,relief=SUNKEN)
 Head.pack(side=TOP)

 Label(Head,text='PDF EDITOR',font=('Arial',25,'bold')).pack(side=TOP)
 #Heading (Start)
 Middle=Frame(root,bg="grey",borderwidth=5,relief=GROOVE)
 Middle.pack(fill=BOTH)
 #1
 Page_=Label(Middle,text="To Check Pages",font=('Arial'))
 Page_.grid(row=0,column=0)
 #2
 rotate_=Label(Middle,text="To rotate All Pdf Pages",font=('Arial'))
 rotate_.grid(row=1,column=0,pady=5)
 #3
 read_=Label(Middle,text='To Read Pdf in Text Format',font=('Arial'))
 read_.grid(row=2,column=0,pady=5)
 #4
 Merg_=Label(Middle,text="Merge Two Pdf's",font=('Arial'))
 Merg_.grid(row=3,column=0,pady=5)
 #5
 split_=Label(Middle,text="Split's The Pdf",font=('Arial')) 
 split_.grid(row=4,column=0,pady=5)
 #6
 extract=Label(Middle,text="Extract Pages",font=("Arial"))
 extract.grid(row=5,column=0,pady=5)
 #7
 rm=Label(Middle,text="Remove page from pdf",font=('Arial'))
 rm.grid(row=6,column=0,pady=5)
 #8
 water=Label(Middle,text='To watermark pdf',font=('Arial'))
 water.grid(row=7,column=0,pady=5)
 #Button
 b1=Button(Middle,text='click',command=cb1)
 b1.grid(row=0,column=2,padx=5)

 b2=Button(Middle,text='click',command=cb2)
 b2.grid(row=1,column=2,padx=5)

 b3=Button(Middle,text='click',command=cb3)
 b3.grid(row=2,column=2,padx=5)

 b4=Button(Middle,text='click',command=cb4)
 b4.grid(row=3,column=2,padx=5)

 b5=Button(Middle,text='click',command=cb5)
 b5.grid(row=4,column=2,padx=5)

 b6=Button(Middle,text='click',command=cb6)
 b6.grid(row=5,column=2,padx=5)

 b7=Button(Middle,text='click',command=cb7)
 b7.grid(row=6,column=2,padx=5)

 b8=Button(Middle,text='click',command=cb8)
 b8.grid(row=7,column=2,padx=5)
 Label(root,text='''To Edit The Pdf Put 
 It In PDF_EDITOR Dicetory''').pack(side=TOP)
 Label(root,text='This project is made by subhyoyo',font=('Arial',9)).pack(side=BOTTOM)

root=Tk()
root.geometry('400x500')
root.maxsize(400,500)
root.minsize(400,500)
Gui_setup()
root.mainloop()
