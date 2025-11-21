from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinter import messagebox
from PIL import Image, ImageFilter, ImageEnhance, ImageOps 

# --- Global Variables (English) ---
main_window, canvas, paper = [None] * 3
# original_photo: original PIL image, current_photo: currently processed PIL image
original_photo, current_photo = None, None
original_width, original_height, new_width, new_height = 0, 0, 0, 0
input_filepath = "" # Current file path

# --- Function Definitions (English) ---

def display_image(img, width, height):
    """
    Displays the given PIL image object on the Tkinter canvas, 
    updating the window size to fit the image.
    """
    global main_window, canvas, paper, original_photo, current_photo, original_width, original_height, new_width, new_height
    
    if canvas != None:
        canvas.destroy() # Remove previous canvas

    # Update dimensions
    new_width, new_height = width, height
    # Adjust window size (+50 for menu bar and padding)
    main_window.geometry(str(new_width) + "x" + str(new_height + 50)) 
    
    # Create new canvas
    canvas = Canvas(main_window, width=new_width, height=new_height)
    paper = PhotoImage(width=new_width, height=new_height)
    canvas.create_image((new_width/2, new_height/2), image=paper, state="normal")
    
    # Convert PIL Image to Tkinter PhotoImage for display (Pixel by Pixel)
    rgbImage = img.convert("RGB")
    for i in range(new_height):
        for k in range(new_width):
            r, g, b = rgbImage.getpixel((k, i))
            tempStr = "#%02x%02x%02x" % (r, g, b)
            paper.put(tempStr, (k, i))
    
    canvas.pack()

def check_image_open():
    """
    Utility function to check if an image is currently loaded.
    """
    global current_photo
    if current_photo is None:
        messagebox.showwarning("Warning", "Please open a file first.")
        return False
    return True

# --- File Operations ---

