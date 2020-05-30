import os

def get_posts_path():
    FILE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
    POSTS_DIRECTORY = '_posts'
    POSTS_PATH = os.path.join(FILE_DIRECTORY, '../', POSTS_DIRECTORY)
    return POSTS_PATH

def get_md_files(path):
    md_files = []

    for root, directories, files in os.walk(path):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def image_to_files(post_files):
    for post in post_files:
        with open(post, 'rw') as f:
            lines = f.readlines()
            try:
                image_line = next(line for line in lines if line.startswth('image:'))
                image_line_index = lines.index(image_line)
                words = image_line.split()
                image_path = words[-1]
                background_line = f'background: {image_path}'
                lines.insert(image_line_index + 1, background_line)
                f.writelines(lines)
            except:
                pass            


def main():
    posts_path = get_posts_path()
    md_files = get_md_files(posts_path)
    image_to_background(md_files)


if __name__ == '__main__':
    main()


