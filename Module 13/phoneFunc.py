def slugify(title):
    slug = title.strip().replace(' ', '-')
    return slug

def wp_image(url, alt, caption):
    line_one = '<!-- wp:image {"align":"center","sizeSlug":"large"} -->'
    line_two = f'<figure class="wp-block-image aligncenter size-large"><img src="{url}" alt="{alt}"/><figcaption class="wp-element-caption">{caption}</figcaption></figure>'
    line_three = '<!-- /wp:image -->'
    code = f'{line_one}{line_two}{line_three}'
    return code


def wp_table(dicts):
    line_one = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    table_rows = ''
    for key, value in dicts.items():
        table_row = f'<tr><td>{key}</td><td>{value}</td></tr>'
        table_rows += table_row
    last_line = '</tbody></table></figure><!-- /wp:table -->'
    code = f'{line_one}{table_rows}{last_line}'
    return code