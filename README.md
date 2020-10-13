# AI_3_project

За основу пакмана ми взяли [берклівський темплейт](https://inst.eecs.berkeley.edu/~cs188/fa18/project1.html)<br/>
Оскільки цей темплейт підходить як раз під ті вимоги, які від нас потребуються.

    
Файл на редакції : 
>search.py

Були реалізовані алгоритми <br/> DFS 

![dfs](https://i.ibb.co/DVvLP6G/pycharm64-o1t-Pz0di-TE.png)

BFS

![bfs](https://i.ibb.co/1R2xR26/image-2020-10-05-161923.png)

A*

![A*](https://i.ibb.co/vBGm8M6/image-2020-10-13-133901.png)
![A*](https://i.ibb.co/6bJd2cM/pycharm64-QK6-KYFhetr.png)

Жадібний алгоритм

![greedy](https://i.ibb.co/N9C4LDC/pycharm64-u-S073p-C7-G4.png)

У зв'язку з показаннями затрат пам'яті імпортували memory profiler.<br/><br/>
Потрібен встановленний [pip](https://bootstrap.pypa.io/get-pip.py). Зберегти у форматі .py та запустити. [*Ось повний гайд на встановлення pip*](https://pip.pypa.io/en/latest/installing/)<br/>
Завантаження memory profiler : 
> pip install -U memory_profiler

[*Ось повний гайд на встановлення memory_profiler*](https://pypi.org/project/memory-profiler/)

Для запуску режиму DFS : 

> py pacman.py -l mediumMaze -p SearchAgent -a fn=dfs

Для запуску режиму BFS : 

> py pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

Для запуску режиму A* : 

> py pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

Для запуску режиму жадібного алгоритму :

> py pacman.py -l mediumMaze -p SearchAgent -a fn=greedy,heuristic=manhattanHeuristic


