from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinter import messagebox
from PIL import Image, ImageFilter, ImageEnhance, ImageOps 

# --- 전역 변수 (Global Variables) ---
window, canvas, paper = [None] * 3
# photo: original PIL image, photo2: currently processed PIL image
photo, photo2 = None, None
oriX, oriY, newX, newY = 0, 0, 0, 0
inFileName = "" # Current file path

# --- 함수 선언 부분 (Function Definitions) ---

def displayImage(img, width, height):
    """
    주어진 PIL 이미지를 Tkinter 캔버스에 표시하고, 윈도우 크기를 이미지에 맞게 조절합니다.
    """
    global window, canvas, paper, photo, photo2, oriX, oriY, newX, newY
    
    if canvas != None:
        canvas.destroy() # 이전 캔버스 제거

    # 치수 업데이트
    newX, newY = width, height
    # 윈도우 크기 조절 (+50은 메뉴바를 위한 공간)
    window.geometry(str(newX) + "x" + str(newY + 50)) 
    
    # 새 캔버스 생성
    canvas = Canvas(window, width=newX, height=newY)
    paper = PhotoImage(width=newX, height=newY)
    canvas.create_image((newX/2, newY/2), image=paper, state="normal")
    
    # PIL 이미지를 Tkinter PhotoImage로 변환하여 표시 (픽셀 단위 변환)
    rgbImage = img.convert("RGB")
    for i in range(newY):
        for k in range(newX):
            r, g, b = rgbImage.getpixel((k, i))
            # RGB 값을 16진수 색상 문자열로 변환
            tempStr = "#%02x%02x%02x" % (r, g, b)
            paper.put(tempStr, (k, i))
    
    canvas.pack()

def check_image_open():
    """
    이미지가 로드되었는지 확인하는 유틸리티 함수입니다.
    """
    global photo2
    if photo2 is None:
        messagebox.showwarning("경고", "파일을 먼저 열어주세요.")
        return False
    return True

# --- 파일 작업 (File Operations) ---

def func_open():
    """이미지 파일을 열고 표시합니다."""
    global window, photo, photo2, oriX, oriY, inFileName
    readFp = askopenfilename(parent=window, filetypes=(
        ("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"), ("모든 파일", "*.*")))
    
    if readFp == "":
        return
        
    inFileName = readFp
    photo = Image.open(inFileName).convert('RGB')
    oriX = photo.width
    oriY = photo.height
    
    photo2 = photo.copy()
    displayImage(photo2, oriX, oriY)

def func_save():
    """현재 처리된 이미지를 저장합니다."""
    global window, photo2
    if not check_image_open(): return

    saveFp = asksaveasfilename(parent=window, mode='w', defaultextension=".jpg", 
                               filetypes=(("JPG 파일", "*.jpg"), ("PNG 파일", "*.png"), ("모든 파일", "*.*")))
    
    if saveFp == "":
        return
        
    photo2.save(saveFp)

def func_exit():
    """프로그램을 종료합니다."""
    window.quit()
    window.destroy()

# --- 이미지 처리(1) - 조정 및 간단한 변형 ---

def func_bright():
    """이미지 밝기를 증가시킵니다 (밝게)."""
    global photo2, newX, newY
    if not check_image_open(): return
    
    # 밝기 증가량 요청 (1.0~2.0)
    value = askfloat("밝게", "밝기 증가량(1.0~2.0)", minvalue=1.0, maxvalue=2.0)
    if value is not None:
        photo2 = photo2.copy()
        enhancer = ImageEnhance.Brightness(photo2)
        photo2 = enhancer.enhance(value)
        displayImage(photo2, newX, newY)

def func_dark():
    """이미지 밝기를 감소시킵니다 (어둡게)."""
    global photo2, newX, newY
    if not check_image_open(): return

    # 밝기 감소량 요청 (0.0~1.0)
    value = askfloat("어둡게", "밝기 감소량(0.0~1.0)", minvalue=0.0, maxvalue=1.0)
    if value is not None:
        photo2 = photo2.copy()
        enhancer = ImageEnhance.Brightness(photo2)
        photo2 = enhancer.enhance(value)
        displayImage(photo2, newX, newY)

def func_grayscale():
    """이미지를 흑백으로 변환합니다 (흑백)."""
    global photo2, newX, newY
    if not check_image_open(): return

    photo2 = photo2.convert('L').convert('RGB')
    displayImage(photo2, newX, newY)

def func_mirror():
    """이미지를 상하 반전합니다."""
    global photo2, newX, newY
    if not check_image_open(): return
    
    photo2 = photo2.copy()
    photo2 = photo2.transpose(Image.FLIP_TOP_BOTTOM)
    displayImage(photo2, newX, newY)

def func_flips():
    """이미지를 좌우 반전합니다."""
    global photo2, newX, newY
    if not check_image_open(): return
    
    photo2 = photo2.copy()
    photo2 = photo2.transpose(Image.FLIP_LEFT_RIGHT)
    displayImage(photo2, newX, newY)

