# OUC Feed Server

## 教程 - 生成订阅源链接

### 流程

* 获取当前所有的文章分类
* 用户选择要订阅的分类
* 发送用户选择的分类到服务端，得到分类标识
* 根据分类标识生成订阅链接

服务端提供的基础 API 是 [**RESTful Web API**](http://zh.wikipedia.org/zh-cn/REST)，同时也提供了以此为基础的 **JavaScript API**。

对于 Web 应用等便于执行 JavaScript 的环境，可以选择使用 JavaScript API；其他环境可以选择使用 RESTful Web API。

_这份教程使用运行在 http://oucfeed.duapp.com/ 的服务端作为示例，如果使用运行在其他地方的服务端请自行替换下文中的相关内容。_

### 使用 RESTful Web API

_使用 RESTful Web API 生成订阅源链接时，往返于服务器之间的数据都是 [**JSON**](http://www.json.org/json-zh.html) 格式。_

#### 获取当前所有的文章分类

    GET http://oucfeed.duapp.com/category

返回值为一个描述了现有文章分类的 JSON 字符串，类似于：

    {
        "教务处": {
        	"学业与学籍管理科": {},
            "教学运行管理科": {},
            "实验实践教学科": {}
        },
    	"观海听涛": {
            "新闻主页": {
            	"海大要闻主页": {
            		"新闻列表": {}
                },
                "活动预览": {},
                "通知公告": {}
            }
        }
    }

在这些键值对中，键表示一个分类的名字，对应的值为此分类下的子分类。子分类也是类似的键值对，如果某一分类下面没有子分类，那么值为空的键值对 `{}` 。

对于上面的例子，有 2 个顶级分类`教务处` 和`观海听涛`；分类`教务处`下面有 3 个子分类，这 3 个子分类下面都没有子分类；分类`观海听涛`下面有 1 个子分类，这个子分类下面又有 3 个子分类，其中的一个子分类`海大要闻主页`下面还有一个子分类。

#### 用户选择要订阅的分类

把上一步得到的分类们呈现给用户，由用户从中挑选出想要订阅分类们。

之后根据用户选择了的分类们生成和上面的现有分类类似 JSON 字符串。

例如用户选择了分类`教务处`和`海大要闻主页`，就要生成这样的 JSON：

    {
        "教务处": {},
    	"观海听涛": {
            "新闻主页": {
            	"海大要闻主页": {},
            }
        }
    }

这里的 `{}` 表示对应分类下的所有内容，包含所有的子分类。

#### 发送用户选择的分类到服务端，得到分类标识

把上一步得到的 JSON 字符串发送到服务端：

    POST http://oucfeed.duapp.com/profile
    
服务端会返回这种选择对应的标识，类似于：

    {
        "id": "osxqL42lv9avLG1JFeO-oa2DQOQ"
    }

这样我们就得到了分类标识 `osxqL42lv9avLG1JFeO-oa2DQOQ` 。

#### 根据分类标识生成订阅链接

服务端支持三种输出格式，分别是 RSS、Atom 和 JSON。其中前两者是标准格式，最后一个的格式容易通过观察得到，这里不再描述了。

三种输出的链接分别为：

    http://oucfeed.duapp.com/rss/<分类标识>
    http://oucfeed.duapp.com/atom/<分类标识>
    http://oucfeed.duapp.com/news/<分类标识>

对于上一步的标识，订阅链接就是：

    http://oucfeed.duapp.com/rss/osxqL42lv9avLG1JFeO-oa2DQOQ
    http://oucfeed.duapp.com/atom/osxqL42lv9avLG1JFeO-oa2DQOQ
    http://oucfeed.duapp.com/news/osxqL42lv9avLG1JFeO-oa2DQOQ
    
可以把这些链接提供给支持相应格式的阅读器。

### 使用 JavaScript API

_JavaScript API 是通过 AJAX 调用上面描述的 RESTful Web API 来工作的。_

_往返的数据格式与上面相同，只是被解析为了 JavaScript 对象，不再重复描述。_

_服务端支持 [CORS](https://zh.wikipedia.org/wiki/CORS)，可以从任何地方跨域访问。_

使用 JavaScript API，首先需要引入相关的 js 文件。

    <script src="http://oucfeed.duapp.com/oucfeed.js"></script>

#### 获取当前所有的文章分类

    oucfeed.getCategory(function (category) {
        // category 为现有文章分类
    })

#### 用户选择要订阅的分类

和直接使用 RESTful Web API 时类似，但是需要生成 JavaScript 对象而不是 JSON 字符串

#### 发送用户选择的分类到服务端，得到分类标识

    oucfeed.postProfile(profile, function (data) {
        // profile 为上一步得到的用户选择了的分类们
        // data.id 为对应的分类标识
    })

#### 根据分类标识生成订阅链接

    oucfeed.getFeedUrl(profile_id, feed_type)
    // profile_id 为上一步得到的分类标识
    // feed_type 为描述订阅源类型的字符串，比如 'RSS'、'Atom'
    // 这是一个同步方法，直接返回结果，不使用回调函数
