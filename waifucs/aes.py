
from typing import Iterator
import torch
from aesthetic_predictor_v2_5 import convert_v2_5_from_siglip
from waifuc.action import BaseAction
from waifuc.model import ImageItem
from typing import Iterator
import os
model, preprocessor = convert_v2_5_from_siglip(
    trust_remote_code=True,
)
gpu_device = torch.device("cuda")

model = model.to(gpu_device)

class FilterAesAction(BaseAction):
    def iter(self, item: ImageItem) -> Iterator[ImageItem]:
        pixel_values = (
            preprocessor(images=item.image.convert("RGB"), return_tensors="pt")
            .pixel_values.to(gpu_device)
        )
         # 预测美学分数
        with torch.inference_mode():
            score = model(pixel_values).logits.squeeze().float().cpu().numpy()
        if score < 4.5:
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
                new_filename = f"{basename}_aes_{score:.2f}{extension}"

            # 保存新的文件名到 item.meta['filename']
                item.meta['filename'] = new_filename
                yield item
            
            else:
                item.meta['score'] = score  # set meta info
                item.meta['filename'] = f'aes_{score:.2f}.png'  # set filename
                yield item

    def reset(self):
        pass