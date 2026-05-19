import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Google Fonts link
old_link = r'<link href="https://fonts.googleapis.com/css2\?family=EB\+Garamond.*?rel="stylesheet">'
new_link = '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&family=Montserrat:wght@300;400;500&family=Cinzel:wght@400;500;600&display=swap" rel="stylesheet">'
content = re.sub(old_link, new_link, content, flags=re.DOTALL)

# Replace fonts
content = content.replace("'Playfair Display', serif", "'Cinzel', serif")
content = content.replace("'EB Garamond', serif", "'Cormorant Garamond', serif")
content = content.replace("'Josefin Sans', sans-serif", "'Montserrat', sans-serif")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done!")
