
git clone https://github.com/openai/CLIP
  # pip install taming-transformers
git clone https://github.com/CompVis/taming-transformers.git
#rm -Rf clipit
git clone https://github.com/mfrashad/clipit.git
pip install ftfy regex tqdm omegaconf pytorch-lightning
pip install kornia
pip install imageio-ffmpeg   
pip install einops
pip install torch-optimizer
pip install easydict
pip install braceexpand
pip install torch
pip install torchvision
pip install torch_optimizer
pip install perlin_numpy
pip install kornia
pip install imageio
pip install moviepy
pip install ftfy
pip install pytorch_lightning
pip install regex
pip install einops
pip install git+https://github.com/pvigier/perlin-numpy

  # ClipDraw deps
pip install svgwrite
pip install svgpathtools
pip install cssutils
pip install numba
pip install torch-tools
pip install visdom

pip install gradio

git clone https://github.com/BachiLi/diffvg
#%cd diffvg
# !ls
git submodule update --init --recursive
python setup.py install
#%cd ..
  
#mkdir -p steps
#mkdir -p models