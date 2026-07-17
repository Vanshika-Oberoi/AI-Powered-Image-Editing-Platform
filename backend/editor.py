import shutil
import os
from datetime import datetime

from config import EDITED_FOLDER

os.makedirs(EDITED_FOLDER, exist_ok=True)


def edit_image(original_path, prompt):

    filename = os.path.basename(original_path)

    name, ext = os.path.splitext(filename)

    new_filename = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"

    new_path = os.path.join(EDITED_FOLDER, new_filename)

    # Placeholder: copy original image
    shutil.copy(original_path, new_path)

    return new_path