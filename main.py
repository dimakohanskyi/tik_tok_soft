from tkinter import *
import tkinter as tk
import os
import ttkbootstrap as ttb
from tkinter import filedialog
import shutil





root = ttb.Window(themename="darkly")
root.title("Tik Tok Soft")
root.geometry("1400x800")



style = ttb.Style()
style.configure("TLabel", font=("Helvetica", 10))
style.configure("Title.TLabel", font=("Helvetica", 12, "bold"))


main_frame = ttb.Frame(root, padding=15)
main_frame.pack(fill=BOTH, expand=YES)





# Left Column
left_col = ttb.Frame(main_frame)
left_col.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)

# 1. Original Videos
original_videos_frame = ttb.Labelframe(left_col, text=" Original Videos ", bootstyle="info", padding=10)
original_videos_frame.pack(fill=BOTH, pady=5)

original_listbox = tk.Listbox(
    original_videos_frame, 
    height=8,
    selectbackground=style.colors.info,
    selectforeground=style.colors.bg
)
original_listbox.pack(fill=BOTH, expand=YES)




def choose_origi_video_file_system():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("Video Files", "*.mp4 *.mov *.avi"), ("All Files", "*.*")]
    )
    if file_path:
        print("Selected file:", file_path)
        destination_dir = "/Users/user/Desktop/projects/python_projects/tik_tok_soft/videos"
        
        file_name = file_path.split("/")[-1]
        destination_path = os.path.join(destination_dir, file_name)

        try:
            shutil.copy(file_path, destination_path)
            update_video_listbox()
            print(f"Файл '{file_name}' успішно скопійовано в '{destination_dir}'")
        except Exception as Ex:
            print(f"Сталася помилка при копіюванні файлу: {Ex}")

ttb.Button(original_videos_frame, text="Add Video", command=choose_origi_video_file_system, bootstyle="info-outline").pack(side=tk.LEFT, padx=10, pady=10)





def click_cut_main_btn():
    selection = listbox.curselection()
    if selection: 
        index = selection[0]
        selected_item = listbox.get(index)
        full_path = os.path.join("videos", selected_item)
        print(full_path)
        # cut_main_video(full_path)

    else:
        print("Нічого не вибрано")


ttb.Button(original_videos_frame, text="Cut (1m)", command=click_cut_main_btn, bootstyle="info-outline").pack(side=tk.LEFT, padx=10, pady=10)




# 2. Video Timelines
video_timelines_frame = ttb.Labelframe(left_col, text=" Video Timelines ", bootstyle="warning", padding=10)
video_timelines_frame.pack(fill=BOTH, pady=5)

timelines_listbox = tk.Listbox(
    video_timelines_frame,
    height=8,
    selectbackground=style.colors.warning,
    selectforeground=style.colors.bg
)
timelines_listbox.pack(fill=BOTH, expand=YES)
ttb.Button(video_timelines_frame, text="Select Timeline", bootstyle="warning-outline").pack(pady=5)









# Middle Column
middle_col = ttb.Frame(main_frame)
middle_col.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)

# 3. Short Videos
short_videos_frame = ttb.Labelframe(middle_col, text=" Short Videos ", bootstyle="info", padding=10)
short_videos_frame.pack(fill=BOTH, pady=5)

short_listbox = tk.Listbox(
    short_videos_frame,
    height=8,
    selectbackground=style.colors.danger,
    selectforeground=style.colors.bg
)
short_listbox.pack(fill=BOTH, expand=YES)
ttb.Button(short_videos_frame, text="Process Shorts", bootstyle="info-outline").pack(pady=5)

# 4. Short Video Timelines
short_timelines_frame = ttb.Labelframe(middle_col, text=" Short Timelines ", bootstyle="warning", padding=10)
short_timelines_frame.pack(fill=BOTH, pady=5)

short_timelines_listbox = tk.Listbox(
    short_timelines_frame,
    height=8,
    selectbackground=style.colors.primary,
    selectforeground=style.colors.bg
)
short_timelines_listbox.pack(fill=BOTH, expand=YES)
ttb.Button(short_timelines_frame, text="Select Short", bootstyle="warning-outline").pack(pady=5)







# Right Column
right_col = ttb.Frame(main_frame)
right_col.pack(side=LEFT, fill=BOTH, padx=10, expand=YES)





# 5. TikTok Set
tiktok_set_frame = ttb.Labelframe(right_col, text=" TikTok Set ", bootstyle="success", padding=10)
tiktok_set_frame.pack(fill=BOTH, pady=5)

set_listbox = tk.Listbox(
    tiktok_set_frame,
    height=8,
    selectbackground=style.colors.success,
    selectforeground=style.colors.bg
)
set_listbox.pack(fill=BOTH, expand=YES)
ttb.Button(tiktok_set_frame, text="Clear Selection",bootstyle="success-outline").pack(pady=5)






# 6. TikTok Ready
tiktok_ready_frame = ttb.Labelframe(right_col, text=" Ready Videos ", bootstyle="light", padding=10)
tiktok_ready_frame.pack(fill=BOTH, pady=5)

ready_listbox = tk.Listbox(
    tiktok_ready_frame,
    height=8,
    selectbackground=style.colors.light,
    selectforeground=style.colors.dark
)
ready_listbox.pack(fill=BOTH, expand=YES)
ttb.Button(tiktok_ready_frame, text="Export Videos", bootstyle="light-outline").pack(pady=5)




def update_all_lists():
    update_listbox(original_listbox, "videos")
    update_listbox(timelines_listbox, "video_timelines")
    update_listbox(short_listbox, "short_videos")
    update_listbox(short_timelines_listbox, "short_videos_timelines")
    update_listbox(set_listbox, "set_for_tik_tok")
    update_listbox(ready_listbox, "ready_videos")

def update_listbox(listbox_widget, folder):
    listbox_widget.delete(0, END)
    try:
        for item in os.listdir(folder):
            listbox_widget.insert(END, item)
    except FileNotFoundError:
        os.makedirs(folder)

update_all_lists()













def choose_timeline():
    selection = middle_listbox.curselection()
    
    if selection: 
        index = selection[0]
        selected_item = middle_listbox.get(index)
        full_path = os.path.join("/Users/user/Desktop/projects/python_projects/tik_tok_soft/origin_video_cut", selected_item)

        dir_to_copy = "/Users/user/Desktop/projects/python_projects/tik_tok_soft/set_for_tik_tok" 
        
        if full_path:
            try:
                shutil.copy(full_path, dir_to_copy)
                update_origin_videos_timelines_listbox()
                update_set_for_tik_tok_listbox()
            except Exception as Ex:
                print(f"Сталася помилка при копіюванні файлу: {Ex}")

    else:
        print("Нічого не вибрано")
    


def cut_short_videos():
    ...



def choose_short_video_timeline():
    selection = right_container_for_ready_short_videos_listbox.curselection()
    
    if selection: 
        index = selection[0]
        file_dir = "/Users/user/Desktop/projects/python_projects/tik_tok_soft/short_videos_timelines"
        selected_item = right_container_for_ready_short_videos_listbox.get(index)
        full_path = os.path.join(file_dir, selected_item)
        destionation_dir = "/Users/user/Desktop/projects/python_projects/tik_tok_soft/set_for_tik_tok"

        if full_path:
            try:
                shutil.copy(full_path,destionation_dir)
                update_short_video_timelines_listbox()
                update_set_for_tik_tok_listbox()
            except Exception as Ex:
                print(f"Сталася помилка при копіюванні файлу: {Ex}")

    else:
        print("Нічого не вибрано")





root.mainloop()