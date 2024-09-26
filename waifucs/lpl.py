
from typing import Iterator
from waifuc.action import BaseAction
from waifuc.model import ImageItem
from imgutils.metrics import laplacian_score
import os
from typing import Iterator

class FilterBlurAction(BaseAction):
    def iter(self, item: ImageItem) -> Iterator[ImageItem]:
        image = item.image
        score = laplacian_score(image)
        if score < 70:
            pass
        else:
            item.meta['score'] = score  # set meta info
            # 假设原始文件名可能存在于 item.meta['filename']
            original_filename = item.meta.get('filename') # 使用get方法，如果'filename'不存在，将返回None
            # 检查文件名是否存在
            if original_filename:
            # 使用 os.path.splitext 分割原始文件名和扩展名
                basename, extension = os.path.splitext(original_filename)

            # 将新的分数添加到文件名中，并重新添加扩展名
                new_filename = f"{basename}_blur_{score:.2f}{extension}"

            # 保存新的文件名到 item.meta['filename']
                item.meta['filename'] = new_filename
                yield item
            
            else:
                item.meta['score'] = score  # set meta info
                item.meta['filename'] = f'lpl_{score:.2f}.png'  # set filename
                yield item

    def reset(self):
        pass