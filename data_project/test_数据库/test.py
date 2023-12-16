import tkinter as tk
 
# class Test():
#     def __init__(self):
#     #     self.root = tk.Tk()
         
#     #     self.frm1 = tk.Frame(self.root)
         
#     #     self.entry_value = tk.StringVar()
#     #     self.entry1 = tk.Entry(self.frm1,textvariable = self.entry_value)
         
#     #     self.listbox1 = tk.Listbox(self.frm1)
         
#     #     self.base_selection_list = ["A","AB","ABCD","ABCDE","ABCDEF"]
#     #     #self.set_list_value(self.base_selection_list)
         
#     #     self.entry1.grid(column=0, row=0, padx=10)
#     #     self.listbox1.grid(column=0, row=1, padx=10)
#     #     self.listbox1.grid_remove()
         
#     #     self.frm1.pack()
         
#     #     self.entry1.bind("<KeyRelease>", self.entry_change)
#     #     self.entry1.bind("<Button-3>", self.hide_list)
         
#     #     self.listbox1.bind("<<ListboxSelect>>", self.list_select)
         
#     #     self.root.mainloop()
     
#     # #有输入变化的时候，设置下拉列表，并显示列表
#     # def entry_change(self, event):
#     #     entry_value = self.entry1.get().strip()
         
#     #     self.listbox1.delete(0, self.listbox1.size()-1)
         
#     #     new_select_list = []
#     #     for selection_info in self.base_selection_list:
#     #         if (len(entry_value) > 0) and (entry_value in selection_info):
#     #             new_select_list.append(selection_info)
                 
#     #     print(entry_value, new_select_list)
         
#     #     if len(new_select_list) > 0:
#     #         self.set_list_value(new_select_list)
#     #         #显示出来
#     #         self.listbox1.grid()
#     #     else:
#     #         self.listbox1.grid_remove()
         
#     # def hide_list(self, event):
#     #     self.listbox1.grid_remove()
     
#     # #选择完下拉列表后，直接隐藏
#     # def list_select(self, event):
#     #     index_num = self.listbox1.curselection()[0]
#     #     select_value = self.listbox1.get(index_num)
#     #     self.entry_value.set(select_value)
         
#     #     #隐藏起来
#     #     self.listbox1.grid_remove()
         
#     # def set_list_value(self, value_list):
#     #     #["A","AB","ABCD","ABCDE","ABCDEF"]
#     #     for item in value_list:
#     #         self.listbox1.insert("end",item)
#         self.window_select_inventory= tk.Tk()  # 初始框的声明
#         self.window_select_inventory.geometry('200x200')
#         self.window_select_inventory.title('选择库存')
#         # db = pymysql.connect(host='localhost', port=3306, db='medicine management system', user='root',
#         #                         password='123456')  # 打开数据库连接
#         # cursor = db.cursor()  # 使用cursor()方法获取操作游标
#         # sql = "SELECT * FROM medicine WHERE mname = '%s'" % (self.entry_usr_name.get())  # SQL 查询语句
#         # try:
#         #     # 执行SQL语句
#         #     cursor.execute(sql)
#         #     # 获取所有记录列表
#         #     results = cursor.fetchall()
#         #     for row in results:
#         #         self.window_drug_name_mid.append(row[4])
#         #         # 打印结果
#         # except:
#         #     print("Error")
#         #     flag = False
#         #     messagebox.showinfo('警告！', '错误！')
#         self.window_select_inventory_label_text = tk.StringVar()
#         self.window_select_inventory_label_text.set('初始文本')
#         self.window_select_inventory_label = tk.Label(self.window_select_inventory, textvariable=self.window_select_inventory_label_text, font=('Verdana', 20))
#         self.window_select_inventory_label.pack()

#         # ...

#         self.window_select_inventory_label_text.set('123')
        
# window_select_inventory= tk.Tk()  # 初始框的声明
# window_select_inventory.geometry('200x200')
# window_select_inventory.title('选择库存')
# db = pymysql.connect(host='localhost', port=3306, db='medicine management system', user='root',
#                         password='123456')  # 打开数据库连接
# cursor = db.cursor()  # 使用cursor()方法获取操作游标
# sql = "SELECT * FROM medicine WHERE mname = '%s'" % (self.entry_usr_name.get())  # SQL 查询语句
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         self.window_drug_name_mid.append(row[4])
#         # 打印结果
# except:
#     print("Error")
#     flag = False
#     messagebox.showinfo('警告！', '错误！')
# from tkinter import Tk, Label, StringVar

# def update_label_text():
#     # 更新字符串变量的值
#     var.set("新的文本")

# # 创建Tkinter窗口
# window = Tk()

# # 创建一个字符串变量
# var = StringVar()
# var.set("初始文本")

# # 创建Label部件，并将其与字符串变量绑定
# label = Label(window, textvariable=var)

# # 显示Label部件
# label.pack()


# # 进入Tkinter事件循环
# window.mainloop()
         
         
list_1=['123']
print(list_1[0])