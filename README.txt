=======================================
UYDU GÖRÜNTÜLERİ ARASINDA FARK TESPİTİ
=======================================

📌 Proje Hakkında:
------------------
Bu proje, iki farklı tarihli uydu görüntüsü arasındaki farkları tespit etmek amacıyla geliştirilmiştir. Görsel işleme teknikleri kullanılarak doğal afetler, yapılaşma, arazi değişiklikleri gibi durumların otomatik olarak fark edilmesi hedeflenmiştir.

🧰 Kullanılan Teknolojiler:
---------------------------
- Python
- OpenCV
- FastAPI (Backend API servisi)
- Streamlit (Kullanıcı arayüzü)
- Docker (Container altyapısı)
- Skimage (Histogram eşleme için)
- NumPy, cv2

🔍 Özellikler:
--------------
- İki farklı görüntüyü karşılaştırarak yapısal farkları tespit eder.
- Histogram eşleme ile renk düzeltmesi yapılır.
- Blurlama, kenar bulma ve eşikleme adımları uygulanır.
- Binary değişim haritası üretir.
- Streamlit arayüzü ile görselleştirme sunar.
- FastAPI ile arka planda işleme yapılır.

🚀 Kurulum:
-----------
1. Docker'ın sisteminizde kurulu olduğundan emin olun.

2. DockerHub üzerinden projeyi çekin:
   docker pull sematemur/findingchangemap:latest

3. Konteyneri başlatın:
   docker run -p 8501:8501 -p 8000:8000 sematemur/findingchangemap:latest

4. Uygulamayı tarayıcınızda açın:
   http://localhost:8501 


📧 İletişim:
------------
Geliştirici: Sema Temur  
E-posta: sema_temur_@hotmail.com
Teknik dökümantasyon Proje.pdf adlı dosyadır.

