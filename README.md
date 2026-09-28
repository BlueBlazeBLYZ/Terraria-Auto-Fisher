---

### Step 1: Create a New Repository on GitHub
1. Go to [GitHub.com](https://github.com) and log in.
2. Click the **`+`** icon in the top right $\rightarrow$ **New repository**.
3. Name it: `Terraria-Auto-Fisher` (or any name you like).
4. Leave it **Public** (or Private).
5. **Do not** check "Add a README file" (we will create one locally).
6. Click **Create repository**.
7. Copy your repository link (e.g., `https://github.com/YourUsername/Terraria-Auto-Fisher.git`).

---

### Step 2: Prepare Your Files Locally
Put all your files into a single folder on your computer:

#### 1. `auto_fishing.py`
*(The script provided earlier)*

#### 2. Create `requirements.txt`
Create a file named `requirements.txt` and paste this:
```text
opencv-python
pyautogui
keyboard
numpy
pillow
pyinstaller
```

#### 3. Create `.gitignore`
Create a file named `.gitignore` to prevent uploading compiled `.exe` files and build caches:
```gitignore
__pycache__/
*.pyc
build/
dist/
*.spec
.vscode/
.idea/
venv/
```

#### 4. Create `README.md`
Create a file named `README.md` to make your GitHub page look professional:
```markdown
# Terraria Auto Fishing Bot

A lightweight, computer-vision-based auto-fishing macro for Terraria using OpenCV and PyAutoGUI. 

Instead of simple pixel checks that break due to water animation, it dynamically tracks motion/splashes within a user-defined bounding box and automatically clicks to reel in and recast.

## Features
- **Custom Bounding Box**: Select any area on the screen for the bobber.
- **Motion Difference Detection**: Detects dips/splashes reliably.
- **Auto-Loop**: Automatically recasts and repeats indefinitely.
- **Safety Timeout**: Recasts after 25 seconds if no bite occurs.

## Hotkeys
| Key | Action |
|---|---|
| `F6` | Set Top-Left corner of detection box |
| `F7` | Set Bottom-Right corner of detection box |
| `F8` | Start the fishing loop |
| `F9` | Stop / Pause |
| `ESC` | Exit program completely |

## Setup & Running
1. Clone the repository:
   ```bash
   git clone https://github.com/<YOUR-USERNAME>/Terraria-Auto-Fisher.git
   cd Terraria-Auto-Fisher
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python auto_fishing.py
   ```

## Compiling to `.exe`
To build a standalone executable:
```bash
pyinstaller --onefile --admin auto_fishing.py
```
The compiled file will be located inside the `dist/` directory.
```

---

### Step 3: Push to GitHub (Using Terminal/Command Prompt)

Open your terminal or command prompt inside your project folder and run:

```bash
git init
git add .
git commit -m "Initial commit: Terraria Auto Fishing Bot"
git branch -M main
git remote add origin https://github.com/<YOUR-USERNAME>/Terraria-Auto-Fisher.git
git push -u origin main
```
*(Replace `<YOUR-USERNAME>` with your actual GitHub username).*

---

### Alternative (No Git / Web Browser Method):
If you don't use Git in the terminal:
1. When creating the repo on GitHub, check **"Add a README file"**.
2. Click **"Add file"** $\rightarrow$ **"Upload files"**.
3. Drag and drop `auto_fishing.py`, `requirements.txt`, and `.gitignore` directly into your browser.
4. Click **Commit changes**.
