## 用于open-falcon发送告警邮件的接口！！！

使用方式完全满足open-falcon的alarm模块的说明，只需要在alarm的cfg.json文件配置对应的接口即可

1）sendermail模块监听的地址和端口

	"http":{
		"enable":true,
		"listen":"0.0.0.0:3215"
	},

2)mail配置

	"mail":{
		"enable" : true,
		"sendConcurrent" : 5,
		"maxQueueSize" : 1000,
		"mailServerHost" : "smtp.ym.163.com", //邮件主机
		"mailServerPort" : 465, //发送端口
		"mailServerAccount" : "youchuanjiang@wanbei.tv", //邮箱地址
		"mailServerPasswd" : "wuhuan42@123.A" //邮箱密码
	}

3) 启动方式
    

    python3 bin/control.py start &
    
    python3 bin/control.py stop
    
    python3 bin/control.py restart &
    
    



   #####作者申明：水平有限，肯定有写的不好的地方，请指正！！！
    
    

