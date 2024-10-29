import json

# Load skills from JSON
with open('skills.json', 'r') as f:
    skills = json.load(f)

# Generate Markdown for skills
markdown_lines = ["## Most Used Skills\n"]
for skill, percentage in skills.items():
    # Creating shield badges
    markdown_lines.append(f"![{skill}](https://img.shields.io/badge/{skill}-{percentage}%-blue?style=flat-square)")

# Print generated lines for debugging
print("\n".join(markdown_lines))  # Print to console to verify the output

# Save Markdown to README.md
with open('README.md', 'r') as f:
    readme_content = f.readlines()

# Replace the old skills section or append the new one
for i, line in enumerate(readme_content):
    if line.startswith("## Most Used Skills"):
        readme_content[i:i + len(markdown_lines) + 1] = markdown_lines + ["\n"]
        break
else:
    # If not found, append to the end
    readme_content.append("\n" + "\n".join(markdown_lines) + "\n")

with open('README.md', 'w') as f:
    f.writelines(readme_content)

print("README.md updated with Most Used Skills.")
