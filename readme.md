# HEIC to JPG Converter (Streamlit App) 📸

一個基於 Python 和 Streamlit 構建的輕量級網頁工具，可將 Apple 的 HEIC 格式圖片批量轉換為相容性更高的 JPG 格式，並支援壓縮打包下載。

## ✨ 特色功能

- **批量轉換**：支援同時上傳多張 `.heic` 或 `.heif` 檔案。
- **EXIF / 圖片相容性修復**：透過 `pillow-heif` 精準解碼，完美轉換為標準 JPG。
- **一鍵打包**：轉換完成後，可直接將所有 JPG 檔案打包成一個 `.zip` 壓縮檔下載。
- **直觀網頁介面**：基於 Streamlit 介面開發，無須指令操作，拖放即可完成。

---

## 🚀 本地執行教學

### 1. 複製儲存庫 (Clone)

首先，將此專案複製到你的本地電腦：

```bash
git clone [https://github.com/JAAAE/heic_to_jpg.git](https://github.com/JAAAE/heic_to_jpg.git)
cd heic_to_jpg
