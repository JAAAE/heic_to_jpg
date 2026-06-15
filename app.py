import io
import zipfile
import streamlit as st
from PIL import Image
from pillow_heif import register_heif_opener

# 註冊 HEIF 解碼器
register_heif_opener()

# 設定網頁標題與圖示
st.set_page_config(page_title="HEIC 轉 JPG 工具", page_icon="📸", layout="centered")

st.title("📸 HEIC 線上轉 JPG 工具")
st.write("上傳你的 HEIC 照片，一鍵轉換為 JPG 格式並下載！")


# 檔案上傳組件（支援多檔案上傳）
uploaded_files = st.file_uploader(
    "請選擇要轉換的 HEIC 檔案", 
    type=["heic"], 
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"已成功載入 {len(uploaded_files)} 個檔案！")
    
    # 用來存放轉換後的檔案資料，方便打包成 ZIP
    converted_images = []
    
    # 建立一個進度條
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # 開始轉換流程
    for index, uploaded_file in enumerate(uploaded_files):
        filename = uploaded_file.name
        status_text.text(f"正在轉換: {filename}...")
        
        try:
            # 讀取 HEIC 檔案
            image = Image.open(uploaded_file)
            
            # 將轉換後的 JPG 存入記憶體中 (BytesIO)
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='JPEG', quality=95)
            img_byte_arr = img_byte_arr.getvalue()
            
            # 產生新的 JPG 檔名
            # 使用 rsplit 確保只替換最後的副檔名，並處理大小寫
            new_filename = filename.lower().replace(".heic", ".jpg")
            
            # 存入列表
            converted_images.append((new_filename, img_byte_arr))
            
        except Exception as e:
            st.error(f"轉換 {filename} 時出錯: {e}")
            
        # 更新進度條
        progress_bar.progress((index + 1) / len(uploaded_files))
        
    status_text.text("✨ 所有檔案轉換完成！")
    
    
    # 下載邏輯
    if len(converted_images) == 1:
        # 如果只有一張照片，直接提供 JPG 下載
        single_name, single_data = converted_images[0]
        st.download_button(
            label="📥 下載 JPG 照片",
            data=single_data,
            file_name=single_name,
            mime="image/jpeg",
            type="primary"
        )
    elif len(converted_images) > 1:
        # 如果有多張照片，打包成 ZIP 檔下載
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED, False) as zip_file:
            for file_name, data in converted_images:
                zip_file.writestr(file_name, data)
                
        st.download_button(
            label="📥 打包下載所有 JPG (ZIP)",
            data=zip_buffer.getvalue(),
            file_name="converted_images.zip",
            mime="application/zip",
            type="primary"
        )