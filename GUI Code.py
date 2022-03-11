يمكنك التحكم في نص الملصقات والألوان الخلفية باستخدام المعلمات المقدمة والخلفية:
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black"  # Set the background color to black
.........................................................
يمكنك أيضا تحديد لون باستخدام قيم RGB السداسية:
label = tk.Label(text="Hello, Tkinter", background="#34A2FE")

...................................................
إذا كنت لا تشعر وكأنك كتابة المقدمة والخلفية في كل وقت، فيمكنك استخدام معلمات الاختصار FG و BG لتعيين ألوان الأمامية والخلفية:
label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
................................................
import tkinter as tk
 
window = tk.Tk()
frame = tk.Frame()
frame.pack()
window.mainloop()
...................................................
import tkinter as tk
 
window = tk.Tk()
 
frame_a = tk.Frame()
frame_b = tk.Frame()
 
label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()
 
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()
 
frame_a.pack()
frame_b.pack()
window.mainloop()

..................................................
الآن نرى ما يحدث عند تبديل ترتيب frame_a.pack () و frame_b.pack ():
import tkinter as tk
 
window = tk.Tk()
 
frame_a = tk.Frame()
label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()
 
frame_b = tk.Frame()
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()
 
# Swap the order of `frame_a` and `frame_b`
frame_b.pack()
frame_a.pack()
 
window.mainloop()
 
..............................................................
ثلاثة من الحاجيات التسمية في إطار:
import tkinter as tk
 
window = tk.Tk()
 
frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack()
 
frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()
 
frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack()
window.mainloop()
..................................................
إليك كيفية تكديس الإطارات الثلاثة حتى يملأ كل واحد النافذة بأكمله أفقيا:
import tkinter as tk
window = tk.Tk()
frame1 = tk.Frame(master=window, height=100, bg="red")
frame1.pack(fill=tk.X)
frame2 = tk.Frame(master=window, height=50, bg="yellow")
frame2.pack(fill=tk.X)
frame3 = tk.Frame(master=window, height=25, bg="blue")
frame3.pack(fill=tk.X)
 
window.mainloop()
........................................................
import tkinter as tk
 
window = tk.Tk()
 
frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.Y, side=tk.LEFT)
 
frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.Y, side=tk.LEFT)
 
frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.Y, side=tk.LEFT)
 
window.mainloop()
..............................................
لجعل التخطيط استجابة حقا، يمكنك تعيين حجم أولي لإطاراتك باستخدام سمات العرض والارتفاع. ثم، قم بتعيين وسيطة ملء الكلمة الأساسية من .Pack () إلى TK.Both وتعيين وسيطة توسيع الكلمة الرئيسية إلى TRUE:
import tkinter as tk
window = tk.Tk()
frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
 
frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
 
frame3 = tk.Frame(master=window, width=50, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
 
window.mainloop()
........................................................
إليك مثال على كيفية عمل. بليس () مدير الهندسة يعمل:
import tkinter as tk
 3window = tk.Tk()
 5frame = tk.Frame(master=window, width=150, height=150)
 6frame.pack()
 8label1 = tk.Label(master=frame, text="I'm at (0, 0)", bg="red")
 9label1.place(x=0, y=0)
11label2 = tk.Label(master=frame, text="I'm at (75, 75)", bg="yellow")
12label2.place(x=75, y=75)
14window.mainloop()
.................................
البرنامج النصي التالي يخلق شبكة 3 × 3 من الإطارات مع الحاجيات التسمية معبأة فيها:
import tkinter as tk
window = tk.Tk()
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
 
window.mainloop()
....................................................
يتم استخدام مديري هندسيين في هذا المثال. يتم إرفاق كل إطار في النافذة باستخدام مدير الهندسة .GRID:
import tkinter as tk
 
window = tk.Tk()
 
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
 
window.mainloop()
...............................................................
يتم توصيل كل ملصق بإطار ماجستير مع .Pack ():
import tkinter as tk
 
window = tk.Tk()
 
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack()
 
window.mainloop()
...................................................
 
.Pack () لديها أيضا المعلمات padx و pady. التعليمة البرمجية التالية متطابقة تقريبا إلى الرمز السابق، إلا أنك تضيف 5 بكسل من الحشو الإضافي حول كل ملصق في كل من الاتجاهات x و y:
import tkinter as tk
 
window = tk.Tk()
 
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
 
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)
 
