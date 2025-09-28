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
# snapshot_download(repo_id="Qwen/Qwen2.5-0.5B-Instruct", local_dir="../premodels/Qwen2.5-0.5B-Instruct")
# snapshot_download(repo_id="google/siglip-base-patch16-224", local_dir="../premodels/siglip-base-patch16-224")

# 数据
# snapshot_download(repo_id="liuhaotian/LLaVA-CC3M-Pretrain-595K", repo_type="dataset", local_dir="../predatasets/LLaVA-CC3M-Pretrain-595K")
snapshot_download(repo_id="LinkSoul/Chinese-LLaVA-Vision-Instructions", repo_type="dataset", local_dir="../predatasets/Chinese-LLaVA-Vision-Instructions")
