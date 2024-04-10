Code cleanup.



info[x] -> description of symmetry
point[x] -> returns the cut line for the edges of the tile based on the specific info (last param of info is the shape type)
groups{….} -> dictionary describing all the possible permutations
TilingGroup(point=xx, info = cc, **kwargs)-> individual tile object.
	parent class is Cell
		TilingGroup -> child class for drawing the specific tiled wallpaper
		TilingGroupLine -> child class for drawing the specific tile with lines and the individual tile
		TilingGroup.generate() -> create a list of functions to generate tiling piece, and runs the functions
			TiningGroup.run()
				-> loop over the function list
					-> functions are methods in Cell






# GWGPM

#### 本文件夹

（1）run **batch_production.py** 生成17种对称型: 
（2）run **production_with_line.py** 生成带有镜像旋转点的图
（3）**batch_production_run.ipynb** 生成单张图片或者批量生成图片

*注：本文件使用相对路径导包，若需单独运行 python文件，则以**wallpaper_groups_image_production**文件夹为根目录；若运行 jupyter文件无限制，只需注意导入图片路径*





### 图片文件夹:

##### ../images：

|—ori_img：原始图像

|—cir_images：多角度旋转图形结果图

|—output：wallpaper group结果图

|—output_with_line：带旋转点、镜像轴等标注的wallpaper group结果图



`p1/1 正方形、p1/2 矩形、p1/3 平行四边形、p1/4 菱形、p1/5 六边形`

`p2/2、 p2/3、 p2/4`

`pm/1、pm/2`、`pg/2`、`cm/4`、`pmm/1`、`pmm/2`、`pmg/2`、`pgg/2`、`cmm/1、cmm/4`

`p3/5`、`p3m1/5`、`p31m/5`

`p4/1`、`p4g/1`、`p4m/1`

`p6/5`、`p6m/5`
