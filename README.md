# crm_test
基于Django的权限管理组件


步骤：
	1、创建django project，CRM
	
	2、两个app
		- rbac，权限组件
		- web，销售管理系统
	
	3、app：rbac
		- 将权限相关的表编写到此app下的 modles.py中

	4、app：web
		- 将权限相关的表编写到此app下的 modles.py中
		- 销售系统的业务相关的代码
	
	5、两个APP的整合
		销售管理系统中的URL：
		1、基于admin进行权限信息的录入
		2、基于admin进行权限和角色信息的分配
	
	6、快速完成一个基于权限控制，
		1、登录页面师傅有权访问。
		2、POST请求，用户登录检验是否合法。
		3、获取当前用户相关的所有权限并放入session。
		4、再次向服务端发起请求，编写中间件对用户当前访问的url进行权限判断（是否在session中）

	7、功能的完善，将权限相关的功能放到rbac应用下，以便于以后组件的应用。
		a、用户登录和权限初始化拆分
		b、配置文件应用

	总结：6/7属于进行权限控制


	8、动态菜单的功能
		- 一级菜单
			- 问题：如何实现动态显示菜单？
				a、表结构 + 录入菜单数据
				b、获取菜单信息保存到 session
				c、模板中显示菜单信息（session）
					ps： inclusion_tag

		- 二级菜单
		  a、session中储存的菜单信息结构
		  b、数据表结构
		  c、页面显示（inclusion_tag中循环显示）


	9、点击菜单的权限是，默认选中或默认展开。
		当点击某个不能成为菜单的权限是，指定一个可以成为菜单的权限，让其默认选中以及展开
		a、数据库设计
		b、思路
			- 登录，做权限和菜单的初始化
				- 获取菜单信息
				- 获取权限信息
			- 再次来访问
				- 中间件进行权限的效验（根据权限信息）
				获取ID 或 PID （应该被选中的可以做菜单的权限 ID）

			- 模板中使用inclusion_tag 生成动态菜单（根据菜单信息进行动态生成）

	10、路劲导航





	
	11、权限的粒度控制到按钮级别
	总结：
		- 权限控制
		- 动态菜单
		- 权限分配
		问题：让你为某个用户分配一个角色？某个人分配一个权限。
		答案：
			- django.admin来进行操作。

	12、权限分配
		a、角色管理
			知识点：
				- ModelForm
				- 根据 namespace 和 name 反向生成 URL。
				- 模板的查找顺序

		b、用户管理
			知识点：
				- ModelForm
					- 字段的自定制
					- 钩子方法
					- 错误提示（中文）
					- 重写 __init__ 方法，统一给所有字段添加属性（form-control）
				- 根据 namespace 和 name 反向生成 URL。
				- 模板的查找顺序

		c、菜单和权限管理
			目标：
				- 一级
				- 二级
				- 权限
			知识点：
				- 保留URL中的原搜索条件
				- 模板中整形转换成字符串 1|safa
				- ModelForm 定制 radio
				- ModelForm显示默认值
				- ModelForm save之前对其 instance 进行修改
				- BootstrapModelForm 基类 封装


		d、权限的批量操作
			- formset
				- 什么是formset？
					答：Form组件 或 ModelForm 用于做一个表单验证。 formset 用于做多个表单验证。
				- 应用场景？
					答：批量操作。
			- 自动发现项目中的URL
				- 问题：给你一个项目，请帮我获取当前项目中都有哪些URL 及 name？
				- 实现思路
			
			- 知识点
				- formset （ModelFormSet）
				- 自动发现项目中的URL
				- 唯一约束错误信息

            

		e、权限分配
			- 展示用户、角色、权限信息
			- 选择用户、角色时，页面上的默认选项。
			- 角色和权限分配（保存）



1、获取项目中的权限 set1
2、去数据库中获取已经录入的所有权限 set2


情况一：	自动发现 > 数据库 --> 实现批量添加    ps：通过name 进行比对
	set1 - set2 -->  添加
	+ forset

情况二：	数据库 > 自动发现 --> 实现批量删除
	set2 - set2  --> 删除

情况三：  自动发现所有  > 数据库有  --->实现批量更新
	set3 = set1 + set2  -->  更新
	+ forset
	


知识点
	- 中间件
	- 过滤器
		- register.inclusion_tag
		- register.filter
		- register.simple_tag
	- modelform form 

		-  form = CustomerForm(data=request.POST, instance=obj)
			- data 和 instance 这个知识点
		- widget 插件
		- 钩子
			-全局钩子和局部钩子

