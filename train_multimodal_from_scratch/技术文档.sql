
--- modality 环境搭建(多模态, desktop的python开发环境)
conda create -n modality python=3.10.8
pip install torch-2.4.1+cu118-cp310-cp310-win_amd64.whl (F:/Packages, https://download.pytorch.org/whl/cu118)
pip install torchvision-0.19.1+cu118-cp310-cp310-win_amd64.whl (F:/Packages, https://download.pytorch.org/whl/cu118)
pip install transformers==4.56.2
pip install sentencepiece==0.2.1
pip install protobuf==6.32.0
pip install gradio==5.42.0
pip install pandas==2.3.2
pip install accelerate==1.10.0
pip install tensorboard==2.20.0


--- torch && torchvision 版本对应关系：
https://pytorch.org/get-started/previous-versions/

