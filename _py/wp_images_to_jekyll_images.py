from get_all_post_paths import get_all_post_paths
from html.parser import HTMLParser


class WPImage:
    def __init__(self, start_position):
        self.start_position = start_position
        self.end_position = None
        self.link = None
        self.alt = None
        self.caption = None


class WPImagesParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.parsing_image = False
        self.parsing_caption = False
        self.current_image = None
        self.wp_images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == 'div':
            if attrs['class'].startswith('wp-block-image'):
                self.parsing_image = True
                start_position = self.getpos()
                self.current_image = WPImage(start_position)
        
        if tag == 'img' and self.parsing_image:
            if self.current_image.link is None:
                self.current_image.link = attrs['src'].strip()
                self.current_image.alt = attrs['alt'].strip()

        if tag == 'figcaption' and self.parsing_image:
            self.parsing_caption = True
        
    def handle_data(self, data):
        if self.parsing_caption:
            self.current_image.caption = data.strip()
            self.parsing_caption = False

    def handle_endtag(self, tag):
        if tag == 'div' and self.parsing_image:
            self.parsing_image = False
            self.current_image.end_position = self.getpos()
            self.wp_images.append(self.current_image)
            self.current_image = None
            assert self.wp_images[0] is not None

def get_content_and_images(filename):
    """Returns lines, parsed_images"""
    parser = WPImagesParser()
    with open(filename, 'r') as f:
        content = f.read()
        parser.feed(content)
    with open(filename, 'r') as f:
        lines = f.readlines()
        return lines, parser.wp_images

def wp_to_jekyll_images(file_contents, wp_images):
    for i in range(len(wp_images) - 1, -1, -1):
        image = wp_images[i]
        tag_start_line = image.start_position[0]
        tag_end_line = image.end_position[0]
        new_image_entry = f'![{image.alt}]({image.link})\n'
        if image.caption is not None:
            new_image_entry += f'*{image.caption}*\n'
        file_contents = file_contents[:tag_start_line-1] + [new_image_entry] + file_contents[tag_end_line:]
    return file_contents

def wp_images_to_jekyll_images(post_paths):
    for file in post_paths:
        content, wp_images = get_content_and_images(file)
        updated_content = wp_to_jekyll_images(content, wp_images)
        with open(file, "w") as f:
            f.writelines(updated_content)

def main():
    post_paths = get_all_post_paths()
    wp_images_to_jekyll_images(post_paths)


if __name__ == "__main__":
    main()
