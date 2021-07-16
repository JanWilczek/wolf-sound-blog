function category_toggle(button) {
    const categories_radio_buttons = document.querySelectorAll('input[name="article-categories"]');
    categories_previews = document.getElementsByName('preview-block');
    for (preview of categories_previews) {
      if (preview.classList.contains('d-block'))
      {
        preview.classList.remove('d-block');
        preview.classList.add('d-none');
      }

      if (preview.id.includes(button.id))
      {
        if (preview.classList.contains('d-none'))
        {
          preview.classList.remove('d-none');
          preview.classList.add('d-block');
        }
      }
    }
  }
  