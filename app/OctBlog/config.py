#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

OctBlogSettings = {
    'post_types': ('post', 'page'),
    'allow_registration': os.environ.get('allow_registration', 'false').lower() == 'true',
    'allow_su_creation': os.environ.get('allow_su_creation', 'false').lower() == 'true',
    'allow_donate': os.environ.get('allow_donate', 'true').lower() == 'true',
    'auto_role': os.environ.get('auto_role', 'reader').lower(),
    'blog_meta': {
        'name': os.environ.get('name').decode('utf8') if os.environ.get('name') else 'Oct Blog',
        'subtitle': os.environ.get('subtitle').decode('utf8') if os.environ.get('subtitle') else 'Oct Blog Subtitle',
        'description': os.environ.get('description').decode('utf8') if os.environ.get('description') else 'Oct Blog Description',
        'owner': os.environ.get('owner').decode('utf8') if os.environ.get('owner') else 'Gevin',
        'keywords': os.environ.get('keywords').decode('utf8') if os.environ.get('keywords') else 'python,django,flask,docker,MongoDB',
        'google_site_verification': os.environ.get('google_site_verification') or '12345678',
        'baidu_site_verification': os.environ.get('baidu_site_verification') or '87654321',
        'sogou_site_verification': os.environ.get('sogou_site_verification') or '87654321',
    },
    'search_engine_submit_urls':{
        'baidu': os.environ.get('baidu_submit_url')
    },
    'pagination':{
        'per_page': int(os.environ.get('per_page', 5)),
        'admin_per_page': int(os.environ.get('admin_per_page', 10)),
        'archive_per_page': int(os.environ.get('admin_per_page', 20)),
    },
    'blog_comment':{
        'allow_comment': os.environ.get('allow_comment', 'true').lower() == 'true',
        'comment_type': os.environ.get('comment_type', 'duoshuo').lower(), # currently, OctBlog only supports duoshuo comment
        'comment_opt':{
            'duoshuo': 'oct-blog', # shotname of duoshuo
            }
    },
    'donation': {
        'allow_donate': os.environ.get('allow_donate', 'true').lower() == 'true',
        'donation_msg': os.environ.get('donation_msg', 'You can donate to me if the article makes sense to you').decode('utf8')
    },
    'copyright': {
        'display_copyright': os.environ.get('allow_donate', 'true').lower() == 'true',
        'copyright_msg': os.environ.get('copyright_msg', 'The article is not allowed to repost unless author authorized').decode('utf8')
    },
    'allow_share_article': os.environ.get('allow_share_article', 'true').lower() == 'true',
        
}

class Config(object):
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fjdljLJDL08_80jflKzcznv*c'
    MONGODB_SETTINGS = {'DB': 'OctBlog'}

    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates').replace('\\', '/')
    STATIC_PATH = os.path.join(BASE_DIR, 'static').replace('\\', '/')


    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True

class PrdConfig(Config):
    # DEBUG = False
    DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
    MONGODB_SETTINGS = {
            'db': 'OctBlog',
            'host': os.environ.get('MONGO_HOST') or 'localhost',
            # 'port': 12345
        }


config = {
    'dev': DevConfig,
    'prd': PrdConfig,
    'default': DevConfig,
}