window.mainloop()
...................................................
لتحسين تغيير حجم نافذة:
import tkinter as tk
 
window = tk.Tk()
 
for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)
 
    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
 
        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)
 
window.mainloop()
.......................................................
جربه بنفسك للحصول على شعور بكيفية العمل! قم بالتشغيل مع الوزن والمعلمات Minsize لمعرفة كيف تؤثر على الشبكة.
import tkinter as tk
 
window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)
 
label1 = tk.Label(text="A")
label1.grid(row=0, column=0)
 
label2 = tk.Label(text="B")
label2.grid(row=1, column=0)
 
window.mainloop()
تأتي الحروف "N"، "S"، "E"، و "W" من الاتجاهات الكاردينال الشمالية والجنوب والشرق والغرب. إعداد لزجة إلى "n" على كلا الملصقتين في التعليمات البرمجية السابقة وظائف كل ملصق في أعلى مركز خلية الشبكة:
import tkinter as tk
 
window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)
 
label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="n")
 
label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="n")
 
window.mainloop()
............................................
 
يمكنك الجمع بين أحرف متعددة في سلسلة واحدة لوضع كل تسمية في زاوية خلية الشبكة:
import tkinter as tk
 
window = tk.Tk()
window.columnconfigure(0, minsize=250)
window.rowconfigure([0, 1], minsize=100)
 
label1 = tk.Label(text="A")
label1.grid(row=0, column=0, sticky="ne")
 
label2 = tk.Label(text="B")
label2.grid(row=1, column=0, sticky="sw")
 
window.mainloop()
.................................................
import tkinter as tk
 
window = tk.Tk()
 
window.rowconfigure(0, minsize=50)
window.columnconfigure([0, 1, 2, 3], minsize=50)
 
label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")
 
label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky="ew")
label3.grid(row=0, column=2, sticky="ns")
label4.grid(row=0, column=3, sticky="nsew")
 
window.mainloop()

.................................................
للاتصال معالج الأحداث:
    import tkinter as tk
 
window = tk.Tk()
 
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)
 
# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)
 
window.mainloop()
...............................................................
سيزيد من القيمة. :
import tkinter as tk
 
window = tk.Tk()
 
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)
 
btn_decrease = tk.Button(master=window, text="-")
btn_decrease.grid(row=0, column=0, sticky="nsew")
 
lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)
 
btn_increase = tk.Button(master=window, text="+")
btn_increase.grid(row=0, column=2, sticky="nsew")
 
window.mainloop()
لا تحتوي الحاجيات على التسمية .GET () مثل الدخول والنصوص الخاصة بالدخول. ومع ذلك، يمكنك استرداد النص من الملصق عن طريق الوصول إلى سمة النص مع تدوين فرص على طراز قاموس:
label = Tk.Label(text="Hello")
 
# Retrieve a Label's text
text = label["text"]
 
# Set new text for the label
label["text"] = "Good bye"
......................................................
الآن قم بتعيين النقص () لتقليل_Button:
btn_decrease = tk.Button(master=window, text="-", command=decrease)
الآن بعد أن تعرف ما هي الحاجيات التي تحتاجها وماذا تبدو النافذة، يمكنك أن تبدأ ترميزه! أولا، استيراد Tkinter وإنشاء نافذة جديدة:
import tkinter as tk
 
window = tk.Tk()
window.title("Temperature Converter")
..........................................................
تحديث البرنامج:
    import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
 
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
 
window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
 
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...")
 
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
 
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
 
window.mainloop()
بعد ذلك، أضف تعريف Save_File () فقط أسفل تعريف Open_File ():
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
 
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
 
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")
 
window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
 
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...")
 
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
 
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
 
window.mainloop()
أخيرا، قم بتعيين سمة الأمر btn_save إلى save_file:
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
 
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
 
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")
 
window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
 
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
 
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
 
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
window.mainloop()
 
..............................................................