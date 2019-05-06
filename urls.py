from handlers.commentitemhandler import CommentItemHandler
from handlers.mainpagehandler import MainPageHandler
from handlers.postinfohandler import PostInfoHandler
from handlers.searchpagehandler import SearchPageHandler
from handlers.singleitemhandler import SingleItemHandler


urls=[		
		(r'/po', PostInfoHandler),
        (r'/',MainPageHandler),
        (r'/item',SingleItemHandler),
        (r'/search',SearchPageHandler),
        (r'/comment',CommentItemHandler)
]
