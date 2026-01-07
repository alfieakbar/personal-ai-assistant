# 🤖 Persistent AI Assistant (Gemini 2.5 Flash Edition)

Asisten AI cerdas yang dibangun dengan arsitektur modern, memiliki memori jangka panjang menggunakan database SQL, dan antarmuka chat yang interaktif. Proyek ini mendemonstrasikan integrasi LLM terbaru dengan sistem backend yang scalable.

## 🚀 Fitur Utama

- **Gemini 2.5 Flash Integration:** Menggunakan model AI terbaru dari Google untuk respon yang super cepat dan cerdas.
- **Persistent Memory:** Chat history tidak hilang meskipun server dimatikan, berkat integrasi **SQLite** dan **SQLAlchemy**.
- **Session Management:** Mendukung banyak sesi percakapan yang berbeda menggunakan `session_id`.
- **Decoupled Architecture:** Backend (FastAPI) dan Frontend (Streamlit) berjalan terpisah, memungkinkan pengembangan UI yang fleksibel.
- **Async Logic:** Implementasi asinkronus untuk penanganan request yang efisien.

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **AI Framework:** LangChain & Google Generative AI SDK
- **Backend:** FastAPI & Uvicorn
- **Frontend:** Streamlit
- **Database:** SQLite (SQLAlchemy)
- **Environment:** WSL2 (Ubuntu)

## 📋 Prasyarat

- Python 3.10 ke atas terinstall di WSL.
- Google AI Studio API Key (Gratis).

## 🔧 Cara Instalasi

1. **Clone Repository**
   ```bash
   git clone [https://github.com/alfieakbar/personal-ai-assistant.git](https://github.com/alfieakbar/personal-ai-assistant.git)
   cd personal-ai-assistant
   ```
2. **Setup Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Konfigurasi .env Buat file .env di root folder dan masukkan API Key kamu**
   ```Plaintext
   GOOGLE_API_KEY=your_api_key_here
   ```

## 🏃 Cara Menjalankan

1. **Jalankan Backend (Terminal 1):**
   ```bash
   uvicorn app.main:app --reload
   ```
2. **Jalankan Frontend (Terminal 2):**
   ```bash
   streamlit run app_ui.py
   ```
3. **Buka browser di:**
   ```Plaintext
   http://localhost:8501
   ```
