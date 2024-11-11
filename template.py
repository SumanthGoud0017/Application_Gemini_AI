import os

# Base project directory (modify this if your working directory is different)
base_dir = "Application_Gemini_AI"

# Define the project structure
folders = [
    "src/frontend/components",
    "src/frontend/pages",
    "src/frontend/services",
    "src/frontend/utils",
    "src/backend/controllers",
    "src/backend/models",
    "src/backend/routes",
    "src/backend/services",
    "src/backend/config",
    "src/ai/prompts",
    "src/ai/embeddings",
    "public"
]

# Create each directory if it doesn't already exist
for folder in folders:
    dir_path = os.path.join(base_dir, folder)
    os.makedirs(dir_path, exist_ok=True)
    print(f"Created: {dir_path}")

# Create placeholder files in the structure
files = {
    "src/frontend/App.js": "// Main application file\n",
    "src/backend/server.js": "// Main server file\n",
    "src/ai/GeminiService.js": "// Module to interact with Google Gemini\n",
    ".env": "# Environment variables\n",
    "docker-compose.yml": "# Docker setup for multi-container deployment\n",
    "package.json": "{\n  \"name\": \"application_gemini_ai\",\n  \"version\": \"1.0.0\",\n  \"dependencies\": {}\n}\n"
}

# Write placeholder content in each file
for file_path, content in files.items():
    full_path = os.path.join(base_dir, file_path)
    with open(full_path, "w") as f:
        f.write(content)
    print(f"Created file with placeholder content: {full_path}")
