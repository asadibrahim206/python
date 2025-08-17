import os

current_dir = os.path.abspath('')
url = os.path.join(current_dir, "html/1992_World_Junior_Championships_in_Athletics_–_Men's_high_jump")
with open(url) as _f:
    url_data = _f.read()

