import os
from waifuc.export import SaveExporter
from waifuc.source import LocalSource
from aes import FilterAesAction
from lpl import FilterBlurAction
from waifuc.action import FilterSimilarAction

base_dir = '/home/pbox/snake/data/video/gf/song/qpy'
export_base_dir = '/home/pbox/snake/data/image/gf/'

for i in range(1, 70):  
    episode_dir = os.path.join(base_dir, f'{str(i).zfill(2)}_frames')  # Use string formatting to fill leading zeros
    export_dir = os.path.join(export_base_dir, f'qpy{str(i).zfill(2)}')

    source = LocalSource(episode_dir)
    source.attach(
        FilterBlurAction(),
        FilterAesAction(),
        FilterSimilarAction(threshold=0.55)
    ).export(SaveExporter(export_dir))
