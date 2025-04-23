import tkinter as tk
from tkinter import filedialog, messagebox

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        # 创建菜单栏
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="打开 OFD 文件", command=self.open_ofd_file)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)
        menubar.add_cascade(label="文件", menu=file_menu)
        self.root.config(menu=menubar)

        # 创建主显示区域
        self.text_area = tk.Text(self.root, wrap="word")
        self.text_area.pack(expand=1, fill="both")

    def open_ofd_file(self):
        file_path = filedialog.askopenfilename(
            title="选择 OFD 文件",
            filetypes=[("OFD 文件", "*.ofd"), ("所有文件", "*.*")]
        )
        if file_path:
            try:
                # 这里可以调用解析 OFD 文件的逻辑
                content = self.parse_ofd(file_path)
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("错误", f"无法打开文件: {e}")

    def parse_ofd(self, file_path):
        # 简单模拟解析 OFD 文件的逻辑
        # 实际上需要根据 OFD 文件格式解析内容
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()