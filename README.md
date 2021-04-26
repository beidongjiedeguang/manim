* Update manim:

  * linux:
    ```bash
    ./update_manim.sh
    ```
    
  * windows:
    ```bash
    git checkout master setup.py setup.cfg requirements.txt
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



* GOA model
  ![image-20210426155714995](pic/GOA.png)