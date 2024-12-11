from PIL import Image, ImageSequence
import os

# 目標目錄
gif_frame_jpg_dir = "./gif-frame-jpg"
gif_frame_bw_jpg_dir = "./gif-frame-bw-jpg"
gif_dir = "./gif"

def ensure_dir(directory):
    """確保目錄存在，如果不存在則創建"""
    if not os.path.exists(directory):
        os.makedirs(directory)

def extract_frames_from_gif(gif_path, output_dir):
    """從GIF中提取每個frame並儲存為jpg"""
    ensure_dir(output_dir)
    with Image.open(gif_path) as gif:
        for i, frame in enumerate(ImageSequence.Iterator(gif)):
            frame_path = os.path.join(output_dir, f"frame_{i}.jpg")
            frame.convert("RGB").save(frame_path)

def resize_image(image_path, output_path, width, height):
    """調整圖片大小並轉為黑白"""
    img = Image.open(image_path).convert("1")  # 轉為單色圖片
    img = img.resize((width, height))  # 調整大小
    img.save(output_path)

def main():
    ensure_dir(gif_frame_jpg_dir)
    ensure_dir(gif_frame_bw_jpg_dir)

    # 假設只有一個GIF檔案需要處理
    gif_files = [f for f in os.listdir(gif_dir) if f.endswith(".gif")]
    if not gif_files:
        print("No GIF files found in the directory.")
        return

    gif_path = os.path.join(gif_dir, gif_files[0])
    print(f"Processing GIF: {gif_path}")

    # 提取GIF的frames
    extract_frames_from_gif(gif_path, gif_frame_jpg_dir)

    # 讀取並處理frames
    image_list = os.listdir(gif_frame_jpg_dir)
    for image_name in image_list:
        input_path = os.path.join(gif_frame_jpg_dir, image_name)
        output_path = os.path.join(gif_frame_bw_jpg_dir, image_name)
        resize_image(input_path, output_path, 128, 64)

if __name__ == "__main__":
    main()
