import os

# Define folder paths
folders = {
    "Japanese Study Logs": "Japanese/Logs",
    "IT Networking Study Logs": "IT_Networking/Logs",
    "Japanese Notes": "Japanese",
    "IT Networking Notes": "IT_Networking"
}

# Output file
toc_file = "TOC.md"

# Template for TOC.md
toc_content = "# 📖 Study Journal - Table of Contents\n\n"

for section, path in folders.items():
    if os.path.exists(path):
        toc_content += f"## {section}\n"
        for filename in sorted(os.listdir(path)):
            if filename.endswith(".md"):  # Only add markdown files
                file_path = os.path.join(path, filename)
                relative_path = f"{path}/{filename}"
                toc_content += f"- [{filename.replace('.md', '')}]({relative_path})\n"
        toc_content += "\n"

# Write to TOC.md
with open(toc_file, "w", encoding="utf-8") as f:
    f.write(toc_content)

print(f"✅ TOC.md updated successfully!")
