import os
from PIL import Image
from pillow_heif import register_heif_opener

# 註冊 HEIF 解碼器
register_heif_opener()

def convert_heic_to_jpg():
    # 取得程式執行時所在的資料夾路徑
    folder_path = os.getcwd()
    
    print(f"正在處理資料夾: {folder_path}")
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(folder_path, filename)
            jpg_path = os.path.join(folder_path, filename.replace(".heic", ".jpg").replace(".HEIC", ".jpg"))
            
            try:
                image = Image.open(heic_path)
                image.save(jpg_path, "JPEG", quality=95)
                print(f"成功轉換: {filename} -> {os.path.basename(jpg_path)}")
            except Exception as e:
                print(f"轉換 {filename} 時出錯: {e}")

    print("\n所有轉換任務已完成！")
    input("按任意鍵退出...")

if __name__ == "__main__":
    convert_heic_to_jpg()