import os
from bs4 import BeautifulSoup

# 优化后的导航栏代码（紧凑布局+统一样式）
NAVBAR_HTML = """
<div class="modern-navbar" style="
    background: linear-gradient(145deg, #4b6cb7 0%, #182848 100%);
    color: white;
    padding: 10px 20px;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    border-bottom: 1px solid rgba(255,255,255,0.1);
">
    <nav style="
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        align-items: center;
        gap: 20px;
    ">
        <div class="nav-brand" style="
            font-size: 1.3em;
            font-weight: bold;
            color: rgba(255,255,255,0.95);
            white-space: nowrap;
            flex-shrink: 0;
        ">
			<a href="/" style="color: inherit; text-decoration: none;">
            🏯 中华古籍库
			</a>
        </div>
        <div class="nav-links" style="
            display: flex;
            gap: 12px;
            align-items: center;
            flex-wrap: nowrap;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            flex-grow: 1;
        ">
            <!-- 统一链接样式模板 -->
            <a href="/佛藏/index.html" style="
                color: rgba(255,255,255,0.95);
                text-decoration: none;
                font-size: 0.95em;
                transition: all 0.2s ease;
                padding: 5px 10px;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                line-height: 1.2;
                white-space: nowrap;
                flex-shrink: 0;
            ">
                <span style="font-size:1.1em">📜</span>佛藏
            </a>
            <a href="/儒藏/index.html" style="
                color: rgba(255,255,255,0.95);
                text-decoration: none;
                font-size: 0.95em;
                transition: all 0.2s ease;
                padding: 5px 10px;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                line-height: 1.2;
                white-space: nowrap;
                flex-shrink: 0;
            ">
                <span style="font-size:1.1em">📚</span>儒藏
            </a>
            <a href="/医藏/index.html" style="
                color: rgba(255,255,255,0.95);
                text-decoration: none;
                font-size: 0.95em;
                transition: all 0.2s ease;
                padding: 5px 10px;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                line-height: 1.2;
                white-space: nowrap;
                flex-shrink: 0;
            ">
                <span style="font-size:1.1em">🌿</span>医藏
            </a>
            <a href="/史藏/index.html" style="
                color: rgba(255,255,255,0.95);
                text-decoration: none;
                font-size: 0.95em;
                transition: all 0.2s ease;
                padding: 5px 10px;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                line-height: 1.2;
                white-space: nowrap;
                flex-shrink: 0;
            ">
                <span style="font-size:1.1em">📖</span>史藏
            </a>
            <a href="/子藏/index.html" style="
                color: rgba(255,255,255,0.95);
                text-decoration: none;
                font-size: 0.95em;
                transition: all 0.2s ease;
                padding: 5px 10px;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                line-height: 1.2;
                white-space: nowrap;
                flex-shrink: 0;
            ">
                <span style="font-size:1.1em">🧠</span>子藏
            </a>
            <a href="/易藏/index.html" style="
                color: rgba(255,255,255,0.95);
                text-decoration: none;
                font-size: 0.95em;
                transition: all 0.2s ease;
                padding: 5px 10px;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                line-height: 1.2;
                white-space: nowrap;
                flex-shrink: 0;
            ">
                <span style="font-size:1.1em">☯</span>易藏
            </a>
            <a href="/艺藏/index.html" style="
                color: rgba(255,255,255,0.95);
                text-decoration: none;
                font-size: 0.95em;
                transition: all 0.2s ease;
                padding: 5px 10px;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                line-height: 1.2;
                white-space: nowrap;
                flex-shrink: 0;
            ">
                <span style="font-size:1.1em">🎨</span>艺藏
            </a>
            <a href="/诗藏/index.html" style="
                color: rgba(255,255,255,0.95);
                text-decoration: none;
                font-size: 0.95em;
                transition: all 0.2s ease;
                padding: 5px 10px;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                line-height: 1.2;
                white-space: nowrap;
                flex-shrink: 0;
            ">
                <span style="font-size:1.1em">🌸</span>诗藏
            </a>
            <a href="/道藏/index.html" style="
                color: rgba(255,255,255,0.95);
                text-decoration: none;
                font-size: 0.95em;
                transition: all 0.2s ease;
                padding: 5px 10px;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                line-height: 1.2;
                white-space: nowrap;
                flex-shrink: 0;
            ">
                <span style="font-size:1.1em">🌀</span>道藏
            </a>
            <a href="/集藏/index.html" style="
                color: rgba(255,255,255,0.95);
                text-decoration: none;
                font-size: 0.95em;
                transition: all 0.2s ease;
                padding: 5px 10px;
                border-radius: 4px;
                display: flex;
                align-items: center;
                gap: 6px;
                line-height: 1.2;
                white-space: nowrap;
                flex-shrink: 0;
            ">
                <span style="font-size:1.1em">📚</span>集藏
            </a>
        </div>
    </nav>
</div>
"""

def process_html_files(root_folder):
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                add_navbar_to_html(file_path)

def add_navbar_to_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    soup = BeautifulSoup(content, "html.parser")
    
    # 移除旧导航栏
    old_nav = soup.find("div", class_="modern-navbar")
    if old_nav:
        old_nav.decompose()

    # 更新body样式
    body_style = """
    body {
        padding-top: 60px !important;
        font-family: 'Georgia', serif;
        font-size: 18px;
        line-height: 1.8;
        color: #333;
        margin: 2em auto;
        max-width: 800px;
        padding: 0 20px;
        text-align: justify;
    }
    """
    
    style_tag = soup.find("style")
    if style_tag:
        style_tag.string = style_tag.string.replace("body {", body_style)
    else:
        new_style = soup.new_tag("style")
        new_style.string = body_style
        soup.head.append(new_style)

    # 插入新导航栏
    body = soup.find("body")
    if body:
        navbar = BeautifulSoup(NAVBAR_HTML, "html.parser")
        body.insert(0, navbar)

    # 保存修改
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(soup.prettify()))

    print(f"Optimized navigation bar added to {file_path}")

if __name__ == "__main__":
    current_folder = os.getcwd()
    process_html_files(current_folder)
    print("所有HTML文件处理完成！")