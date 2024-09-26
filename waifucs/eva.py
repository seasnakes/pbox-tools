from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from tqdm import tqdm
import numpy as np
import pandas as pd
import timm
import torch
from huggingface_hub import hf_hub_download
from huggingface_hub.utils import HfHubHTTPError
from PIL import Image
from simple_parsing import field, parse_known_args
from timm.data import create_transform, resolve_data_config
from torch import Tensor, nn
from torch.nn import functional as F
from waifuc.action import ProcessAction
from waifuc.model import ImageItem


class CutHeadAction(ProcessAction):
    def process(self, item: ImageItem) -> ImageItem:
        area, type_, score = detect_heads(item.image)[0]
        return ImageItem(
            image=item.image.crop(area),
            meta=item.meta,
        )