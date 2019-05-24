from handlers.commentitemhandler import CommentItemHandler
from handlers.mainpagehandler 	 import MainPageHandler
from handlers.postinfohandler 	 import PostInfoHandler
from handlers.searchpagehandler  import SearchPageHandler
from handlers.singleitemhandler  import SingleItemHandler
from handlers.typeshandler 		 import TypesHandler
from handlers.rankpagehandler 	 import RankPageHandler
from handlers.signhandler 		 import SignHandler
from handlers.loginhandler 		 import LoginHandler
from handlers.logouthandler 	 import LogoutHandler


urls=[		
		(r'/',MainPageHandler),
		(r'/po', PostInfoHandler),
        (r'/item',SingleItemHandler),
        (r'/search',SearchPageHandler),
        (r'/comment',CommentItemHandler),
        (r'/types',TypesHandler),
        (r'/rank/(\w+)',RankPageHandler),
        (r"/login", LoginHandler),
        (r"/signin", SignHandler),
        (r"/logout", LogoutHandler),
]
