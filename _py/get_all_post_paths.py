import os


def get_posts_path():
    FILE_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
    POSTS_DIRECTORY = '_posts'
    POSTS_PATH = os.path.join(FILE_DIRECTORY, '../', POSTS_DIRECTORY)
    return POSTS_PATH

def get_md_files(path):
    md_files = []

    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def get_all_post_paths():
    posts_path = get_posts_path()
    md_files = get_md_files(posts_path)
    return md_files
