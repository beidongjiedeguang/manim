* 中文维基  
  https://manim.wiki/  
  https://manim.wiki/shaders/


* Update manim:

  * linux:
    ```bash
    ./update_manim.sh
    ```
    
  * windows:
    ```bash
    git checkout master setup_manimlib.py setup.cfg requirements.txt
    pip install -e .
    # windows poershell:
    rm setup.*
    rm requirements.txt
    rm .eggs -r -fo
    ```

* 早期版本的常见问题：  
  https://manim-kindergarten.github.io/manim_document_zh/problems/index.html
  
* 3B1B videos:  
  https://github.com/3b1b/videos


* 请运行示例在根目录下，即本README.md所在目录。
  
* GOA model
  <img src="data/pic/GOA.PNG" width = "900"/>