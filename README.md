📄 README.md


# 🌈 DayDreamer - AI Image Generator

DayDreamer is a cute and responsive full-stack web application that lets you generate dream-like images using text prompts powered by AI.

✨ Built with:
- Frontend: React + Vite + Bootstrap
- Backend: Flask + HuggingFace Diffusers (Stable Diffusion)
- Hosted frontend: Netlify
- Backend runtime: Google Colab (with ngrok)

---

## 🌐 Live Frontend

Your frontend is deployed and available at:

🔗 [https://your-netlify-site.netlify.app](https://your-netlify-site.netlify.app)  
📝 Note: You must manually start the backend via Google Colab before using the app.

---

## ⚙️ Features

- Enter a creative prompt and generate an image using AI
- Suggested prompt buttons for inspiration
- Stylish UI with animations and pastel theme
- Option to save/download the generated image

---

## 📦 Project Structure

DayDreamer/
├── backend/
│ ├── app.py # Flask backend
│ ├── my_model/ # Locally saved model folder
│ └── .env # (Optional) Environment variables
│
├── DayDreamer/ # Frontend Vite React app
│ ├── public/
│ ├── src/
│ │ └── components/ # All components like ImageGenerator.jsx
│ ├── netlify.toml # Redirect & build config for Netlify
│ └── package.json
│
├── .venv/ # Python virtual environment (optional)
└── README.md # You're reading it!


---

## 🚀 How to Run Locally (Frontend)

1. Open terminal and navigate into frontend folder:
''bash
cd DayDreamer
Install dependencies:

''bash
npm install
Start local development server:

''bash
npm run dev
App will run on:

arduino
http://localhost:5173
🧠 How to Start Backend (via Google Colab)
Open this notebook in Google Colab:

👉 https://colab.research.google.com

Upload or open your notebook (e.g., Untitled1.ipynb).

Run all the cells in the notebook in order. This will:

Install dependencies (Flask, flask-cors, diffusers, etc.)

Load your pretrained model from /my_model

Start the Flask server on port 5000

Expose it via ngrok (e.g., https://abc123.ngrok-free.app)

Copy the public ngrok URL printed in the output.

Open your React frontend project:

Navigate to: src/components/ImageGenerator.jsx

Replace the backend API URL (in fetch) with the new ngrok URL:

Example:

js
const response = await fetch("https://abc123.ngrok-free.app/generate", {
Save the file and refresh your frontend browser (localhost:5173 or Netlify-deployed link).

✅ You’re now connected to your backend!

🧪 Sample Prompt Ideas
Try these for stunning results:

A mystical forest with glowing mushrooms

Cyberpunk neon street at night

Whimsical underwater tea party

Vintage robot reading newspaper

💾 Save Generated Images
After an image is generated, you’ll see a 💾 Save Image button to download it locally.

🎨 Styling
All components are styled with Bootstrap + custom CSS to create a soft pastel, dreamy look. Fonts used:

Quicksand (main font)

Great Vibes (titles)

Nunito/Poppins (inputs and buttons)

❗ Notes
You must run the Colab backend every time before using the app.

The ngrok link changes every session.

Make sure your ngrok link is whitelisted in CORS (handled by flask_cors).

📸 Screenshots
Home Page	Image Generator

👩‍💻 Developed By
💡 Era Gupta

📜 License
This project is open-source for educational purposes.

Feel free to contribute, fork, and create your own dream apps!

python
Let me know if you'd like this README as a downloadable file or if you'd like it ad

