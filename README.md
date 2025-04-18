
# 🎬 Videreelic — Faceless Short Video Automation  

Create high-quality short videos using powerful AI tools. Generate scripts, visuals, subtitles, voiceovers, and upload — all from a local environment with internet access.

---

## 🧱 Tech Stack

This section lists the full stack of technologies and APIs used to **build and run Videreelic locally**.

### 🔹 A. Core Language & Framework
- 🐍 **Python** — Core engine and automation logic.
- ⚙️ **fle-framework v1.x** — Lightweight custom Python framework powering the automation pipeline.

### 🎥 B. Multimedia Framework
- 🛠 **FFmpeg** — Audio/video decoding, encoding, and rendering.

### 🌐 C. AI & API Integrations *(Requires Internet)*

#### ✍️ 1. Script Writers
- 📝 **DeepSeek**
- 🤖 **OpenAI GPT**
- 🧠 **Claude (Anthropic)**

#### 🎨 2. Visual Generators
- 🖼 **Stable Diffusion** — Text-to-image generation.
- 📸 **Pexels API** — Stock media content.
- 🎬 **Runway ML** — AI-powered video generation.
- 🎨 **Leonardo AI** — Stylized image generation.
- 🏞 **Tensor Art** — Aesthetic art generation.

#### 🎤 3. Subtitles (Transcription)
- 🔊 **Whisper AI** — Audio-to-text transcription.

#### 🗣 4. Voice Generation
- 🎙 **ElevenLabs API** — Text-to-speech voice synthesis.
- 📍 **Local TTS** — Offline voice generation (optional).

#### 📡 5. Auto Upload (Optional)
- 🎥 **YouTube Data API**
- 🎵 **TikTok Upload API**
- 📸 **Instagram Graph API**
- 📢 **Facebook Video API**

---

## 📦 Final Product & Deployment

Once built, **Videreelic** runs entirely on **localhost**. It does **not** require a server or cloud backend. However, a **stable internet connection is required** to enable the following features:

### ✅ During Video Creation
- Connects to external AI APIs for:
  - Script generation
  - Image and video assets
  - Voice and subtitles

### ⏰ For Scheduled Uploads
- Videreelic runs a local **daemon process** for posting on a schedule.
- ⏲ Internet **must be available** at the time of posting.
- ❌ No internet at post time = No upload (no retry mechanism by default).

---

## 🚀 How to Use

1. 🔌 Ensure you are connected to the internet.
2. 🐍 Run Videreelic:
   ```bash
   python automate.py
   ```
3. 🧠 Follow prompts to generate content and assemble your short video.
4. 📤 (Optional) Enable auto-upload and set your posting schedule.

---

> 💡 **Videreelic** is a no-server, locally run tool designed for creators who want the power of AI in one streamlined, scriptable workflow.
