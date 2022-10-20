import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])
        
# Example
if __name__ == '__main__':
    install('ftfy regex tqdm omegaconf pytorch-lightning')     
       
    install('kornia')
    install('imageio-ffmpeg')   
    install('einops')
    install('torch-optimizer')
    install('easydict')
    install('braceexpand')
    install('git+https://github.com/pvigier/perlin-numpy')

  # ClipDraw deps
    install('svgwrite')
    install('svgpathtools')
    install('cssutils')
    install('numba')
    install('torch-tools')
    install('visdom')

    install('gradio')

#git clone https://github.com/BachiLi/diffvg
#%cd diffvg
# !ls
#git submodule update --init --recursive
#python setup.py install