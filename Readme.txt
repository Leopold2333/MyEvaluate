运行方法：

1. 在python环境下执行

   pip install flask;  pip install pillow; pip install PyMySQL; pip install SQLAlchemy;

2. 在PYCharm下创建项目，并将源代码放入项目目录下

3. 打开MySQL服务，新建一个空数据库，并修改项目中config.py里数据库连接密码以及对应新建的数据库名

4. 将common\dboperate.py里最下方的注释去掉，执行db.drop_all()和db.create_all()；运行dboperate.py, 可以观察到数据库中建立好对应的表；之后将上面对应行添加注释。

5. 运行main.py ，浏览器访问127.0.0.1:5000 