def file_open():
    """Opens an image file and displays it."""
    global main_window, original_photo, current_photo, original_width, original_height, input_filepath
    readFp = askopenfilename(parent=main_window, filetypes=(
        ("All Picture Files", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"), ("All Files", "*.*")))
    
    if readFp == "":
        return
        
    input_filepath = readFp
    original_photo = Image.open(input_filepath).convert('RGB')
    original_width = original_photo.width
    original_height = original_photo.height
    
    current_photo = original_photo.copy()
    display_image(current_photo, original_width, original_height)

def file_save():
    """Saves the currently processed image."""
    global main_window, current_photo
    if not check_image_open(): return

    saveFp = asksaveasfilename(parent=main_window, mode='w', defaultextension=".jpg", 
                               filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
    
    if saveFp == "":
        return
        
    current_photo.save(saveFp)

def program_exit():
    """Exits the program."""
    main_window.quit()
    main_window.destroy()

# --- Image Processing (1) - Adjustments & Simple Transforms ---

def adjust_brighten():
    """Increases image brightness."""
    global current_photo, new_width, new_height
    if not check_image_open(): return
    
    value = askfloat("Brighten", "Increase value (1.0 to 2.0)", minvalue=1.0, maxvalue=2.0)
    if value is not None:
        current_photo = current_photo.copy()
        enhancer = ImageEnhance.Brightness(current_photo)
        current_photo = enhancer.enhance(value)
        display_image(current_photo, new_width, new_height)

def adjust_darken():
    """Decreases image brightness."""
    global current_photo, new_width, new_height
    if not check_image_open(): return

    value = askfloat("Darken", "Decrease value (0.0 to 1.0)", minvalue=0.0, maxvalue=1.0)
    if value is not None:
        current_photo = current_photo.copy()
        enhancer = ImageEnhance.Brightness(current_photo)
        current_photo = enhancer.enhance(value)
        display_image(current_photo, new_width, new_height)

def convert_grayscale():
    """Converts image to grayscale."""
    global current_photo, new_width, new_height
    if not check_image_open(): return

    current_photo = current_photo.convert('L').convert('RGB')
    display_image(current_photo, new_width, new_height)

def transform_v_flip():
    """Flips image vertically (Mirror)."""
    global current_photo, new_width, new_height
    if not check_image_open(): return
    
    current_photo = current_photo.copy()
    current_photo = current_photo.transpose(Image.FLIP_TOP_BOTTOM)
    display_image(current_photo, new_width, new_height)

def transform_h_flip():
    """Flips image horizontally."""
    global current_photo, new_width, new_height
    if not check_image_open(): return
    
    current_photo = current_photo.copy()
    current_photo = current_photo.transpose(Image.FLIP_LEFT_RIGHT)
    display_image(current_photo, new_width, new_height)

def transform_rotate():
    """Rotates the image by a user-defined angle."""
    global current_photo
    if not check_image_open(): return
    
    angle = askinteger("Rotate", "Rotation Angle (0~360)", minvalue=0, maxvalue=360)
    if angle is not None:
        current_photo = current_photo.copy()
        current_photo = current_photo.rotate(angle, expand=True) 
        display_image(current_photo, current_photo.width, current_photo.height)

# --- Image Processing (2) - Size & Filters ---

def resize_zoomin():
    """Enlarges the image."""
    global current_photo
    if not check_image_open(): return
    
    scale = askinteger("Zoom In", "Enter scale factor (2~4)", minvalue=2, maxvalue=4)
    if scale is not None:
        w = int(current_photo.width * scale)
        h = int(current_photo.height * scale)
        current_photo = current_photo.copy()
        current_photo = current_photo.resize((w, h))
        display_image(current_photo, w, h)

def resize_zoomout():
    """Shrinks the image."""
    global current_photo
    if not check_image_open(): return
        
    scale = askinteger("Zoom Out", "Enter scale factor (2~4)", minvalue=2, maxvalue=4)
    if scale is not None:
        w = int(current_photo.width / scale)
        h = int(current_photo.height / scale)
        current_photo = current_photo.copy()
        current_photo = current_photo.resize((w, h))
        display_image(current_photo, w, h)

def filter_blur():
    """Applies a blur filter."""
    global current_photo, new_width, new_height
    if not check_image_open(): return
    
    current_photo = current_photo.copy()
    current_photo = current_photo.filter(ImageFilter.BLUR)
    display_image(current_photo, new_width, new_height)

def filter_sharpen():
    """Applies a sharpen filter."""
    global current_photo, new_width, new_height
    if not check_image_open(): return
    
    current_photo = current_photo.copy()
    current_photo = current_photo.filter(ImageFilter.SHARPEN)
    display_image(current_photo, new_width, new_height)

def filter_emboss():
    """Applies an emboss filter."""
    global current_photo, new_width, new_height
    if not check_image_open(): return
    
    current_photo = current_photo.copy()
    current_photo = current_photo.filter(ImageFilter.EMBOSS)
    display_image(current_photo, new_width, new_height)

def filter_contour():
    """Applies a contour (edge detection) filter."""
    global current_photo, new_width, new_height
    if not check_image_open(): return
    
    current_photo = current_photo.copy()
    current_photo = current_photo.filter(ImageFilter.CONTOUR)
    display_image(current_photo, new_width, new_height)

def filter_detail():
    """Applies a detail enhancement filter."""
    global current_photo, new_width, new_height
    if not check_image_open(): return
    current_photo = current_photo.copy()
    current_photo = current_photo.filter(ImageFilter.DETAIL)
    display_image(current_photo, new_width, new_height)

def adjust_color_boost():
    """Enhances or reduces color saturation."""
    global current_photo, new_width, new_height
    if not check_image_open(): return
    
    value = askinteger("Color Boost", "Color enhancement (0~200)", minvalue=0, maxvalue=200)
    if value is not None:
        current_photo = current_photo.copy()
        enhancer = ImageEnhance.Color(current_photo)
        current_photo = enhancer.enhance(value / 100.0) 
        display_image(current_photo, new_width, new_height)

# --- Main GUI Setup ---

main_window = Tk()
main_window.geometry("250x150")
main_window.title("Mini Photoshop")

main_menu = Menu(main_window)
main_window.config(menu=main_menu)

# File Menu
file_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open File", command=file_open)
file_menu.add_command(label="Save File", command=file_save)
file_menu.add_separator()
file_menu.add_command(label="Exit Program", command=program_exit)

# Image Processing (1) Menu - Adjustments & Transforms
adjust_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Adjust (1)", menu=adjust_menu)
adjust_menu.add_command(label="Brighten", command=adjust_brighten)
adjust_menu.add_command(label="Darken", command=adjust_darken)
adjust_menu.add_separator()
adjust_menu.add_command(label="Grayscale", command=convert_grayscale)
adjust_menu.add_command(label="Vertical Flip", command=transform_v_flip)
adjust_menu.add_command(label="Horizontal Flip", command=transform_h_flip)
adjust_menu.add_command(label="Rotate", command=transform_rotate)

# Image Processing (2) Menu - Filters & Size
filter_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Filter & Resize (2)", menu=filter_menu)
filter_menu.add_command(label="Zoom In", command=resize_zoomin)
filter_menu.add_command(label="Zoom Out", command=resize_zoomout)
filter_menu.add_separator()
filter_menu.add_command(label="Blur", command=filter_blur)
filter_menu.add_command(label="Sharpen", command=filter_sharpen)
filter_menu.add_command(label="Emboss", command=filter_emboss)
filter_menu.add_command(label="Contour", command=filter_contour)
filter_menu.add_command(label="Detail", command=filter_detail) 
filter_menu.add_command(label="Color Boost", command=adjust_color_boost)

# --- Start the Main Event Loop ---
main_window.mainloop()