def func_rotate():
    """사용자가 정의한 각도로 이미지를 회전합니다."""
    global photo2
    if not check_image_open(): return
    
    angle = askinteger("회전", "회전 각도(0~360)", minvalue=0, maxvalue=360)
    if angle is not None:
        photo2 = photo2.copy()
        # expand=True는 회전된 이미지에 맞게 캔버스 크기를 확장합니다.
        photo2 = photo2.rotate(angle, expand=True) 
        displayImage(photo2, photo2.width, photo2.height)

# --- 이미지 처리(2) - 크기 및 필터 ---

def func_zoomin():
    """이미지를 확대합니다."""
    global photo2
    if not check_image_open(): return
    
    scale = askinteger("확대", "확대할 배율을 입력하세요 (2~4)", minvalue=2, maxvalue=4)
    if scale is not None:
        new_width_scaled = int(photo2.width * scale)
        new_height_scaled = int(photo2.height * scale)
        photo2 = photo2.copy()
        photo2 = photo2.resize((new_width_scaled, new_height_scaled))
        displayImage(photo2, new_width_scaled, new_height_scaled)

def func_zoomout():
    """이미지를 축소합니다."""
    global photo2
    if not check_image_open(): return
        
    scale = askinteger("축소", "축소할 배율을 입력하세요 (2~4)", minvalue=2, maxvalue=4)
    if scale is not None:
        new_width_scaled = int(photo2.width / scale)
        new_height_scaled = int(photo2.height / scale)
        photo2 = photo2.copy()
        photo2 = photo2.resize((new_width_scaled, new_height_scaled))
        displayImage(photo2, new_width_scaled, new_height_scaled)

def func_blur():
    """흐림 필터를 적용합니다."""
    global photo2, newX, newY
    if not check_image_open(): return
    
    photo2 = photo2.copy()
    photo2 = photo2.filter(ImageFilter.BLUR)
    displayImage(photo2, newX, newY)

def func_sharpen():
    """선명하게 필터를 적용합니다."""
    global photo2, newX, newY
    if not check_image_open(): return
    
    photo2 = photo2.copy()
    photo2 = photo2.filter(ImageFilter.SHARPEN)
    displayImage(photo2, newX, newY)

def func_emboss():
    """엠보싱 필터를 적용합니다."""
    global photo2, newX, newY
    if not check_image_open(): return
    
    photo2 = photo2.copy()
    photo2 = photo2.filter(ImageFilter.EMBOSS)
    displayImage(photo2, newX, newY)

def func_contour():
    """경계선(윤곽) 필터를 적용합니다."""
    global photo2, newX, newY
    if not check_image_open(): return
    
    photo2 = photo2.copy()
    photo2 = photo2.filter(ImageFilter.CONTOUR)
    displayImage(photo2, newX, newY)

def func_detail():
    """세부 묘사 필터를 적용합니다."""
    global photo2, newX, newY
    if not check_image_open(): return
    photo2 = photo2.copy()
    photo2 = photo2.filter(ImageFilter.DETAIL)
    displayImage(photo2, newX, newY)

def func_color():
    """색상 채도를 강조하거나 줄입니다."""
    global photo2, newX, newY
    if not check_image_open(): return
    
    # 색상 강화량 요청 (0~200, 100은 원본)
    value = askinteger("색상 강조", "색상 강화량(0~200)", minvalue=0, maxvalue=200)
    if value is not None:
        photo2 = photo2.copy()
        enhancer = ImageEnhance.Color(photo2)
        # 정수 입력을 실수 비율로 변환 (예: 200 -> 2.0)
        photo2 = enhancer.enhance(value / 100.0) 
        displayImage(photo2, newX, newY)

# --- 메인 GUI 설정 (Main GUI Setup) ---

window = Tk()
window.geometry("250x150")
window.title("미니 포토샵") # 윈도우 제목: Mini Photoshop

mainMenu = Menu(window)
window.config(menu=mainMenu)

# 파일 메뉴
fileMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일 열기", command=func_open)
fileMenu.add_command(label="파일 저장", command=func_save)
fileMenu.add_separator()
fileMenu.add_command(label="프로그램 종료", command=func_exit)

# 이미지 처리(1) 메뉴 (조정/변환)
imageMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="이미지 처리(1)", menu=imageMenu)
imageMenu.add_command(label="밝게", command=func_bright)
imageMenu.add_command(label="어둡게", command=func_dark)
imageMenu.add_separator()
imageMenu.add_command(label="흑백", command=func_grayscale)
imageMenu.add_command(label="상하 반전", command=func_mirror)
imageMenu.add_command(label="좌우 반전", command=func_flips)
imageMenu.add_command(label="회전", command=func_rotate)

# 이미지 처리(2) 메뉴 (필터/효과)
imageMenu2 = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="이미지 처리(2)", menu=imageMenu2)
imageMenu2.add_command(label="확대", command=func_zoomin)
imageMenu2.add_command(label="축소", command=func_zoomout)
imageMenu2.add_separator()
imageMenu2.add_command(label="흐리게", command=func_blur)
imageMenu2.add_command(label="선명하게", command=func_sharpen)
imageMenu2.add_command(label="엠보싱", command=func_emboss)
imageMenu2.add_command(label="경계선", command=func_contour)
imageMenu2.add_command(label="세부 묘사", command=func_detail) 
imageMenu2.add_command(label="색상 강조", command=func_color)

# --- 메인 이벤트 루프 시작 ---
window.mainloop()