# -*- coding: utf-8 -*-
# ModuleName: download
# Author: dongyihua543
# Time: 2025/9/28 9:14

from huggingface_hub import snapshot_download

"""
下载huggingface模型 + 数据

若不指定 cache_dir, Hugging Face Hub 会将下载的文件存储在默认缓存目录中, 通常是 `~/.cache/huggingface/hub`
pip install huggingface-hub==0.20.1
"""

# 模型
snapshot_download(repo_id="Qwen/Qwen2.5-0.5B-Instruct", local_dir="../premodels/Qwen2.5-0.5B-Instruct")

# 数据
