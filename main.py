from tkinter import *
import tkinter as tk
import os
from utils import cut_main_video

root = tk.Tk()

root.title("Tik Tok Soft")
root.geometry("1000x500")  # трішки ширше

# Головний контейнер для всіх блоків
main_frame = Frame(root)
main_frame.pack(padx=20, pady=20)

# ==== Left block: Origin Videos ====
origin_list_of_video_files = os.listdir("videos")

left_frame = Frame(main_frame)
left_frame.pack(side='left', padx=10)

videos_block_label = Label(left_frame, text="Origin Video", font=("Arial", 12, "bold"))
videos_block_label.pack()

listbox = tk.Listbox(left_frame, width=30, height=20)

for it in origin_list_of_video_files:
    listbox.insert(tk.END, it)
listbox.pack()

def click_cut_main_btn():
    selection = listbox.curselection()
    if selection:  # перевіряємо, чи щось вибрано
        index = selection[0]
        selected_item = listbox.get(index)
        full_path = os.path.join("videos", selected_item)
        cut_main_video(full_path)
    else:
        print("Нічого не вибрано")

cut_main_video_btn = tk.Button(left_frame, text="Cut Main Video (1m)", command=click_cut_main_btn)
cut_main_video_btn.pack(pady=10)  




























# ==== Middle block: Origin Video Timelines ====
origin_cut_videos_timelines = os.listdir("origin_video_cut")

middle_frame = Frame(main_frame)
middle_frame.pack(side='left', padx=10)

middle_label = Label(middle_frame, text="Origin Video Timelines", font=("Arial", 12, "bold"))
middle_label.pack()

middle_listbox = tk.Listbox(middle_frame, width=30, height=20)
for origin_cut_item in origin_cut_videos_timelines:
    middle_listbox.insert(tk.END, origin_cut_item)
middle_listbox.pack()

cut_short_video_btn = tk.Button(middle_frame, text="Cut Short Videos (1m)")
cut_short_video_btn.pack(pady=10)

# ==== Right block: Short Video Templates ====
short_videos_files = os.listdir("short_video_templates")

right_frame = Frame(main_frame)
right_frame.pack(side='left', padx=10)

short_video_templates_label = Label(right_frame, text="Bottom Video Templates", font=("Arial", 12, "bold"))
short_video_templates_label.pack()

right_listbox = tk.Listbox(right_frame, width=30, height=20)

for short_video_path in short_videos_files:
    right_listbox.insert(tk.END, short_video_path)
right_listbox.pack()

generete_tik_tok = tk.Button(right_frame, text="Generate")
generete_tik_tok.pack(pady=10)

root.mainloop()