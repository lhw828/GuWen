import os

def rename_page1_files_recursively(root_dir='.'):
    # 遍历当前文件夹及其所有子目录
    for dirpath, _, filenames in os.walk(root_dir):
        for file_name in filenames:
            # 检查文件名是否以 _page1.html 结尾
            if file_name.endswith('_page1.html'):
                print(f"正在处理文件: {os.path.join(dirpath, file_name)}")

                # 构造新的文件名
                old_file_path = os.path.join(dirpath, file_name)
                new_file_name = file_name.rsplit('_', 1)[0] + '.html'
                new_file_path = os.path.join(dirpath, new_file_name)

                try:
                    # 重命名文件
                    os.rename(old_file_path, new_file_path)
                    print(f"已重命名: {old_file_path} -> {new_file_path}")
                except Exception as e:
                    print(f"重命名失败: {old_file_path} -> {new_file_path}, 错误: {e}")

if __name__ == "__main__":
    rename_page1_files_recursively()