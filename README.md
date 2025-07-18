# pbox-tools

一个功能丰富的图像处理和机器学习工具集合，专注于计算机视觉任务和数据集管理。

## 📋 项目概述

pbox-tools 是一个多功能的工具箱，提供了图像分析、标签生成、美学评分、数据集管理等功能。项目主要分为两个核心模块：

- **fiftyone**: 计算机视觉数据集管理和分析
- **waifucs**: 图像处理和机器学习工具集合

## 🚀 功能特性

### FiftyOne 模块
- 数据集管理和可视化
- 零样本分类和相似性计算
- 中文CLIP模型集成

### WaifuCS 工具集
- **美学评分** (aes.py): 使用美学预测模型对图像进行质量评分
- **图像标签生成** (wdv3_timm.py): 基于WD v3模型的自动标签生成
- **CLIP分析** (clip.py): 中文CLIP模型的零样本分类
- **文件管理** (rename.py): 批量文件重命名工具
- **其他工具**: 包含多种图像处理和分析功能

## 📦 安装依赖

```bash
pip install torch torchvision
pip install fiftyone
pip install timm
pip install huggingface_hub
pip install simple_parsing
pip install pandas numpy
pip install Pillow
pip install tqdm
```

## 🔧 使用方法

### 1. 美学评分过滤

```python
from waifucs.aes import FilterAesAction

# 创建美学评分过滤器
filter_action = FilterAesAction()
# 处理图像并获取美学分数（阈值：4.5）
```

### 2. 图像标签生成

```python
from waifucs.wdv3_timm import LabelData

# 使用WD v3模型生成图像标签
# 支持多种模型：vit, swinv2, convnext, eva
```

### 3. 数据集管理

```python
import fiftyone as fo

# 加载数据集
dataset = fo.load_dataset("pboxGufeng")

# 计算相似性
import fiftyone.brain as fob
fob.compute_similarity(dataset, model="chinese-clip-vit-base-patch16")
```

## 🛠️ 工具详情

### 美学评分器 (aes.py)
- 基于aesthetic_predictor_v2_5模型
- 自动筛选高质量图像（评分 > 4.5）
- GPU加速推理

### WD v3标签器 (wdv3_timm.py)
- 支持多种预训练模型架构
- 自动图像预处理和标签生成
- 高精度的动漫/插画内容识别

### CLIP集成 (clip.py)
- 中文CLIP模型支持
- 零样本图像分类
- 多模态检索和相似性分析

## 📁 项目结构

```
pbox-tools/
├── README.md
├── fiftyone/
│   └── pboxgufeng.ipynb      # 数据集分析notebook
└── waifucs/
    ├── aes.py                # 美学评分过滤器
    ├── clip.py               # CLIP模型应用
    ├── wdv3_timm.py          # WD v3标签生成器
    ├── rename.py             # 文件重命名工具
    ├── eva.py                # EVA模型相关
    ├── lpl.py                # 其他处理工具
    ├── wdtg.py               # 标签生成工具
    ├── actiontest_1.py       # 测试脚本
    └── waifu.ipynb           # 主要分析notebook
```

## 🔗 相关资源

- [FiftyOne官方文档](https://docs.voxel51.com/)
- [Hugging Face Models](https://huggingface.co/)
- [TIMM模型库](https://github.com/rwightman/pytorch-image-models)

## 📄 许可证

本项目仅供学习和研究使用。

## 🤝 贡献

欢迎提交issues和pull requests来改进这个项目。

---

> 🎯 这个工具集合专为图像分析、内容筛选和数据集管理而设计，适合研究人员和开发者使用。
