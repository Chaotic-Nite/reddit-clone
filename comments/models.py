from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from post_app.models import CommonFieldsMixin, Post

class Comment(CommonFieldsMixin, MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(max_length=4000)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    # class MPTTMeta:
        # order_insertion_by = ['-body']
        # level_attr = 'mptt_level'

    def __str__(self):
        return self.body
