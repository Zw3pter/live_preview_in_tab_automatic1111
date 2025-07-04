Live Image Preview for AUTOMATIC1111

This is a simple and yet very effective way to have the latest image created placed on a second monitor in fullscreen — instead of manually pressing and enlarging images in AUTOMATIC1111.

This tool allows you to serve and live-preview the most recent image generated by AUTOMATIC1111's Stable Diffusion WebUI, directly in your browser.

It works by:

    Serving the outputs/txt2img-images directory (and its dated subfolders)

    Updating the preview in real-time every 0.25 seconds to always show the newest image

🔧 Files

    silent_server.py
    A lightweight HTTP server (Python-based) that silently serves files from the current directory on port 7861. Only image requests are logged.

    live_preview.html
    An auto-updating web page that fetches and displays the latest image from the newest date-named subfolder (e.g., 2025-06-05) inside the output directory.

    silent_livepreview.bat
    A batch script that launches the silent_server.py and opens the live preview in your browser automatically.

📁 Setup Instructions

    Place the files in your Stable Diffusion WebUI output folder:
    Example:

    stable-diffusion-webui/
    └── outputs/
        └── txt2img-images/
            ├── 2025-06-05/
            │   └── your_generated_image.png
            ├── silent_server.py
            ├── live_preview.html
            └── silent_livepreview.bat

    Run the preview:

        Double-click silent_livepreview.bat

        This will start the server and open the browser at http://localhost:7861/live_preview.html

    Generate images as usual in AUTOMATIC1111.

        The preview will auto-update with the newest image from the most recent subfolder.

💡 Notes

    Only .png, .jpg, .jpeg, and .webp files are supported.

    Subfolders are expected to be named using the date format YYYY-MM-DD, which is the default behavior of AUTOMATIC1111.

    This does not move or copy any files — it reads directly from the existing output folder.

✅ Requirements

    Python 3.x

    A web browser (Chrome, Firefox, etc.)

    Tested on Windows using Git Bash / CMD / PowerShell
