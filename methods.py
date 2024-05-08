from connection import pageApi

# function to post a text post on the page
def post_text(text):
    return pageApi.put_object(parent_object='me', connection_name='feed', message=text)
    
# function to post a photo on the page
def post_photo(photo_path, caption):
    return pageApi.put_photo(image=open(photo_path, 'rb'), message=caption)
    
# function to post a comment on a post
def post_comment(post_id, message):
    return pageApi.put_comment(object_id=post_id, message=message)
    
# function to post a reply on a comment
def post_reply(comment_id, message):
    return pageApi.put_comment(object_id=comment_id, message=message)
    
# function to delete a post
def delete_post(post_id):
    return pageApi.delete_object(post_id)
    
# function to delete a comment
def delete_comment(comment_id):
    return pageApi.delete_object(comment_id)
    
# function to get the posts on the page
def get_posts():
    posts = pageApi.get_connections(id='me', connection_name='feed')
    return posts

# function to get the comments on a post
def get_comments(post_id):
    comments = pageApi.get_connections(id=post_id, connection_name='comments')
    return comments

# function to get the replies on a comment
def get_replies(comment_id):
    replies = pageApi.get_connections(id=comment_id, connection_name='comments')
    return replies