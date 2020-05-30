from get_all_post_paths import get_all_post_paths


def image_to_background(post_files):
    for post in post_files:
        output_lines = None
        with open(post, 'r') as f:
            lines = f.readlines()
            try:
                image_line = next(line for line in lines if line.startswith('image:'))
                image_line_index = lines.index(image_line)
                words = image_line.split()
                image_path = words[-1]
                background_line = f'background: {image_path}\n'
                lines.insert(image_line_index + 1, background_line)
                output_lines = lines
            except:
                continue            
        with open(post, 'w') as f:
            f.writelines(output_lines)

def main():
    md_files = get_all_post_paths()
    image_to_background(md_files)


if __name__ == '__main__':
    main()


