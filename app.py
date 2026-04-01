import streamlit as st
import os

# --- 1. إعدادات الصفحة ---
st.set_page_config(
    page_title="منصة المحاضرات | مصطفى محمود",
    page_icon="📚",
    layout="wide"
)

# --- 2. ربط الفرونت إند (مع تصحيح اللغة العربية) ---
def local_css(file_name):
    if os.path.exists(file_name):
        # التعديل هنا: أضفنا encoding="utf-8" عشان يقرأ العربي صح
        with open(file_name, encoding="utf-8") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.sidebar.warning(f"ملف {file_name} غير موجود.")

# استدعاء التنسيق
local_css("style.css")

# --- 3. الباك إند (مجلد التخزين) ---
UPLOAD_DIR = "lectures_db"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# --- 4. واجهة المستخدم (Front-end) ---
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.title("🎓 منصة المحاضرات الذكية")
st.subheader("تم التطوير بواسطة: مصطفى محمود السيد")
st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📤 رفع محاضرة جديدة")
    file = st.file_uploader("اسحب الملف هنا", type=['pdf', 'pptx', 'docx'])
    if file and st.button("🚀 حفظ في المكتبة"):
        path = os.path.join(UPLOAD_DIR, file.name)
        with open(path, "wb") as f:
            f.write(file.getbuffer())
        st.success(f"✅ تم حفظ {file.name} بنجاح!")
        st.balloons()

with col2:
    st.markdown("### 📊 حالة المكتبة")
    files = os.listdir(UPLOAD_DIR)
    st.metric(label="عدد الملفات", value=len(files))

st.divider()

# --- 5. عرض الملفات ---
st.header("📖 المحاضرات المتوفرة")
if files:
    for f_name in files:
        with st.expander(f"📄 {f_name}"):
            with open(os.path.join(UPLOAD_DIR, f_name), "rb") as f:
                st.download_button("تحميل", f, file_name=f_name, key=f_name)
else:
    st.info("المكتبة فارغة.")

# --- 6. التذييل ---
st.markdown('<div class="footer"><hr>حقوق الطبع محفوظة © 2026 | م. مصطفى محمود السيد</div>', unsafe_allow_html=True)